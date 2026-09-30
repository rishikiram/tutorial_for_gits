# Intorduction and Tutorial to Git, and Github

See the [git website](https://git-scm.com/) and [git book](https://git-scm.com/book/en/v2) for source material

## What is Git? ([1.2](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)/[1.3](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F))
 
Git is a *version control system*, which is 'a system that records changes to a file or set of files over time so that you can recall specific versions later.' This becomes essential when people are collaboratively developing a codebase. Notably it allows for easily maintaining an updated codebase shared between collaborators, and provides tools for merging different versions of code. Today, git is by far the most used version control system.

Git thinks of its data like a series of snapshots of a miniature filesystem. With Git, every time you commit, or save the state of your project, Git basically takes a picture of what all your files look like at that moment and stores a reference to that snapshot.

**Git vs Github**: Github is a platform that allows users to create, store, manage, and share their code *using git*. Lets compare the two: Git is a program that anyone can run on their computer, allowing users to manage a *repository*, or a set of files. Github is a service provided via the internet that allows users to store and share Git repositories. Git is the engine for the version control, and Github is the cloud service for Git repositories.

## Running Git ([1.4](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)/[1.5](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))

Git is an appliation. The most classic way to run it is through its command-line-interface, or CLI. There also exist many graphical user interfaces, such as a vscode extension and the github desktop app. In this tutorial we'll learn a set of git functions in the CLI, which is how all things git work behind the scenes.

## Git Repositories

A project that is managed by Git is called a *repository*, or a *repo*. 

You typically obtain a Git repository in one of two ways:
- You can take a local directory that is currently not under version control, and turn it into a Git repository, or
- You can *clone* (copy a remote repo from the internet onto your computer) an existing Git repository from elsewhere.

To turn a local directory into a Git repo you must
- navigate to the desired folder
- run this:
```bash
$ git init
```
To clone a repo you must
- navigate to the desired parent folder
- run this:
```bash
$ git clone https://[INSERT LINK TO REPO] 
```

All git repos will have a folder called `.git` which holds all the information about past snapshots