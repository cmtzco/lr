# LR

* [Installation](https://github.com/cmtzco/lr#organized-log-retrieval)
    * [Requirements]()
    * [Linux](https://github.com/cmtzco/lr/tree/lr-py#linux)
    * [Cygwin](https://github.com/cmtzco/lr/tree/lr-py#cygwin)
    * [Windows](https://github.com/cmtzco/lr/tree/lr-py#windowscmd)
* [Usage](https://github.com/cmtzco/lr#usage)
* [Features](https://github.com/cmtzco/lr#features)
* [Todo](https://github.com/cmtzco/lr#todo)

###Organized log retrieval

lr is currently used in a helpdesk environment for pulling logs from remote servers and 
organizing them based on the tickets they relate to.  lr makes it simple to pull down logs 
and avoid having to remember the SCP/RSYNC command format.  

##Installation

###Requirements
* Python (2.7)
* Pip


###Linux 

(Currently working on this as PIP will not install PySFTP)

*NOTE: sudo is required as it installs the script in the /bin folder*

`git clone https://github.com/cmtzco/lr`

`sudo python lr/install.py`

Follow the installation questions and Voila! its installed


###Cygwin

`git clone https://github.com/cmtzco/lr`

`python lr/install.py`

Follow the installation questions and Voila! its installed


###Windows(CMD)
####WORK IN PROGRESS




##Usage
`lr [OPTIONS] user host foldername`
* Options
    * -p or --path to specify a different remote path to crawl 
    * -l or --local to specify a different local path to save the logs to
    * -e or --ext to specify the file extension to search for

##Features
-Pull down all files with a .log extension in a common directory

-Compress them for quick downloading

-Archive

-Specify directories to search/use when running the installer


##TODO
- [X] Specify the extension of the files to look for.
- [] Scrape all logs on the server
- [] Pull from multiple servers

