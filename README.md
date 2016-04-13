# LP
###Organized log retrieval

lp is currently used in a helpdesk environment for pulling logs from remote servers and 
organizing them based on the tickets they relate to.  lp makes it simple to pull down logs 
and avoid having to remember the SCP/RSYNC command format.  

##Installation
*NOTE: sudo is required as it installs the script in the /bin folder*
> git clone https://github.com/mrMuffins/lp .
> sudo ./lp/install 

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

