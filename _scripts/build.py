# build.py script to build Markdown files for publishing with Jekyll.
#
# Copyright (C) 2017  Christopher Jerdonek
# Copyright (C) 2018  Carl Hage
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Contact info:
#
# The authors can be reached at (listed in chronological order of
# contributing)--
#
#   Christopher Jerdonek <chris.jerdonek@gmail.com>
#   Carl Hage <ch@carlhage.com>
#

"""
Script to build the Markdown files for publishing to the web.

Some of the things this script does are--

1. generate the table of contents with hyperlinks to each section, and
2. generate both "single-page" and "multi-page" versions of the
   document.

Usage:

From the repository root, run:

    $ python _scripts/build.py

For command help, including command-line options:

    $ python _scripts/build.py -h

The script requires Python 3.5 or higher.

Detailed Description:

1. The file "last-posted.txt" is written with the --posted-date or todays
   date in a human-friendly format, e.g. April 1, 2018.

2. The _source/scripts/prep.py is run to update sequence numbers in the
   source pages (sections), and return a json-formatted list of headers plus the
   list of section names and last approved date.

3. Creates a standard page header with title, approval, and last posted date.
   Creates a standard page footer with _source/snippets/license-info.
   The footer includes a copy of all references.

4. For each section .md file, creates a copy of the file in the top-level
   site directory with a standard page header and footer added.

5. An index page with the intro.md file, auto-generated table of contents
   page is created, then a combined single page .md file is created.
"""


import argparse
from datetime import date, datetime
import json
import logging
import os
from pathlib import Path
import subprocess
import sys
from textwrap import dedent


_log = logging.getLogger(__file__)


SOURCE_DIRECTORY = Path('_source')
LAST_POSTED_PATH = Path('last-posted.txt')

# The path to the files submodule.
FILES_DIRECTORY = 'files'

# See make_anchor() for the purpose of this dict.
# TODO: add more characters as needed.
ANCHOR_TRANS = {
    ' ': '-',
    '.': None,
    '&': None,
}

TOC_LINK = """\
* [Introduction & Table of Contents](index) (for multi-page version)"""

SINGLE_PAGE_LINK = """\
* [Single-page version](single-page) (long, can be used for printing)"""

# All files use UTF-8, no matter what locale settings are (e.g. LC_ALL=C)
# Some python libraries default to ASCII even with LANG=en_US.UTF-8
ENCODING = 'utf-8'


def get_submodule_sha(repo_dir, submodule):
    """
    Args:
      repo_dir: the path to the repository containing the submodule,
        as a path-like object.
      submodule_path: the path to the submodule (as a path-like object),
        relative to the repository root.
    """
    cmd = 'git submodule status'
    args = cmd.split()
    args.append(str(submodule))
    proc = subprocess.run(args, stdout=subprocess.PIPE, cwd=str(repo_dir))
    stdout = proc.stdout.decode(ENCODING)
    # The output can look like this, for example:
    # "-72bfdd96151561bbbb6dc834ef38a5cf5cf6031d files"
    parts = stdout.split()
    part = parts[0]
    # TODO: check what other symbols can appear at the beginning.
    sha = part.lstrip('+-')

    return sha


def get_source_path(name):
    """
    Return the path to a Markdown file in the _source directory.
    """
    return SOURCE_DIRECTORY / '{}.md'.format(name)


def write_file(text, path):
    path = Path(path)
    _log.info('writing file: {}'.format(path))
    path.write_text(text,encoding=ENCODING)


def write_sections(sections, name):
    """
    Args:
      name: the base portion of the file name, for example "index" for
        index.md.
    """
    text = '\n\n'.join(sections)
    write_file(text, '{}.md'.format(name))


def read_source_file(name):
    """
    Read a Markdown file in the _source directory.
    """
    path = get_source_path(name)
    text = path.read_text(encoding=ENCODING)

    return text


def lines_to_text(lines):
    text = '\n'.join(lines)
    text = text.strip()

    # End with a trailing newline.
    text += '\n'

    return text


def make_anchor(header_text):
    """
    Create and return the anchor label for a section header.

    Args:
      header_text: the text portion of a header line, which includes the
        dotted section number and title, but not the header line prefix
        which has the form "###".

    This function was written to mimic Jekyll's / GitHub Pages'
    auto-generation of element id's for header elements. For example,
    "5.2. Incremental Approach" should return "52-incremental-approach".
    """
    anchor = header_text.lower()
    trans = str.maketrans(ANCHOR_TRANS)
    anchor = anchor.translate(trans)

    return anchor


class HeaderInfo:

    """
    Encapsulates the information needed to generate a section header line.
    """

    def __init__(self, coords, title, page):
        """
        Args:
          coords: an iterable of integers representing a section number.
            For example, (2, 3, 1) represents section 2.3.1.
          title: the section title that should follow the section number in
            the rendered text.
          page: the name of the source Markdown file containing the header
            (e.g. "background" for "background.md").
        """
        self.coords = coords
        self.page = page
        self.title = title

    def __repr__(self):
        return ('<HeaderInfo object coords={!r} title={}, page={}>'
                .format(self.coords, self.title, self.page))

    def __str__(self):
        return self.make_header_text()

    def get_level(self):
        return len(self.coords)

    def make_header_text(self):
        """
        Generate and return the text portion of a header line, which
        includes the dotted section number and title, but not the header
        line prefix which has the form "###".
        """
        section = '.'.join(str(number) for number in self.coords)
        line = '{section}. {title}'.format(section=section, title=self.title)

        return line

    def make_header_line(self):
        level = self.get_level()
        header_text = self.make_header_text()

        # We precede top-level sections with "##" since we reserve "#" for
        # the overall page header.  Thus, we need to add 1.
        prefix = (level + 1) * '#'

        line = '{prefix} {header}'.format(prefix=prefix, header=header_text)

        return line

    def make_contents_line(self, page_name=None):
        """
        Makes a table of contents line for the current header.

        Args:
          page_name: the name of the page to which the contents entry
            should link.  Defaults to the name of the page that originally
            contained the header.

        An example with page_name None could be--

          "  * [2.2. Voting System](background#22-voting-system)"

        With page_name '', this same example would be--

          "  * [2.2. Voting System](#22-voting-system)"

        """
        if page_name is None:
            page_name = self.page

        level = self.get_level()
        indent = 2 * (level - 1) * ' '

        header_text = self.make_header_text()
        anchor = make_anchor(header_text)

        line = ('{indent}* [{header}]({page}#{anchor})'
                .format(indent=indent, header=header_text, page=page_name, anchor=anchor))

        return line


def make_contents(header_infos, page_name=None):
    """
    Args:
      header_infos: an iterable of HeaderInfo objects.
    """
    lines = ['## Contents', '']
    for header_info in header_infos:
        level = header_info.get_level()

        # Only render the first two levels.
        if level > 2:
            continue

        line = header_info.make_contents_line(page_name=page_name)
        lines.append(line)

    contents = lines_to_text(lines)

    return contents


class Renderer:

    """
    Responsible for writing the top-level Markdown files.
    """

    def __init__(self, page_intro, reference_links, license_info):
        self.license_info = license_info
        self.page_intro = page_intro
        self.reference_links = reference_links

    def write_rendered_file(self, name, intro_sections, main_sections):
        """
        Args:
          intro_sections, main_sections: the intro sections and main
            sections, respectively.  Each value should be an iterable of
            strings, one for each section.  Moreover, each string section
            should end in a single trailing newline.
          name: the base portion of the file name, for example "index" for
            index.md.
        """
        sections = [
            self.page_intro,
            *intro_sections,
            self.license_info,
            *main_sections,
            self.reference_links,
            self.license_info,
        ]
        write_sections(sections, name=name)

    def render_index_page(self, header_infos):
        intro = read_source_file('intro')
        contents = make_contents(header_infos)

        self.write_rendered_file('index', [intro, SINGLE_PAGE_LINK], [contents])

    def render_section_page(self, name, body_text):
        self.write_rendered_file(name, [TOC_LINK, SINGLE_PAGE_LINK], [body_text])

    def render_single_page_version(self, sections, header_infos):
        # Pass '' for the page_name so that section links will point to
        # the same page that is being viewed.
        contents = make_contents(header_infos, page_name='')
        main_sections = [contents] + sections

        self.write_rendered_file('single-page', [TOC_LINK], main_sections)


def run_prep():
    """
    Run the prep.py script in the recommendations submodule.
    """
    prep_path = os.path.join('scripts', 'prep.py')
    _log.info('running: {}'.format(prep_path))
    args = [sys.executable, prep_path, '--dry-run', '--output-json']
    proc = subprocess.run(args, stdout=subprocess.PIPE, cwd=str(SOURCE_DIRECTORY), check=True)
    # We need to decode with Python 3.5.
    stdout = proc.stdout.decode('utf-8')
    data = json.loads(stdout)

    meta = data['_meta']
    has_changes = meta['has_changes']
    last_approved = meta['last_approved']
    section_names = meta['section_names']

    _log.info('found source changes: {}'.format(has_changes))

    headers = data['headers']
    header_infos = [HeaderInfo(**kwargs) for kwargs in headers]
    sections = data['sections']

    return header_infos, last_approved, section_names, sections


def make_page_intro(last_approved, posted_date):
    intro = dedent("""\
    # Open Source Voting System Project Recommendations

    (Approved by OSVTAC on {}.)

    Last posted: {}
    """).format(last_approved, posted_date)

    return intro


def to_date(given):
    """
    Return a datetime.date object, or None.
    """
    if not given:
        return None

    dt = datetime.strptime(given, '%Y-%m-%d')
    return dt.date()


def parse_args():
    desc = 'Build the site Markdown files.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--posted-date', metavar='DATE', type=to_date, default=date.today(),
        help='a date in the form YYYY-MM-DD, or the empty string not to '
             "update the posted date. Defaults to today's date.")

    args = parser.parse_args()
    posted_date = args.posted_date

    return posted_date


def main():
    logging.basicConfig(level=logging.INFO)

    posted_date = parse_args()
    if posted_date is not None:
        formatted_date = posted_date.strftime('%B {day}, {year}'
                            .format(day=posted_date.day, year=posted_date.year))
        write_file(formatted_date, LAST_POSTED_PATH)

    # TODO: check that the source repo isn't dirty (in non-dev mode)?
    result = run_prep()
    header_infos, last_approved, section_names, sections = result

    posted_date = LAST_POSTED_PATH.read_text(encoding=ENCODING)
    page_intro = make_page_intro(last_approved, posted_date=posted_date)
    reference_links = read_source_file('reference-links')
    # The html in the following file was copied from the instructions on
    # https://creativecommons.org for using CC BY-SA 4.0 for your own
    # material.
    license_info = read_source_file('snippets/license-info')

    renderer = Renderer(page_intro, reference_links, license_info=license_info)

    _log.info('building sections...')

    section_texts = []
    for section_name in section_names:
        section = sections[section_name]
        section_texts.append(section)
        renderer.render_section_page(section_name, section)

    renderer.render_index_page(header_infos)
    renderer.render_single_page_version(section_texts, header_infos)

    files_sha = get_submodule_sha(os.curdir, submodule=FILES_DIRECTORY)
    source_files_sha = get_submodule_sha(SOURCE_DIRECTORY, submodule=FILES_DIRECTORY)
    if source_files_sha != files_sha:
        msg = dedent("""\
        the "files" submodule shas in the source and site repositories do not match:
          source: {source}
            site: {site}
        You should update the source repository before committing.""").format(
            source=source_files_sha,
            site=files_sha,
        )
        _log.warn(msg)


if __name__ == '__main__':
    main()
