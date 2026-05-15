#!/usr/bin/env python3

import sys

# Author: Prince Asamoah Arkoh
# Author ID: aparkoh@myseneca.ca
# Date Created: 2026/05/16

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer != 0:
    print(timer)
    timer = timer - 1

print("blast off!")
