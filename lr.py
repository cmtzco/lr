!/usr/bin/python
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

def lr(path, local, ext, user, host, foldername):
    """LogRoller allows for organized log downloads"""
    click.echo('\tPath: {}'.format(path))
    click.echo('\tLocal Path: {}'.format(local))
    click.echo('\tExtension: {}'.format(ext))
    click.echo('\tUser: {}'.format(user))
    click.echo('\tHost: {}'.format(host))
    click.echo('\tFolder Name: {}'.format(foldername))
    command = 'cd {0} && mkdir {1} && cp *.{2} {1}/ && tar -cvzf {1}.tar.gz {1}'.format(path,
                                                                                        foldername,
                                                                                        ext)
    click.echo(command)
    ssh = subprocess.Popen(["ssh", "{}@{}".format(user, host), command],
                           shell=False,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()
    if result == []:
        error = ssh.stderr.readlines()
        print >>sys.stderr, "ERROR: {}".format(error)
    else:
        print result
        pw  = getpass.getpass()
        sftp = pysftp.Connection(host, username=user, password=pw)
        sftp.get('{}{}.tar.gz'.format(path, foldername), localpath='{}{}'.format(local, foldername),  preserve_mtime=True)

if __name__ == '__main__':
    lr()

