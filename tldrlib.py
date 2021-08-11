"""A library for dealing with tldr."""

from os import getenv, walk
from subprocess import run, PIPE

TLDR_HEAD = getenv('HOME') + '/.tldrc/tldr-master/pages'

def has_tldr(prog: str) -> bool:
    """Checks, wheather `prog` has a tldr page. `prog` must not contain special regex characters."""
    return run(f'fd {prog} {TLDR_HEAD}', stdout=PIPE, check=False, shell=True).stdout.strip() != b''

def get_all_installed_programs() -> set:
    """This has nothing to do with tldr, but it's useful."""
    s = set()
    for path in getenv('PATH').split(':'):
        for _, _, f in walk(path):
            s.update(f)
    return s

def get_all_tldr_pages() -> set:
    """Gets all tldr pages from TLDR_HEAD."""
    s = set()
    for _, _, f in walk(TLDR_HEAD):
        s.update([f.replace('.md', '') for f in f])
    return s
