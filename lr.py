#!/usr/local/bin//python
import click
import subprocess
import sys

@click.command()
@click.option('--path', default='/var/log/', help='Path to search remote host for logs')
@click.option('--local', default='/home/user', help='Path to store the logs locally')
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
  ssh = subprocess.Popen(["ssh", "{}\@{}".format(user, host), COMMAND],
                         shell=False,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
if __name__ == '__main__':
  lr()
