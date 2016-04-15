# LR

* [Installation](https://github.com/cmtzco/lr#organized-log-retrieval)
* [Usage](https://github.com/cmtzco/lr#usage)
* [Features](https://github.com/cmtzco/lr#features)
* [Todo](https://github.com/cmtzco/lr#todo)

###Organized log retrieval

lr is currently used in a helrdesk environment for pulling logs from remote servers and 
organizing them based on the tickets they relate to.  lr makes it simple to pull down logs 
and avoid having to remember the SCP/RSYNC command format.  

##Installation
*NOTE: sudo is required as it installs the script in the /bin folder*

`git clone https://github.com/cmtzco/lr`

*NOTE: You will want to edit the `lr` file inside the `lr` directory before you do the install script to make sure that you specify the base directories.  Currently `install` is being worked on to ensure that this can be configured via the script* 

`sudo ./lr/install [remote log path] [local log path] [processed log path]` *Specify the paths in the command*

or

`sudo ./lr/install` *Be sure to edit the `lr` file if you do not include the log paths in the command*

##Usage
`lr username hostname ticketnumber`

`lr username hostname ticketnumber /custom/path/to/search`

`lr username hostname ticketnumber /custom/path/to/search "fileextension"`

*NOTE: The extension and custom path are currently a work in progress since they need to be able to run independent of each other.*

##Features
-Pull down all files with a .log extension in a common directory

-Compress them for quick downloading

-Archive

-Specify directories to search/use when running the installer


##TODO
- [] Specify the extension of the files to look for.
- [] Scrape all logs on the server
- [] Pull from multiple servers

