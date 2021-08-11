#!/usr/bin/env python3
from tldrlib import *

for p in get_all_installed_programs() - get_all_tldr_pages():
    if not '.' in p:
        print(p)
