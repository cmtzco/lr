#!/usr/bin/python
###!/usr/local/bin//python  ##USED FOR MAC ONLY
import click
import subprocess
import sys
import pysftp
import getpass

@click.command()
@click.option('--path', default='/var/log/', help='Path to search remote host for logs. Make sure to end with a /')
@click.option('--local', default='/home/user/', help='Path to store the logs locally.  Make sure to end with a /')
@click.option('--ext', default='log', help='Extension of files to pull down from the remote server')
@click.argument('user')
@click.argument('host')
@click.argument('foldername')

#def download(user, hostname, pathtoremote, pathtolocal, foldername):
#  password = getpass.getpass()
#  with pysftp.Connection(hostname, username=user, password=password) as sftp:
#    sftp.get_d('{}{}.tar.gz'.format(pathtoremote, foldername), pathtolocal, preserve_mtime=True)

def lr(path, local, ext, user, host, foldername):
  """LogRoller allows for organized log downloads"""
  click.echo('\tPath: {}'.format(path))
  click.echo('\tLocal Path: {}'.format(local))
  click.echo('\tExtension: {}'.format(ext))
  click.echo('\tUser: {}'.format(user))
  click.echo('\tHost: {}'.format(host))
  click.echo('\tFolder Name: {}'.format(foldername))
  command = 'cd {} && mkdir {} && cp *.{} {}/ && tar -cvzf {}.tar.gz {}'.format(path, 
                                                                                foldername, 
                                                                                ext, 
                                                                                foldername, 
                                                                                foldername, 
                                                                                foldername)
  click.echo(command)
  ssh = subprocess.Popen(["ssh", "{}@{}".format(user, host), command],
                         shell=False,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
  result = ssh.stdout.readlines()
  if result == []:
    error = ssh.stderr.readlines()
    print >>sys.stderr, "ERROR: %s" % error
  else:
    print result
    pw  = getpass.getpass()
    sftp = pysftp.Connection(host, username=user, password=pw)
    sftp.get('{}{}.tar.gz'.format(path, foldername), localpath='{}{}'.format(local, foldername),  preserve_mtime=True)

if __name__ == '__main__':
  lr()
