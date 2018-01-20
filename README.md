# project-recommendations-site

This repository contains the "built" version of the Markdown files for
OSVTAC's open source voting system project recommendations. (OSVTAC stands
for San Francisco's [Open Source Voting System Technical Advisory
Committee][osvtac-site].)

The "source" Markdown files are located in the `project-recommendations`
repository: <https://github.com/OSVTAC/project-recommendations>. If you would
like to contribute suggestions to the document text, you should consult the
[`README`][recommendations-repo] file of that repository.

The current "site" repository serves two purposes:

1. It is used for displaying the committee's recommendations on OSVTAC's
website, which you can see [here][osvtac-recommendations]. The
[repository][osvtac-site-repo] for OSVTAC's website includes the current
repository as a submodule at the relative path `recommendations`. On the
server side, [GitHub Pages][github-pages] converts the Markdown files in this
repository to HTML when changes to the OSVTAC website repository are pushed
to master.

2. This repository can also be used to locally preview how the
recommendations look before pushing changes. Instructions for doing this are
below. **Note that the Markdown files checked into this repository are not
necessarily viewable within GitHub's UI.** For example, internal hyperlinks
will not work. Rather, previewing the HTML requires using Jekyll, as
described below.

The reason this repository is being kept separate from the
["project-recommendations"][recommendations-repo] repository containing the
source files is to keep the repository containing the source files cleaner
and simpler. By keeping build artifacts out of the source repository, the
commit history is also cleaner, which makes it easier to track contributions
to the text. This pattern also allows the _display_ of the recommendations to
be decoupled from the _content_.

The remainder of this README includes instructions for rebuilding the
Markdown files (i.e. updating the contents of this repository) prior to
committing, as well as previewing these files in a browser to check that
things are working before pushing. You must be familiar with Git,
[Markdown][markdown], and using the command-line.

TODO: also describe the recommended workflow.


## Build and rendering process overview

The [OSVTAC website][osvtac-site] displays OSVTAC's recommendations by
including the repository you are currently viewing as a
[submodule][git-submodules] of the repository for the OSVTAC website:
<https://github.com/OSVTAC/OSVTAC.github.io>. The repository you are viewing
contains the Markdown files for displaying the recommendations. These
Markdown files are auto-generated (aka "built") from the Markdown files in
the project-recommendations repository, which are the "source" files.

The repository you are viewing also contains a script for building the
Markdown files from the source Markdown files, which is described below. In
addition, for convenience, this repository also contains the
project-recommendations repository as a submodule, at the path `_source`.

When making non-trivial changes to the project recommendations, it is
recommended that you clone the current repository and work on your changes to
the document text in the submodule. This lets you preview the changes locally
while working.

To preview your changes to the recommendations locally, you can view the
project-recommendations-site repository in your browser using
[Jekyll][jekyll-github]. Make your changes to the project-recommendations
submodule, and then run the build script to update the html files served
locally by Jekyll. The sections below contain more detailed instructions on
how to do this.


## Fork the repository

First, fork the repository to your personal account on GitHub.

Then, clone your fork to your local machine:

    $ git clone https://github.com/<your-username>/project-recommendations-site.git
    $ cd project-recommendations-site
    $ git submodule update --init --recursive

The `git submodule update` command is needed because the repository contains
two Git [submodules][git-submodules]: one at the path `_source` for the
repository containing the source Markdown files, and one at the path `files`
to store binary files referenced by the recommendations (e.g. PDF's).


## System Setup

Previewing the files in your browser requires (1) having a recent version
of [Python](https://www.python.org/) to _build_ the final Markdown files,
and (2) using [Jekyll][jekyll-github] to _render_ those Markdown files for
viewing in your browser.

We explain how to install these two things below.


### Python

You must have Python 3.5 or greater installed to run the build script.
Instructions for installing Python can be found
[here](https://www.python.org/downloads/).


### Ruby & Jekyll

Running Jekyll requires [Ruby][ruby], so first install a current version of
Ruby. As of August 2017, the latest stable version of Ruby was 2.4.1.

You can check what version of Ruby you are currently using by running:

    $ ruby --version

We recommend using [RVM][rvm] to install and manage the versions
of Ruby installed on your machine. Instructions for installing RVM are on
the RVM [home page][rvm], with more detailed instructions (e.g. for different
platforms) on the [Installing RVM][rvm-install] page.

[rvm]: https://rvm.io/
[rvm-install]: https://rvm.io/rvm/install

With RVM, you can list all of your
installed Ruby versions with:

    $ rvm list

Next, install Jekyll and the theme's dependencies, etc. From the repository
root:

    $ bundle install

The `bundle` command above installs each of the needed Ruby gems (project
dependencies), using the version numbers specified in
[`Gemfile.lock`](Gemfile.lock).


## Building the Markdown Files

From the repository root:

    $ python _scripts/build.py

This will read the Markdown files in the `_source` directory of the
repository and generate new Markdown files in the top-level directory
of the repository.

**Running the script above also rewrites the Markdown files in the `_source`
directory with new section numbers, so you should commit your changes
locally before running the script.**

You can also run the following for more advanced options:

    $ python _scripts/build.py --help


## Previewing Locally

After running the build script above, you can use the [Jekyll][jekyll-github]
command-line tool and preview your changes locally in your browser.  Jekyll
is what GitHub uses to render [GitHub Pages](https://pages.github.com/).
We describe more on this below.

The repository is configured in the [`_config.yml`](_config.yml) file to use
GitHub's ["slate"](https://github.com/pages-themes/slate) theme locally. This
theme was chosen because it is very similar to the theme of OSVTAC's site,
which OSVTAC uses to display these recommendations.

To run and preview the site locally, run the following from the repo root:

    $ bundle exec jekyll serve

This writes the generated pages to a subdirectory called `_site`.

Then browse to: [http://127.0.0.1:4000](http://127.0.0.1:4000).


[git-submodules]: https://git-scm.com/book/en/v2/Git-Tools-Submodules
[github-pages]: https://pages.github.com/
[jekyll-github]: https://jekyllrb.com/docs/github-pages/
[markdown]: https://guides.github.com/features/mastering-markdown/
[osvtac-site]: https://osvtac.github.io/
[osvtac-recommendations]: https://osvtac.github.io/recommendations/
[osvtac-site-repo]: https://github.com/OSVTAC/OSVTAC.github.io
[recommendations-repo]: https://github.com/OSVTAC/project-recommendations
[ruby]: https://www.ruby-lang.org
