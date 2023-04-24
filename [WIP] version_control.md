# Version control

Having version control is effective for working with multiple iterations of a particular project.

We can also work on different copies of the same project, and be able to synchronise them on the same timeline.

This allows multiple people to work on the same project simultaneously (or the same person), on different machines.

## Popular version control tools

- Dropbox
- Google Docs
- git
- mercurial

Commercial version control tools are often also offered as "cloud storage" applications, which handle both version control and storage.

On the other hand, tools like `git` and `mercurial` are both open source tools favoured by programmers.

Compared to commercial tools, they often only have very basic functionality, needing some degree of manual interaction and troubleshooting.

We will only be looking at `git` in this chapter.

## `git`

`git` is by far the most popular version control tool used by programmers.

### Version control

While it is meant for version controlling code files in general, it can be used for almost all types of data by all intents and purposes.

The gist of how `git` works for version control is:

1. Take a snapshot of data in a file at any time
2. Check the difference of current snapshot against older snapshots
3. Revert data back to an older snapshot
4. Change data from an older snapshot to a newer snapshot

This is achieved by saving the snapshots locally in a folder `.git/` on your system.

By gaining access to someone's `.git/` folder, it might be possible to recreate some files even without access to their source code.

### Remote storage

`git` can function on its own locally without access to any network, since it stores the data it needs in the `.git/` folder.

However if we wish to work on a project on another machine, we will need to store it somewhere remotely first.

A gist of how `git` works for remote storage is:

1. Set a remote location where the data should be stored
2. Upload the project's data to the remote location
3. Download the project's data from the remote location

This works by uploading all the files in the project, as well as the `.git/` folder onto the remote location.

Each time the remote location's data is changed, we will also need to update our local copy to stay in sync.

Likewise, when we change data locally we will also want to update the copy stored remotely.

### `git` vs Github?

Services such as Github, Gitlab, Gitbucket provide an interactive way to store and view the data we have version controlled using `git`.

They both have underlying mechanisms that rely on `git` to function, with your snapshots hosted on their services (similar to a cloud service).

The user is also required to use `git` to function with these services.

### VSCode `git` (TODO)

VSCode automatically detects if a `.git/` folder exists in the current project directory.

If a file has been changed, it is marked by the file explorer in orange and appends a M (modified) to the back of the filename.

If a file has been added, it is marked by the file explorer in green and appends a U (untracked) to the back of the filename.

#### Summary tab

The summary tab on the left is indicated by 3 green circles connected with branching lines.

This will show a full list of changes that have been made, for files that have been added, modified, and removed.

Files removed will only show up in this tab marked in red, with the filename crossed out and a D (deleted) appaneded to the back of the filename.

## Hands on with `git` (TODO)

For learning purposes, we shall start off with some simple activities to get accustomed with the `git` workflows using the `git` program natively.

### Using `git` for version control

#### Setting up

1. Create a new folder for this project

2. Open the folder in VSCode

3. Navigate to the folder by either using a separate terminal or using macOS's terminal

4. Add a file with the following contents:

`poem.txt`
```

```

#### `init`

We can init `git` in the workspace with

```bash
git init
```

This creates the folder `.git/` in the current directory and adds configuration files to it.

#### `add`

#### `commit`

### Using `git` for remote storage

### `push`

### `pull`

### `clone`

## Hands on with VSCode `git` (TODO)

### The `.git/` directory

This directory is where information relating to `git` for the project is stored, and does not need to be interacted with.

Since the folder name is prepended with a `.` this hides the folder by default on most systems.

When using the command line, we may use `ls -la` where the `-a` flag allows us to view hidden files and folders.

When zipping up the entire project, this will also cause hidden folders within it (like `.git/` and `.DS_Store`) to be included, which is a common way the `git` history is leaked unintentionally.

## `git` with user interface

Rather than interacting with the `git` program directly on the command line, we might work better with a user interface.

There are tools out there that provide a user interface wrapped on top of `git` for this purpose.

Some of the prominent UI `git` tools include:

- github desktop
- gitkraken
- sourcetree
- VSCode (with caveats)

Since VSCode is primarily meant as a code editor, the features it has are quite rudimentary but it suffices for most workflows.

## `git`-fu

There are bound to be complications that arise when using `git` to version control a file across different machines.

Here are some of the common problems and possible steps for remediation, or just information on potential problems with `git` workflows.

### Uncommit files (TODO)

### Change commit history (TODO)

### Merge conflict (TODO)

### Not a `git` repository

```
sh ~ % git add .
fatal: not a git repository (or any of the parent directories): .git
```

We can encounter this when executing `git` commands on a repository without a `.git/` folder.

This means that the folder has not been initialised with `git` yet.

If we are certain that this is the correct folder, we should initialise `git` with `git init` before continuing.

## Extra reading

- data vs binary files
- multiple branches
