#!/bin/bash

#define user host and ticket number
user=$1           #DO NOT EDIT
host=$2           #DO NOT EDIT
ticketnumber=$3   #DO NOT EDIT
pathtosearch=$4   #DO NOT EDIT


##############################################################
##                                                          ##
##               BEGIN CONFIGURATION BLOCK                  ##
##      Define the paths that are used in the script        ##
##############################################################


mainlogpath=[/path/to/remote/logs]             #This is the path that the script will search the host for
locallogpath=[/path/to/local/logs]      #Path to the logs on the local machine running the script
processedlogpath=[/path/to/logs]        #Path to move all the zipped up archives to prevent clutter


##############################################################
##                                                          ##
##                 END CONFIGURATION BLOCK                  ##
##                                                          ##
##############################################################



#function to echo the usage message
function HELP {
  echo ""
  echo -e "Usage: lp [user] [host] [ticketnumber]"
  echo ""
  echo -e "\tThis command will allow you to specify"
  echo -e "\ta username, host, and ticket number."
  echo -e "\tThat will create a folder locally and"
  echo -e "\tpull down all the logs from that host"
  exit
}

function SETPATH {
  if [ -z ${1} ]; then
    #define the path to the zipped up logs
    logz="$mainlogpath/$ticketnumber.tar.gz"   # DO NOT CHANGE
    #define the path the the folder where the zipped logs will go 
    logpath=$mainlogpath/$ticketnumber         # DO NOT CHANGE
    LOGPULL
  else
    mainlogpath=$1
    #define the path to the zipped up logs
    logz="$mainlogpath/$ticketnumber.tar.gz"   # DO NOT CHANGE
    #define the path the the folder where the zipped logs will go 
    logpath=$mainlogpath/$ticketnumber         # DO NOT CHANGE
    LOGPULL
  fi
}

function LOGPULL {
  ssh $user@$host << ENDHERE
    cd $mainlogpath
    mkdir $ticketnumber
    cp *.log $ticketnumber/
    tar -cvzf $ticketnumber.tar.gz $ticketnumber
    exit
  ENDHERE  #whitespace matters -__-

  #scp pulls down the archive locally then tar extracts the files
  scp $user@$host:$logz $locallogpath
  tar -xzvf $locallogpath/$ticketnumber.tar.gz -C $locallogpath
  #find $locallogpath/$ticketnumber -type f -print0 | xargs -0r gzip  ##MAY BE USED WHEN LOGSTASH ALLOWS gzipped logs not coming from file beat

  #compressed archives get moved to a processed
  #folder after logs are extracted
  mv $locallogpath/*.tar.gz $processedlogpath
}
# Check that all three parameteres have been passed in. 
if [ ! $# -ge 3 ]; then
  HELP
fi

if [ -z ${pathtosearch} ]; then 
  SETPATH
else
  SETPATH $pathtosearch
fi