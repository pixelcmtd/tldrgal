"""A library for dealing with tldr."""

from os import getenv, walk
from subprocess import run, PIPE

def has_tldr(prog: str, head: str) -> bool:
    """Checks, wheather `prog` has a page in `head`. `prog` must not contain special regex characters."""
    return run(f'fd {prog} {head}', stdout=PIPE, check=False, shell=True).stdout.strip() != b''

def get_all_installed_programs() -> set:
    """This has nothing to do with tldr, but it's useful."""
    s = set()
    for path in getenv('PATH').split(':'):
        for _, _, f in walk(path):
            s.update(f)
    return s

def get_all_tldr_pages(head: str) -> set:
    """Gets all tldr pages from `head`."""
    s = set()
    for _, _, f in walk(head):
        s.update([f.replace('.md', '') for f in f])
    return s
