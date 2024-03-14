# WELCOME TO THE TERMINAL
This is a notebook for understanding the shell or terminal. This tutorial is designed to be interactive, with participants following along on their own computers. Let's break down the session into segments. We will have the following:

1. Introduction to the terminal: How to open and close the terminal
2. Navigating the File System
3. Creating, Moving, and Deleting Files and Directories
4. Basic Command Line Tools

## Introduction to the terminal: 
- Objective: To understand what the terminal is and why it's powerful.
- Activity:
    - Mac: Press `Cmd + Space` to open Spotlight Search, type "Terminal", and press `Enter`. 
    - PC: Press Windows Key, type `"Command Prompt"` or `"PowerShell"`, and press `Enter`.
    - You can easily close by cliking on the `close` button. 

## Navigating the File System (10 minutes)
- Objective: Learn to move around the file system using the command line.
- Activity:
    - Type `pwd` to see your current directory. *This shows where you are in the file system.*
    - Type `ls` (Mac) or `dir` (PC) to list the contents of the current directory.
    - Navigate to your `Documents folder` by typing `cd Documents` (adjust if your system uses a different name or path).
    - Return to your home directory by typing `cd ~`.

## Manipulating Files and Directories
- Objective: Master creating, moving, renaming, and deleting files and folders.
- Activity:
    - Create a new directory called `DAPLTest` by typing `mkdir DAPLTest`.
    - Navigate into this directory with `cd DAPLTest`.
    - Create a new file named `test.txt` by typing `touch test.txt` (Mac) or `echo.> test.txt` (PC).
    - Write "Hello, Terminal!" to test.txt by typing `echo "Hello, Terminal!" > test.txt`.
    - Read the content of test.txt by typing `cat test.txt`.
    - Move test.txt to hello.txt by typing `mv test.txt hello.txt`.
    - Go back to the parent directory (`cd ..`) and delete the DAPLTest directory and all its contents with `rm -r DAPLTest` (Mac) or `rmdir /S /Q DAPLTest` (PC).

## Exploring Basic Command Line Tools (5 minutes)
- Objective: Get familiar with basic commands for file manipulation and viewing.
- Activity:
    - Navigate into your Documents directory, create a new file named `greet.txt`, using the instructions you learnt prior, with the text "Hello, World!".
    - View the content of greet.txt.
    - Use `grep "World" greet.txt` to search for the word "World" in the file. (Note: PC users might need to use `findstr "World" greet.txt` in Command Prompt.)
    - Create a copy of greet.txt named farewell.txt with `cp greet.txt farewell.txt` (Mac) or `copy greet.txt farewell.txt` (PC).
    - List all files starting with "f" using `ls f*` (Mac) or `dir f*` (PC).