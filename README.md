# project-recommendations-site

This repository contains the "built" versions of the Markdown files for
OSVTAC's open source voting system project recommendations. (OSVTAC stands
for San Francisco's [Open Source Voting System Technical Advisory
Committee][osvtac].)

The "source" Markdown files for the recommendations are located in the
following repository: <https://github.com/OSVTAC/project-recommendations>. If
you would like to contribute suggestions on the recommendations themselves,
you should consult the `README` file of that repository.

The repository for OSVTAC's website includes the repository you are currently
viewing as a submodule: <https://github.com/OSVTAC/OSVTAC.github.io>. The
Markdown gets converted to HTML on the server side by [GitHub
Pages][github-pages] when the website repository is published to the web.

The remainder of this README includes instructions for rebuilding the
Markdown files (i.e. updating the contents of this repository) prior to
committing, as well as previewing these files in a browser to check that
things are working before pushing. You must be familiar with Git,
[Markdown][markdown], and using the command-line.


## Fork the repository

First, fork the repository to your personal account on GitHub.

Then, clone your fork to your local machine:

    $ git clone https://github.com/<your-username>/project-recommendations-site.git
    $ cd project-recommendations-site
    $ git submodule update --init --recursive

The `git submodule` command is present because the repository uses a Git
[submodule][git-submodules] to store binary files referenced by the
recommendations (e.g. PDF's).


## System Setup

Previewing the files in your browser requires (1) having a recent version
of [Python](https://www.python.org/) to _build_ the final Markdown files,
and (2) using [Jekyll][jekyll-github] to _render_ those Markdown files for
viewing in your browser.

We explain how to install these two things below.


### Python

You must have Python 3.6 or greater installed to run the build script.
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
[osvtac]: https://osvtac.github.io/
[recommendations-repo]: https://github.com/OSVTAC/project-recommendations
[ruby]: https://www.ruby-lang.org
