---
permalink: linux-basic-commands-cheatsheet
categories:
    - Engineering
tags:
    - linux
    - bash
---

Working flawlessly with Linux mostly depends on how well we know the Linux commands. It really needs time to be good at all the Linux commands. The purpose of this document is to list all the basic commands so that anyone can get help.

### Linux Command Structures

A command is a program that tells the system to do something. It has a structure like `command [options] [arguments]`

- The command works on a particular argument. `arguments` are like extra pieces of information to perform the command. Here `arguments` are like  function arguments that tell the command what to perform
- On the other hand, `options` are used to control the command behavior.
    - `options` are generally letter preceded by a hyphen(-). e.g. `ls -a`   or word preceded by a double hyphen(—). e.g. `ls --help`
    - More than one option can be used with a command in two forms. such as separate form and lumped form.
    - Separate form is like `command -[option] -[option] - [option]`. e.g. `ls -a -l -t`
    - For most commands, more than one option can be lumped together to form `command -[option][option]`. e.g. `ls -alt`. One thing to remember is that not all commands support lumped options but most command supports.

### sudo

`sudo` means superuser do. whenever `sudo` is used before any command, it allows the current user to have root privilege temporarily for the current command. 

```bash
sudo rm -rf dir1# recursively delete the dir1 folder as root user privilege
```

### Linux File System

The computer organizes files in a tree-like structure that is known as the file system. Linux has a single file tree system that begins with the root directory(/). One thing we always have to remember is that in Linux almost everything is a file including a USB Device, Hard disk, etc. 

- File names are not case sensitive
- file begin with`.` used for the configuration file

### Linux frequently used basic commands

- `cd` - To change directory
- `mkdir` - make/create directory
- `pwd` - Print Current directory
- `ls` - List Directory Content
- `cp` -  copy files and directory
- `mv` - Move or rename file
- `rm` - remove directory and files
- `rmdir` - Use to remove only empty directory. It does not delete directory that is not empty.
- `cat` - Concatenate and display the whole file
- `exit` to exit the terminal from the command line
- `clear` clear terminal

### Common Linux Flags

- `-h` - Help flag
- `-v` - indicate verbosely.

### Directory and Navigation

There are two ways to denote a path. relative path and absolute path. Relative path refers to a path relative to the current directory. On the other hand, the absolute path starts at the root(/) directory and we can reference it from anywhere in the file system.

- Shortcut notation to the directory
    - `/`   root directory
    - `.`   Current directory
    - `..` Parent directory
    - `~`   Home directory
    - `-`   Previous directory
- `pwd` Print the Current Working Directory
- `cd /` Go to the root directory
- `cd ..` Go to the parent directory
- `cd ~` Go to Home directory
- `cd -`Go to the previous directory
- `cd /dir1/dir2`  Navigate to a particular directory

### Folder & File Create

- `mkdir dir1` Create directory named dir1  inside the current working directory
- `mkdir -p /dir1/testDir`  Create a directory inside dir1. If dir1 does not exist the -p flag indicates that create parent directory `dir1` if needed.
- `touch shuvangkar.txt` Create a text file inside the current directory named shuvangkar.txt
- `touch /dir1/testfile` Create `testfile`  file inside dir1

### File and Directory Listing

- `ls` command options
    - -l = long listing
    - -a= list hiddent files
    - -r = list in reverse name
    - -t = list new files first
    - rt = list in reverse time(oldest first)
- `ls  -l /tmp/dir1/` show to long listing of all files inside `/tmp/dir1/`

Here is a example of file listing and what the different notations indicate. 

```bash
drwxr-xr-x 2 	pi 	pi 	4096 	May 25 20:47 Desktop
-rw-r--r-- 1 	pi 	pi 	5781 	Feb  3 07:07 ocr_pi.png
drwxrwxr-x 2 	pi 	pi 	4096 	Mar 10 12:20 python_games
--------     -------  -------  -------- ------------ -------------
   |             |        |         |         |             |
   |             |        |         |         |         File Name
   |             |        |         |         |
   |             |        |         |         +---  Modification Time
   |             |        |         |
   |             |        |         +-------------   Size (in bytes)
   |             |        |
   |             |        +-----------------------        Group
   |             |
   |             +--------------------------------        Owner
   |
   +----------------------------------------------   File Permissions
```

### Copy Files & Directories

- `cp [option] [source] [destination]` Common format for `cp` command.
- To perform the copy operation, the source must have read permission and the destination must have write permission. Otherwise, permission denied error is shown.
- The source can be single or multiple files or directories. destination have to be single file or directory
- `cp file1 backfile1` copy `file1` content to `backupfile`
- `cp file1.txt file2.txt dir1` copy `file1.txt` and `file2.txt` to the directory `dir1`. When copying multiple files the destination must be a directory.
- `cp -r -v  /tmp/sourcedir desDir/` copy `sourcedir` into `destDir`. `-r` flag indicates recursively means copying whole directory contents. `-v` indicate show verbose output while copying

### Move & Rename

Move command(mv) has two functions. By default Linux does not have rename option. So it rename file and folder. It default function is to move files and folder

- `mv [options] [source]  [destination]` Default syntax
- `mv file1.txt diffname.txt` rename `file1.txt` to `diffname.txt`
- `mv file1.txt file2.txt dir1` move both of the files in folder dir1
- `mv /tmp/testfile .` Move `testfile` to the current directory
- `mv *.txt dir2` move all text file to dir2 folder

### Delete Files & Directory

- `rm /dir1/testfile` remove `testfile` from `dir1` folder
- `rmdir /tmp/testdir` remove `testdir` if it is empty
- `rm -r /tmp/testdir` recursively delete `testdir` folder
- `rm -rf /tmp/testdir` -f flag indicate force delete. -r indicate recursively

### Ubuntu Software Install and Uninstall

In Linux, world software is the package. Different Linux distribution has different package management tools. RedHat has yum, Debian has apt. apt(Advanced Packaging Tool) is the default package management tool for Ubuntu 

- `sudo apt update` update the local package list with the latest change made in the repositories
- `sudo apt upgrade` First update package index using update command and then this command upgrades all package
- `sudo apt install <package_name>` Install a particular package from package_name
- `sudo apt install -y git` The option -y tells the apt to assume the answer to all prompts is yes
- `sudo apt remove  <package_name>` remove package but leave configs
- `sudo apt purge <package_name>` remove package and configs. It may not be the desired effect. So use with caution
- `apt search filezilla` search `filezilla` package
- `apt autoremove` remove the unnecessary package file

Note: While apt is a command-line tool, it is intended to be used interactively, and not to be called from non-interactive scripts. The apt-get command should be used in scripts (perhaps with the --quiet flag). For basic commands the syntax of the two tools is identical.

### Install package from .deb file

- download the .deb package. such as `sublime.deb`
- Go to the file directory and install the package using the command `sudo apt install ./sublime.deb`

### How To Get Help

Linux manual is a great source of getting information related to any command. Here is multiple examples of how we can get information related to `gzip`

- `man -k gzip` finds gzip related manual
- `gzip --help`   print quick list of manual
- `man gzip` Manual open

### Linux Networking

- `ip -j -p addr show` To list network details in JSON format

### Generate SSH Key and Copy on the clipboard

1. /dev/zero is a special file that provides an endless stream of null characters that is used to create file or memory pages. 

```bash
sudo apt install xclip -y #xclip will copy the ssh file
cat /dev/zero | ssh-keygen -t ed25519 -C "keyname" -q -N "passphrase"
xclip -sel clip <~/.ssh/id_ed25519.pub

```

### More commands

- `name -a` It prints all the system information in the following order: Kernel name, network node hostname, kernel release date, kernel version, machine hardware name, hardware platform, operating system

### Deal with Executable

- `which mv` which command returns the path of executables. Here return the location of the move command

### More Linux command documents

Here is the list of cheat sheets we can explore more. 

1. IP command cheatsheet

[](https://access.redhat.com/sites/default/files/attachments/rh_ip_command_cheatsheet_1214_jcs_print.pdf)

### Control Service

`systemctl` and `service` are two commands to control services. 

`service` is high level command used for `start,` `restart`, `stop`, `status` of a service. 

On the other hand `systemctl` can do lot more than `service`.  It can load service parallel at startup, it can mask or unmask service and lot more. 

- `service script-name command` command can be `start,` `restart`, `stop`
- `systemctl command servicename.service` command  = start/stop/enable/reload/restart/