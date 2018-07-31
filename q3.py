#! /usr/bin/python3

import re

line = "The ghost that says boo hants the loo"
m = re.findall(".oo",line)
print(m)
