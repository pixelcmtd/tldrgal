#!/usr/bin/env python3

from os import getenv, walk
from subprocess import run, PIPE

def has_tldr(p):
    return run(f'fd {p} ~/.tldrc/tldr-master/pages', stdout=PIPE, check=False, shell=True).stdout.strip() != b''

for path in getenv("PATH").split(":"):
    for _, _, f in walk(path):
        for p in f:
            if '.' not in p and not has_tldr(p):
                print(p)
