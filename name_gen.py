#!/usr/bin/python3
import urllib.request
import json
import itertools

with urllib.request.urlopen("https://api.census.gov/data/2010/surname?get=NAME&RANK=1:1000000") as url:
    census = json.loads(url.read().decode())
    surnames = set()
    [surnames.add(datum[0]) for datum in census]

with urllib.request.urlopen("https://github.com/rossgoodwin/american-names/raw/master/firstnames_m.json") as url:
    names = json.loads(url.read().decode())
    first_names = set(names)

with open("all_names.txt", 'w+') as f:
    for first_name, last_name in itertools.product(first_names, surnames):
        name = f'{first_name} {last_name}\n' #names[0] + " " + names[1]
        f.write(name)
    f.close()



