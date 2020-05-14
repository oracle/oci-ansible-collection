"""Entry point for command line usage with `github <command>`"""

import click
from . import copy_repository
from . import fetch_specs


@click.group()
def cli():
    pass


@cli.command(name="copy")
@click.argument('SRCDIR')
@click.argument('DESTDIR')
@click.option('--dry-run', help='List files without copying',
              type=bool, default=True, show_default=True)
def copy(srcdir, destdir, dry_run):
    if dry_run:
        print("------- TEST MODE -------")
    else:
        print("!!!!!!! COPYING !!!!!!!")
    copy_repository.copy(srcdir, destdir, dry_run)


@cli.command(name="get-specs")
@click.argument('SRCDIR')
@click.argument('DESTDIR')
def get_specs(srcdir, destdir):
    fetch_specs.fetch(srcdir, destdir)
