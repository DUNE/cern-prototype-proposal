Proposal document for the CERN prototype detector and running.

* For editors:

Here is a quick start guide to using this repository.  It presents just one way to do things.

** Get started:

The first steps is to "=clone=" the GitHub repository

#+BEGIN_EXAMPLE
  $ git clone https://github.com/DUNE/cern-prototype-proposal.git
  $ cd cern-prototype-proposal/
  (edit files)
  $ git add yourfile.tex
  $ git commit -a -m "Some useful commit message"
#+END_EXAMPLE

** Updating your repository

From time to time you will want to "=pull=" contributions from others into your repository.

#+BEGIN_EXAMPLE
  $ git commit -a -m "Some useful commit message"
  $ git pull
#+END_EXAMPLE

** Pushing contributions back to GitHub

First, you will need a (free) [[https://github.com/][GitHub account]] and to send the user name to [[mailto:bv@bnl.gov][bv@bnl.gov]].  Be sure to mention *this* repository.

To "=push=" your commits back to GitHub do:

#+BEGIN_EXAMPLE
  $ git commit -a -m "Some useful commit message"
  $ git pull
  $ git push
  (enter user and password)
#+END_EXAMPLE

The "=pull=" is needed to first incorporate into your repository any changes that others may have pushed to GitHub since the last time you did a "=pull=".

If you get annoyed at using passwords all the time it is recommended that you [[https://help.github.com/articles/generating-ssh-keys/][use ssh keys]] but you can also [[https://help.github.com/articles/caching-your-github-password-in-git/][cache your password]].
** Autobuilder

A PDF of the documented is generated after recent commits and is available for download at:

  https://dune.bnl.gov/tmp/CERNproto.pdf



