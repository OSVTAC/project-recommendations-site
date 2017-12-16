"""
Script to build the Markdown files for publishing to the web.

Some of the things this script does are--

1. generate the table of contents with hyperlinks to each section, and
2. generate both "single-page" and "multi-page" versions of the
   document.

Usage:

From the repository root, run:

    $ python _scripts/build.py

The script should be run with Python 3.6 or newer (because it uses
f-strings, for example).
"""

# build.py script to build Markdown files for publishing with Jekyll.
#
# Copyright (C) 2017  Christopher Jerdonek
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
# The author(s) can be reached at--
#
#   Christopher Jerdonek <chris.jerdonek@gmail.com>
#

import argparse
from datetime import date, datetime
import json
import logging
import os
import functools
import re
import subprocess
import sys
from textwrap import dedent


_log = logging.getLogger(__name__)


SOURCE_DIRECTORY = '_source'

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


def get_submodule_sha(repo_dir, submodule):
    """
    Args:
      repo_dir: the path to the repository containing the submodule.
      submodule_path: the path to the submodule, relative to the repository
        root.
    """
    cmd = 'git submodule status'
    args = cmd.split()
    args.append(submodule)
    proc = subprocess.run(args, stdout=subprocess.PIPE, cwd=repo_dir)
    stdout = proc.stdout.decode('utf-8')
    # The output can look like this, for example:
    # "-72bfdd96151561bbbb6dc834ef38a5cf5cf6031d files"
    parts = stdout.split()
    part = parts[0]
    sha = part[1:]

    return sha


def get_source_path(name):
    """
    Return the path to a Markdown file in the _source directory.
    """
    return os.path.join(SOURCE_DIRECTORY, f'{name}.md')


def read_file(path):
    with open(path, encoding='utf-8') as f:
        text = f.read()

    return text


def write_file(text, path):
    _log.info(f'writing file: {path}')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def write_sections(sections, name):
    """
    Args:
      name: the base portion of the file name, for example "index" for
        index.md.
    """
    text = '\n\n'.join(sections)
    write_file(text, f'{name}.md')


def read_source_file(name):
    """
    Read a Markdown file in the _source directory.
    """
    path = get_source_path(name)
    text = read_file(path)

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
        return f'<HeaderInfo object coords={self.coords!r} title={self.title}, page={self.page}>'

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
        line = f'{section}. {self.title}'

        return line

    def make_header_line(self):
        level = self.get_level()
        header_text = self.make_header_text()

        # We precede top-level sections with "##" since we reserve "#" for
        # the overall page header.  Thus, we need to add 1.
        prefix = (level + 1) * '#'

        line = f'{prefix} {header_text}'

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

        line = f'{indent}* [{header_text}]({page_name}#{anchor})'

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

    def render_copyright_page(self):
        copyright_text = read_source_file('copyright')

        sections = [
            self.page_intro,
            copyright_text,
        ]
        write_sections(sections, name='copyright')


def run_prep():
    """
    Run the prep.py script in the recommendations submodule.
    """
    prep_path = os.path.join('_scripts', 'prep.py')
    _log.info(f'running: {prep_path}')
    args = [sys.executable, prep_path]
    proc = subprocess.run(args, stdout=subprocess.PIPE, cwd=SOURCE_DIRECTORY)
    stdout = proc.stdout
    data = json.loads(stdout)

    meta = data['_meta']
    files_sha = meta['files_sha']
    last_approved = meta['last_approved']
    sections = meta['sections']

    headers = data['headers']
    header_infos = [HeaderInfo(**kwargs) for kwargs in headers]

    return files_sha, header_infos, last_approved, sections


def make_page_intro(last_approved, posted_date=None):
    if posted_date is None:
        posted_date = date.today()

    posted_date = posted_date.strftime(f'%B {posted_date.day}, {posted_date.year}')

    intro = dedent(f"""\
    # Open Source Voting System Project Recommendations

    (Approved by OSVTAC on {last_approved}.)

    Last posted: {posted_date}
    """)

    return intro


def to_date(given):
    """
    Return a datetime.date object.
    """
    dt = datetime.strptime(given, '%Y-%m-%d')
    return dt.date()


def parse_args():
    desc = 'Build the site Markdown files.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--posted-date', metavar='DATE', type=to_date, default=date.today(),
        help="a date in the form YYYY-MM-DD. Defaults to today's date.")

    args = parser.parse_args()
    posted_date = args.posted_date

    return posted_date


def main():
    logging.basicConfig(level=logging.INFO)

    posted_date = parse_args()
    # TODO: check that the source repo isn't dirty (in non-dev mode).
    files_sha, header_infos, last_approved, section_names = run_prep()

    page_intro = make_page_intro(last_approved, posted_date=posted_date)
    reference_links = read_source_file('reference-links')
    # The html in the following file was copied from the instructions on
    # https://creativecommons.org for using CC BY-SA 4.0 for your own
    # material.
    license_info = read_source_file('snippets/license-info')

    renderer = Renderer(page_intro, reference_links, license_info=license_info)

    _log.info('building sections...')
    sections = []
    for section_name in section_names:
        # TODO: eliminate the need to hard-code this directory name.
        section_path = os.path.join('pages', section_name)
        section = read_source_file(section_path)
        sections.append(section)
        renderer.render_section_page(section_name, section)

    renderer.render_index_page(header_infos)
    renderer.render_single_page_version(sections, header_infos)
    renderer.render_copyright_page()

    files_sha = get_submodule_sha(os.curdir, submodule=FILES_DIRECTORY)
    source_files_sha = get_submodule_sha(SOURCE_DIRECTORY, submodule=FILES_DIRECTORY)
    if source_files_sha != files_sha:
        msg = dedent(f"""\
        the "files" submodule shas in the source and site repositories do not match:
          source: {source_files_sha}
            site: {files_sha}
        You should update the source repository before committing.""")
        _log.warn(msg)


if __name__ == '__main__':
    main()
