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

### VSCode `git`

VSCode automatically detects if a `.git/` folder exists in the current project directory.

If a file has been changed, it is marked by the file explorer in orange and appends a M (modified) to the back of the filename.

If a file has been added, it is marked by the file explorer in green and appends a U (untracked) to the back of the filename.

#### Summary tab

The summary tab on the left is indicated by 3 green circles connected with branching lines.

This will show a full list of changes that have been made, for files that have been added, modified, and removed.

Files removed will only show up in this tab marked in red, with the filename crossed out and a D (deleted) appaneded to the back of the filename.

## Hands on with `git`

For learning purposes, we shall start off with some simple activities to get accustomed with the `git` workflows using the `git` program natively.

### Using `git` for version control

#### Setting up

1. Create a new folder for this project

2. Open the folder in VSCode

3. Navigate to the folder by either using a separate terminal or using macOS's terminal

4. Add a file with the following content:

`poem.txt`
```
The west wind whispered,
And touched the eyelids of spring:
Her eyes, Primroses.
```

#### `init`

We can init `git` in the workspace with

```bash
git init
```

This creates the folder `.git/` in the current directory and adds configuration files to it.

The `git status` command will show a summary of all the files added/modified/deleted in this project:

```bash
sh@mbp poems % git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	poem.txt

nothing added to commit but untracked files present (use "git add" to track)
```

The "Source Control" tab on VSCode will show the summary similar to `git status`.

`poem.txt` will be listed as an untracked file under the "Changes" dropdown.

#### `add`

Adding files marks down a list of changes of their current state (compared to the previous), to save in a snapshot later.

1. Use the `git add <FILENAME>` command to add a file for tracking

```bash
sh@mbp poems % git add poem.txt
```

On VSCode, this can be achieved by hovering your cursor over the file and clicking on the `+` symbol to add it.

We can check the summary again with `git status` once our file has been added.

```bash
sh@mbp poems % git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   poem.txt
```

The "Source Control" tab will now show `poem.txt` under the "Staged Changes" dropdown.

Files that have been added are known as "staged" files.

##### Multiple files

It is possible to add multiple files at once with `git add <FILENAME1> <FILENAME2>`.

The alternative way to add all the files is with the `.` wildcard in place of a filename with `git add .`

On the VSCode "Source Control" tab, we may just click on the files we want to add selectively.

It is good practice to always examine your files first to make sure that your changes are correct and it does not contain any secrets before adding and committing them.

#### `commit`

Since we have marked down the changes to be saved in the previous step, the next thing to do will be to save the changes in a snapshot.

This is done by bundling all the changes into a single snapshot, to be used as a restore point.

1. Use the `git commit -m "<MESSAGE>"` command to commit your changes

```bash
sh@mbp poems % git commit -m "add poem"
[master (root-commit) 4eaeff1] add poem
 1 file changed, 3 insertions(+)
 create mode 100644 poem.txt
```

When a commit is made, it tells us the commit hash so that we can refer to this again when we want to use this as a restore point.

In this case, the commit hash is `4eaeff1`.

It also displays a summary of the number of (1) files changed, (2) lines inserted, and (3) lines deleted.

```bash
sh@mbp poems % git status
On branch master
nothing to commit, working tree clean
```

Since all our changes have already been committed, `git status` will display an empty list.

##### Commit message

Commit messages should describe the purpose of the changes made in a snapshot, so that we can understand why a change was made.

They are to be written in present tense, detailing the changes made.

- "add check for user permissions"
- "remove unused imports"
- "update README.md list of contributers"

The main idea is to keep your commit messages short and concise, describing them in as little words as possible.

While VSCode will show a warning when commit messages exceed 80 characters, it is alright as long as the message itself is informative.

When working with tickets, one convention is to prepend the ticket label to the commit message.

- "SEC-123 fix google auth email regex"

#### `log`

1. Add another file and commit it

`poem2.txt`
```
Whitecaps on the bay:
A broken signboard banging
In the April wind.
```

We can view all the commits that have been made with the `git log` command:

```bash
sh@mbp poems % git log
commit 0cfafcc63f66241b9ad07bcc7e51ec6ce75ef0cf (HEAD -> master)
Author: shaohui <ngshaohui@sea.com>
Date:   Tue Apr 25 16:31:28 2023 +0800

    add another poem

commit 4eaeff1cb864462f088aa506868521e392d973e4
Author: shaohui <ngshaohui@sea.com>
Date:   Tue Apr 25 16:00:37 2023 +0800

    add poem
```

A list of commit logs will be shown, from the newest to the oldest.

One thing to note is the hash `4eaeff1` we obtained previously during our commit only corresponds to the first 8 characters in the first commit `4eaeff1cb864462f088aa506868521e392d973e4`.

These 8 characters are sufficient to use instead of the entire commit hash.

#### Restoring a snapshot

To restore a snapshot, we use `git reset <COMMIT_HASH>`.

We will need to find out the commit hashes by running `git log` as in the previous step.

1. Delete a line from the first file `poem.txt` but keep the file

2. Delete the file `poem2.txt`

```bash
sh@mbp poems % git status
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   poem.txt
	deleted:    poem2.txt
```

3. Add files and commit the changes

```bash
sh@mbp poems % git log
commit c7409b588fe54103f5321f92557c9d6b58f043b1 (HEAD -> master)
Author: shaohui <ngshaohui@sea.com>
Date:   Tue Apr 25 17:44:55 2023 +0800

    random deletion

commit 0cfafcc63f66241b9ad07bcc7e51ec6ce75ef0cf
Author: shaohui <ngshaohui@sea.com>
Date:   Tue Apr 25 16:31:28 2023 +0800

    add another poem

commit 4eaeff1cb864462f088aa506868521e392d973e4
Author: shaohui <ngshaohui@sea.com>
Date:   Tue Apr 25 16:00:37 2023 +0800

    add poem
```

We will now try restoring from our snapshots.

The snapshot `0cfafcc63f66241b9ad07bcc7e51ec6ce75ef0cf` was where we had just added our second poem.

4. Use `git reset <HASH>` to restore to that snapshot

```bash
sh@mbp poems % git reset 0cfafcc63f66241b9ad07bcc7e51ec6ce75ef0cf
Unstaged changes after reset:
M	poem.txt
D	poem2.txt
sh@mbp poems % git status
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   poem.txt
	deleted:    poem2.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

Any change between the current state and that snapshot will be unstaged.

Note that the files are not restored immediately, unless we discard the changes.

We can add the `--hard` flag to restore the snapshot completely, discarding any changes we have not saved.

5. Use `git reset --hard` to discard the changes in order to restore the snapshot completely

```bash
sh@mbp poems % git reset --hard
HEAD is now at 0cfafcc add another poem
```

Note that this can be combined with the git reset command previously as a single step

`git reset 0cfafcc63f66241b9ad07bcc7e51ec6ce75ef0cf --hard`

### Using `git` for remote storage

#### Add a remote url

1. Create an account on Github for us to use as remote storage.

2. Initialise a new repository

Once a repository has been initialised, take of the instructions in "…or push an existing repository from the command line" as we already have an existing repository locally.

```bash
git remote add origin git@github.com:shinlos/learngit.git
```

In this case, `git@github.com:shinlos/learngit.git` is the remote url, and we have named it the `origin` remote.

3. Add your remote url according to the given instructions

##### Origin

It is possible to have multiple origins, but this is usually rather rare.

Most projects will only have a single remote, and it will be called `origin`.

#### `push`

In the previous step when creating our repository, the instructions for "…or push an existing repository from the command line" also comes with instructions on how to push the current branch.

1. Push your branch onto the remote repository

```bash
git branch -M main
git push -u origin main
```

The first step `-M` renames the current branch you are in to `main` to standardise the name of all the "main" (as in primary) branches.

The next step specifies that we want to (1) set our upstream as `origin` remote url and (2) push the `main` branch.

##### Visualisation before push

  Local Repository                   Remote Repository
  (your computer)                (hosted on GitHub or GitLab)

 +-------------+                 no commits
 |  commit A   |
 +-------------+
 |  commit B   |
 +-------------+
 |  commit C   |
 +-------------+
 |  commit D   |
 +-------------+
 |  commit E   |
 +-------------+

##### Visualisation after push

  Local Repository                   Remote Repository
  (your computer)                (hosted on GitHub or GitLab)

 +-------------+                 +------------------+
 |  commit A   |                 |    commit A      |
 +-------------+                 +------------------+
 |  commit B   |                 |    commit B      |
 +-------------+                 +------------------+
 |  commit C   |                 |    commit C      |
 +-------------+                 +------------------+
 |  commit D   |                 |    commit D      |
 +-------------+                 +------------------+
 |  commit E   |                 |    commit E      |
 +-------------+                 +------------------+

##### Branches

Branches are a way to work on multiple features for a codebase at the same time (branching off).

In our context of learning, we will solely be working with the `main` branch.

However, do note that most projects do utilise multiple branches, usually separated by feature or product versions.

#### `clone`

1. Delete the folder from your computer

This simulates the context where we do not have

#### `pull`

  Local Repository                   Remote Repository                   Local Repository
  (your computer)                (hosted on GitHub or GitLab)            (other computer)

 +-------------+                 +------------------+                    +-------------+
 |  commit A   |                 |    commit A      |                    |  commit A   |
 +-------------+                 +------------------+                    +-------------+
 |  commit B   |                 |    commit B      |                    |  commit B   |
 +-------------+                 +------------------+                    +-------------+
                                 |    commit C      |                    |  commit C   |
                                 +------------------+                    +-------------+
                                 |    commit D      |                    |  commit D   |
                                 +------------------+                    +-------------+
                                 |    commit E      |                    |  commit E   |
                                 +------------------+                    +-------------+

If another user adds new commits to the remote repository, your local repository might be behind on commits.

We will need to download the additional data to synchronise with the remote repository.

1. Use `git pull` to download additional commits from the remote to your local repository.

```bash
git pull
```

##### No new data

It is possible that you already have all the newest commits.

In this case, a message will be shown that you are "already up to date".

```bash
sh@mbp poems % git pull
Already up to date.
```

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

## `.gitconfig`

It is possible to add alias commands and beautify the `git log` output.

```
[alias]
  st = status
  co = checkout
  ci = commit
  br = branch
  lg = log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative
```

```bash
sh@mbp poems % git lg
* 4eaeff1 - (HEAD -> master) add poem (29 minutes ago) <shaohui>
```

## Extra reading

- data vs binary files
- multiple branches

## Disclaimers

- ASCII images generated and adapted from ChatGPT3
