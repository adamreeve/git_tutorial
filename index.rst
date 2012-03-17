ABI Summer Tutorial: Version Control With Git
=============================================

Getting Started
---------------

If Git isn't installed already, it can be installed from the git-core
package if you're using Linux or by downloading msysGit for Windows.

The first thing that must be done before using Git is to tell it
your name and email address. These will be associated with any
commits you make::

  git config --global user.name "Adam Reeve"
  git config --global user.email "aree035@aucklanduni.ac.nz"

If you are using a graphical Git client such as Tortoise Git on Windows
or gitg on Linux there will be an option to edit these settings.


Creating a Repository
---------------------

You can initialise a new Git repository in an existing directory with::

  git init

Or to create a new directory::

  git init my_project


Cloning an Existing Repository
------------------------------

You can clone an existing repository from a local path or from a URL. To
clone the repository for this tutorial, run::

  git clone https://github.com/adamreeve/git_tutorial.git

This will create a git_tutorial directory in your current directory, so
change into that directory now::

  cd git_tutorial


Making and Committing Changes
-----------------------------

Run :command:`git status` and you should get a message that there are
no changes to be staged and no staged changes to be committed.

Now make a change to the :file:`index.rst` file and run :command:`git status`
again. You should see that you still have no changes staged to commit
but you have an unstaged change.

Run :command:`git diff` go see what changes you have made. Now add your
change to the staging area::

  git add index.rst

And run :command:`git status` again. You will see that there are no unstaged
changes but one file has changes that are staged.

Now run :command:`git diff` and there should be no changes. This is because
:command:`git diff` compares your working directory with the staging area
by default. To see what changes are in the staging area and would be committed,
run::

  git diff --cached

If you've decided that you no longer want to commit a change that you've
added to the staging area, you'll need to unstage that file by running::

  git reset HEAD index.rst

Note that git tells you how to stage and unstage changes in the output of
the :command:`git status` command.

If you then decide that your change is rubbish and you don't want to remove
it completely, you can checkout a clean version of the changed file::

  git checkout -- index.rst

The "--" before the file path isn't required but is recommended as it means that
any further command options are file paths, which prevents confusion when you
have a file named the same as a branch (as :command:`git checkout` is also used
for checking out a branch).

Now make another change and add it to the staging area, then commit it::

  git commit -m "My awesome change"

You can either specify a commit message on the command line with the "-m"
option or if you leave that option off, git will open a text editor to allow
you to enter a message. By default this is vim, but you might want to change
it to something else, for example::

  git config --global core.editor "nano"


Branches and Merging
--------------------

It's always a good idea to create a new branch for any new feature you're working
on in a project::

  git branch new_feature

This will create a new branch that points to your current head commit. You can
specify which commit the new branch should point to::

  git branch another_feature master

To delete a branch::

  git branch -d another_feature

This will give an error if the branch hasn't been merged into another branch.

Now checkout the branch you created. If there are any differences between
your previous head commit and the branch you are checking out, your working
directory will be updated::

  git checkout new_feature

You can create a new branch and check it out in one go by using the "-b" option
to the checkout command::

  git checkout -b my_feature

Now make some changes and commit them on your new branch.
You can see a list of branches and the branch you're on at
any time by running::

  git branch


Resolving Conflicts
-------------------


Remotes and Remote Branches
---------------------------

As you originally cloned this repository, you have one remote repository
set up already called "origin". To list the remote repositories you've
added with their urls::

  git remote -v

Branches on a remote repository can be checked out or referred to in
other commands by prefixing them with the remote name. For example, to
show the head commit of the master branch on the origin repository::

  git show origin/master

To see all branches including those on remote repositories, you can use::

  git branch --all


Staging Parts of Files
----------------------

Most Git graphical interfaces allow you to stage only some changes in
a file. From the Git command line you can do this with the "--patch" or
"-p" option to the add command. Change a line at the top of this file
and then make another change further down. Now run::

  git add -p index.rst

Say yes to adding the first change but no to the second change,
then run :command:`git status`, :command:`git diff`, and
then :command:`git diff --cached`.


Rewriting History
-----------------

Git has powerful tools for allowing you to rearrange history so that you
can clean up work to make the history more clear. The most useful
one to know is :command:`git rebase --interactive`. Rebasing means
to move a series of commits onto a new base commit. You can also
use the rebase command and keep the base the same, but edit a series
of commits.

Make one change to this file then commit it, then make a second change.
Now use the rebase command with the interactive option to squash the
second commit into the first.

Note that if you simply want to modify the previous commit, it's easiest
to run :command:`git commit --amend` after you've staged the changes
you want to ammend to the previous commit.

Note that you can still access any rebased commits with by their hash,
and you can find the commits that you have recently checked out with the
:command:`git reflog` command. This means that if you have committed
something it's very hard to permanently lose that work.


* :ref:`genindex`
* :ref:`search`
