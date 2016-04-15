# LP
###Organized log retrieval

lp is currently used in a helpdesk environment for pulling logs from remote servers and 
organizing them based on the tickets they relate to.  lp makes it simple to pull down logs 
and avoid having to remember the SCP/RSYNC command format.  

##Installation
*NOTE: sudo is required as it installs the script in the /bin folder*

`git clone https://github.com/mrMuffins/lp`

*NOTE: You will want to edit the `lp` file inside the `lp` directory before you do the install script to make sure that you specify the base directories.  Currently `install` is being worked on to ensure that this can be configured via the script* 

`sudo ./lp/install [remote log path] [local log path] [processed log path]` *Specify the paths in the command*

or

`sudo ./lp/install` *Be sure to edit the `lp` file if you do not include the log paths in the command*

##Usage
> lp username hostname ticketnumber

##Features
-Pull down all files with a .log extension in a common directory

-Compress them for quick downloading

-Archive


##TODO
- [] Specify the extension of the files to look for.
- [] Scrape all logs on the server
- [] Pull from multiple servers

