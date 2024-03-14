# GITFLOW

## Introduction:
GitFlow is a branching model for Git, designed by `Vincent Driessen` in 2010. It's a robust framework for managing larger projects that require multiple developers working on different features simultaneously, while also ensuring that the main branch always maintains a state of readiness for production releases. Here's a brief overview of the key components and practices within GitFlow:

## Basic Structure:
The basic structure of git-flow follows these steps:

- Branch
- Develop
- Test
- Push
- Pull Request (aka "merge request" on some platforms)
- Merge

For the ppurposes of this lecture, we will talk about `pulling from github` and then you can read further and study wider on your own: 

### Pulling from github:
To pull changes from the origin in Git, particularly when working within Visual Studio Code (VS Code), involves fetching changes made in the remote repository and merging them into your current branch. This is a common operation when collaborating on projects with other developers, ensuring your local repository is up-to-date with the shared repository. Here’s a step-by-step guide to do this in VS Code:

**Step 1: Open Your Project in VS Code**
- Open Visual Studio Code.
- Navigate to `File > Open Folder...` and select your project directory.

**Step 2: Access the Integrated Terminal**
- Open the integrated terminal in VS Code by navigating to `Terminal > New Terminal` from the top menu. This gives you access to the command line within the VS Code interface.

**Step 3: Ensure You're on the Correct Branch**
Before pulling from the origin, make sure you're on the branch you want to update with remote changes.

- In the terminal, type `git branch` to see all the local branches and which branch you're currently on (indicated by a star `*`).
- If you need to switch to another branch, use `git checkout branch-name`, replacing `branch-name` with the name of the branch you want to switch to.

**Step 4: Pull from the Origin**
- To pull changes from the remote repository (origin) to your local branch, use the command: `git pull origin branch-name`, where `branch-name` is the name of the branch you’re updating.
- If you're on the branch already and want to pull changes from its upstream counterpart (the branch it tracks from the remote), simply use `git pull`.

**Step 5: Resolve Conflicts (If Any)**
If the pull operation results in merge conflicts (where changes in the remote branch conflict with your local changes), VS Code's editor will highlight these conflicts.
You can manually resolve these by editing the files to choose which changes to keep, or use VS Code's built-in merge conflict resolution tools.

**Step 6: Save and Continue**
After resolving any conflicts, save your files.
Use `git add .` to stage the resolved files, and then `git commit` to commit your merge. You might be prompted to enter a commit message if VS Code doesn't automatically do so for you.

## Further knowledge and readings:

### Branch:

You're about to start working on a feature. Before you get started, though, do one small thing: branch. Because git-flow requires that we do in-progress work on dedicated feature branches, we must create a branch to track progress on that feature, even if it's not done yet!

```c
# Switch to the main branch so your branch is based on the most recent work
git switch main
# Create the new branch named after the feature
git branch featureName
# Switch to the feature branch
git switch featureName
```

### Develop:
Edit the code to add the desired feature. In fact, make only the changes necessary for this feature. Your branch's commits should include only that feature. It helps to keep each branch focused on one feature... leading to quicker reviews, clearer merges, and an understandable git history.

As you code away, commit every time you finish something, pause to work on something else, and even taking a break to get lunch:

```c
git commit -m "Made progress:
- Worked on this
- Coded that
- Optimized such and such"

git push origin featureName
```

For the example shown below, we envision a trivial task: adding a README to the repo. First, create a branch and switch to it:

```c
$ git branch add-readme
$ git switch add-readme
Switched to branch 'add-readme'
```

### Test:
Ensure you run all the unit tests and regression tests, and add all the necessary documentation. Then, merge any recent changes to the `main` branch, into this feature branch:
```c
$ git fetch origin main
$ git merge main
```

### Push:
Finally, when it seems your feature is complete, and fully tested with the latest code from `main`, push it to GitHub:

