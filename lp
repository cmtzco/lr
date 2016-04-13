#!/bin/bash

# Check that all three parameteres have been passed in. 
if [ ! $# == 3 ]; then
  echo ""
  echo -e "Usage: lp [user] [host] [ticketnumber]"
  echo ""
  echo -e "\tThis command will allow you to specify"
  echo -e "\ta username, host, and ticket number."
  echo -e "\tThat will create a folder locally and"
  echo -e "\tpull down all the logs from that host"
  exit
fi


#define user host and ticket number
user=$1
host=$2
ticketnumber=$3

#define the path that is used to find the logs on the hosts
mainlogpath=/path/to/logs # this is the path that the script will search the host for
locallogpath=/path/to/local/logs #path to the logs on the local machine running the script
processedlogpath=/path/to/logs  #path to move all the zipped up archives to prevent clutter
#define the path to the zipped up logs
logz="$mainlogpath/$ticketnumber.tar.gz" # DO NOT CHANGE
#define the path the the folder where the zipped logs will go 
logpath=$mainlogpath/$ticketnumber # DO NOT CHANGE

##############################################################
## ssh into the host with specified user and stdin           #
## with the commands I will be running on the remote host    #
## this includes changing directory to the main log path     #
## creating the path for the specified ticket number         #
## as well as copying all the .log files into the folder     #
## that was just created.   After all of that is completed   #
## an archive is created to make it easy to scp down         #
##############################################################
ssh $user@$host << ENDHERE
  cd $mainlogpath
  mkdir $ticketnumber
  cp *.log $ticketnumber/
  tar -cvzf $ticketnumber.tar.gz $ticketnumber
  exit
ENDHERE

#scp pulls down the archive locally then tar extracts the files
scp $user@$host:$logz $locallogpath
tar -xzvf $locallogpath/$ticketnumber.tar.gz -C $locallogpath
#find $locallogpath/$ticketnumber -type f -print0 | xargs -0r gzip  ##MAY BE USED WHEN LOGSTASH ALLOWS gzipped logs not coming from file beat

#compressed archives get moved to a processed
#folder after logs are extracted
mv $locallogpath/*.tar.gz $processedlogpath
debugstash
