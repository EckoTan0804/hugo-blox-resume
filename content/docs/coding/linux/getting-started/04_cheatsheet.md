---
# ===== Title, summary, and position in the left sidebar =====
linktitle:   # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 105 # Position in the left sidebar
# ============================================================

# ========== Basic metadata ==========
title: Cheatsheet
date: 2024-08-20
draft: false

authors:
  - admin
tags:
  - Linux
  - OS
categories:
  - Coding
toc: true # Show table of contents
# ====================================

# ========== Advanced metadata =========
profile: false  # Show author profile?
reading_time: true # Show estimated reading time?
share: true  # Show social sharing links?
featured: true
comments: true  # Show comments?
disable_comment: false
commentable: true  # Allow visitors to comment? Supported by the Page, Post, and Book content types.
editable: false  # Allow visitors to edit the page? Supported by the Page, Post, and Book content types.

# Optional header image (relative to `assets/media/` folder).
header:
  caption: 
  image:  
---

## Introduction to Linux

| Command                 | Syntax                          | Description                           | Example                   |
| ----------------------- | ------------------------------- | ------------------------------------- | ------------------------- |
| List                    | `ls [OPTIONS] [FILE/DIRECTORY]` | List files and directories at path    | `ls /home/user/documents` |
| Print Working Directory | `pwd`                           | Print present working directory       | `pwd`                     |
| Change Directory        | `cd [DIRECTORY]`                | Change current directory              | `cd /home/user/documents` |
| Super user do           | `sudo [COMMAND]`                | Run command with superuser privileges | `sudo apt update`         |
| Text Editor             | `nano [FILE]`                   | Open file with Nano text editor       | `nano myfile.txt`         |

## Introduction to Linux Commands

### Informational, Navigational, & Management Commands

| Command            | Syntax                                | Description                                          | Example                              |
| ------------------ | ------------------------------------- | ---------------------------------------------------- | ------------------------------------ |
| Who Am I           | `whoami`                              | Return username                                      | `whoami`                             |
| User ID            | `id`                                  | Return current user or group ID                      | `id`                                 |
| System Information | `uname [OPTIONS]`                     | Display system information                           | `uname -a`                           |
| Manual Pages       | `man [COMMAND]`                       | Display manual page for a command                    | `man ls`                             |
| Curl               | `curl [OPTIONS] [URL]`                | Transfer data from or to server                      | `curl https://some_website.com`      |
| Date               | `date [OPTIONS]`                      | Display current date and time                        | `date`                               |
| Find               | `find [DIRECTORY] [OPTIONS]`          | Find files and directories at specified path         | `find /home/user -name '*.txt'`      |
| Make Directory     | `mkdir [DIRECTORY]`                   | Create new directory                                 | `mkdir myfolder`                     |
| Remove Directory   | `rmdir [DIRECTORY]`                   | Remove empty directory                               | `rmdir myfolder`                     |
| Process Status     | `ps [OPTIONS]`                        | Display process status information                   | `ps -ef`                             |
| Table of Processes | `top`                                 | Display live system resource usage                   | `top`                                |
| Disk Usage         | `df [OPTIONS] [FILESYSTEM]`           | Display disk space usage                             | `df -h`                              |
| Create Empty File  | `touch [FILE]`                        | Create new file or update timestamp                  | `touch myfile.txt`                   |
| Copy               | `cp [OPTIONS] [SOURCE] [DESTINATION]` | Copy files or directories from source to destination | `cp myfile.txt /home/user/documents` |
| Move               | `mv [OPTIONS] [SOURCE] [DESTINATION]` | Move or rename files and directories                 | `mv myfile.txt /home/user/documents` |
| Remove             | `rm [OPTIONS] [FILE/DIRECTORY]`       | Remove files                                         | `rm my_scratch_file.txt`             |
|                    |                                       | Remove nonempty directory                            | `rm -r path_to_temp_directory`       |
|                    | `rmdir [OPTIONS] [DIRECTORY]`         | Remove empty directory                               | `rmdir path_to_my_directory`         |
| Change Mode        | `chmod [OPTIONS] [MODE] [FILE]`       | Change file or directory permissions                 | `chmod u+x myfile.txt`               |

### Working with Text Files, Networking & Archiving Commands

| Command     | Syntax                            | Description                                                  | Example                                       |
| ----------- | --------------------------------- | ------------------------------------------------------------ | --------------------------------------------- |
| Concatenate | `cat [FILE]`                      | Display the contents of a file                               | `cat myfile.txt`                              |
|             |                                   | Concatentate and display contents of multiple files          | `cat file1 file2`                             |
| More        | `more [FILE]`                     | Display file one screen at a time                            | `more myfile.txt`                             |
| Head        | `head [OPTIONS] [FILE]`           | Display first N lines of file                                | `head -5 myfile.txt`                          |
| Tail        | `tail [OPTIONS] [FILE]`           | Display last N lines of file                                 | `tail -5 myfile.txt`                          |
| Echo        | `echo [ARGUMENTS]`                | Display arguments in console                                 | `echo Hello, World!`                          |
| Sort        | `sort [OPTIONS] [FILE]`           | Alphanumerically sort file contents                          | `sort file.txt`                               |
| Unique      | `uniq [OPTIONS] [FILE]`           | Report or remove consecutively repeated lines in file        | `uniq file.txt`                               |
| Word Count  | `wc [OPTIONS] [FILE]`             | Print the number of lines, words, and characters in a file   | `wc file.txt`                                 |
| Grep        | `grep [OPTIONS] PATTERN [FILE]`   | Search for a specified pattern in a file                     | `grep "hello" file.txt`                       |
| Paste       | `paste [OPTIONS] [FILE1] [FILE2]` | Merge lines of files side by side                            | `paste file1.txt file2.txt`                   |
| Cut         | `cut [OPTIONS] [FILE]`            | Remove sections from each line of a file                     | `cut -d":" -f1 /etc/passwd`                   |
| Tar         | `tar [OPTIONS] [FILE]`            | Archive files together into a single file                    | `tar -czvf archive.tar.gz /directory`         |
| Zip         | `zip [OPTIONS] [FILE]`            | Compress files into a zip archive                            | `zip archive.zip file1.txt file2.txt`         |
| Unzip       | `unzip [OPTIONS] [FILE]`          | Uncompress files from a zip archive                          | `unzip archive.zip`                           |
| Hostname    | `hostname`                        | Print the name of the current host system                    | `hostname`                                    |
| Ping        | `ping [OPTIONS] HOSTNAME/IP`      | Send ICMP ECHO_REQUEST packets to a network host             | `ping google.com`                             |
| Ifconfig    | `ifconfig [INTERFACE]`            | Display or configure network interface parameters            | `ifconfig`                                    |
| IP          | `ip [OPTIONS]`                    | Show or manipulate routing, devices, policy routing, and tunnels | `ip addr`                                     |
| Curl        | `curl [OPTIONS] URL`              | Transfer data from or to a server                            | `curl https://some_website.com`               |
| Wget        | `wget [OPTIONS] URL`              | Download files from the web                                  | `wget https://some_website.com/some_file.txt` |

## Introduction to Shell Scripting

| Command                                                    | Syntax                    | Description                                              | Example                                                      |
| ---------------------------------------------------------- | ------------------------- | -------------------------------------------------------- | ------------------------------------------------------------ |
| Shebang                                                    | `#!/bin/[shell]`          | First line of shell script                               | `#!/bin/bash`                                                |
| Pipe                                                       | filter1 \| filter2        | Chain any number of filters                              | `ls | sort -r`                                               |
| Locate executable                                          | `which [EXECUTABLE]`      | Display location of `bash` executable                    | `which bash`                                                 |
| Bash                                                       | `bash [SCRIPT]`           | Interpret and run script using Bash shell                | `bash script.txt`                                            |
| Set                                                        | `set [OPTION]`            | List all shell variables                                 | `set`                                                        |
| Define variable                                            | `[VARIABLE_NAME]=[VALUE]` | Define shell variable by name and assign value           | `name="John"`                                                |
| Read                                                       | `read [VARIABLE]`         | Read from standard input and store result in variable    | `read name`                                                  |
| Env                                                        | `env`                     | Print all environment variables and their values         | `env`                                                        |
| Export                                                     | `export [VARIABLE]`       | Extend scope of local variable to all child processes    | `export name`                                                |
| Crontab                                                    | `crontab [OPTIONS]`       | Open crontab default editor                              | `crontab -e`                                                 |
|                                                            |                           | List all cron jobs                                       | `crontab -l`                                                 |
| Schedule tasks to run at specified times using cron daemon | `m h dom mon dow command` | Append date/time to file every Sunday at 6:15 pm         | `15 18 * * 0 date >> sundays.txt`                            |
|                                                            |                           | Back up home directory every Monday at 3:00 am           | `0 3 * * 1 tar -cvf my_backup_path\my_archive.tar.gz $HOME\` |
|                                                            |                           | Run shell script first minute of first day of each month | `1 0 1 * * ./My_Script.sh `                                  |