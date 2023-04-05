#!/usr/bin/python3
import sys
import requests
from lxml import html
import re

states = [
    ('421a55f4-7d82-47d9-b51c-a76916479545', 'stateA', [
            ('521a55f4-7d82-47d9-b51c-a76916479545', 'cityAA'),
            ('521a55f4-7d82-47d9-b51c-a76916479546', 'cityAB')
    ]),
    ('421a55f4-7d82-47d9-b51c-a76916479546', 'stateB', [
            ('511a55f4-7d82-47d9-b51c-a76916479546', 'cityBA'),
            ('511a55f4-7d82-47d9-b51c-a76916479547', 'cityBB')
    ]),
    ('421a55f4-7d82-47d9-b52c-a76916479547', 'stateC', [
            ('521a55f4-7d82-47d9-b52c-a76916479547', 'cityCA'),
            ('521a55f4-7d82-47d9-b52c-a76916479548', 'cityCB')
    ]),
    ('421a55f4-7d82-47d9-b53c-a76916479548', 'stateD', [
            ('531a55f4-7d82-47d9-b53c-a76916479548', 'cityDA'),
            ('531a55f4-7d82-47d9-b53c-a76916479549', 'cityDB')
    ]),
    ('421a55f4-7d82-47d9-b57c-a76916479549', 'stateE', [
            ('511a55f4-7d82-47d9-b57c-a76916479549', 'cityEA'),
            ('511a55f4-7d82-47d9-b57c-a76916479539', 'cityEB')
    ])
]

NO_PROXY = {
    'no': 'pass',
}


## Request
page = requests.get('http://localhost:5000/cities_by_states', proxies=NO_PROXY)
if int(page.status_code) != 200:
    print("Status fail: {}".format(page.status_code))
    sys.exit(1)

## Parsing
print(page.content)
tree = html.fromstring(page.content)
if tree is None:
    print("Can't parse page")
    sys.exit(1)

## H1
h1_tags = tree.xpath('//body/h1/text()')
if h1_tags is None or len(h1_tags) == 0:
    print("H1 tag not found")
    sys.exit(1)

if not re.search(r".*States.*", h1_tags[0]):
    print("Title `States` doesn't found")
    sys.exit(1)

## LI state ID
li_tags = list(filter(None, [x.replace(" ", "").strip(" ").strip("\n").strip("\t") for x in tree.xpath('//body/ul/li/text()')]))
pyprint(li_tags)

if li_tags is None or len(li_tags) != 5:
    print("Doesn't find 5 LI tags (found {})".format(len(li_tags)))
    sys.exit(1)

for li_tag in li_tags:
    is_found = False
    for state_tuple in states:
        is_found = re.search(r".*{}.*".format(state_tuple[0]), li_tag)
        if is_found:
            break
    if not is_found:
        print("{} not found".format(li_tag))
        sys.exit(1)
            
## LI state name sorted
li_tags_b = list(filter(None, [x.replace(" ", "").strip(" ").strip("\n").strip("\t") for x in tree.xpath('//body/ul/li/b/text()')]))
if li_tags_b is None or len(li_tags_b) != 5:
    print("Doesn't find 5 LI tags with B tag (found {})".format(len(li_tags_b)))
    sys.exit(1)

idx = 0
for li_tag in li_tags_b:
    if not re.search(r".*{}.*".format(states[idx][1]), li_tag):
        print("{} not found or not sorted".format(li_tag))
        sys.exit(1)
    idx += 1


## LI city ID
li_tags_el = tree.xpath('//body/ul/li')
if li_tags_el is None or len(li_tags_el) != 5:
    print("Doesn't find 5 LI tags (found {})".format(len(li_tags_el)))
    sys.exit(1)

state_idx = 0
for li_tag_el in li_tags_el:
    state_name = li_tag_el.xpath("text()")[0]
    cities = states[state_idx][2]
    cities_li_tags = list(filter(None, [x.replace(" ", "").strip(" ").strip("\n").strip("\t") for x in li_tag_el.xpath('ul/li/text()')]))
    if cities_li_tags is None or len(cities_li_tags) != 2:
        print("Doesn't find 2 LI tags (found {}) for state {}".format(len(cities_li_tags), state_name))
        sys.exit(1)

    for cities_li_tag in cities_li_tags:
        is_found = False
        for city_tuple in cities:
            is_found = re.search(r".*{}.*".format(city_tuple[0]), cities_li_tag)
            if is_found:
                break
        if not is_found:
            print("{} not found".format(cities_li_tag))
            sys.exit(1)
    
            
    ## LI city name sorted
    cities_li_tags_b = list(filter(None, [x.replace(" ", "").strip(" ").strip("\n").strip("\t") for x in li_tag_el.xpath('ul/li/b/text()')]))
    if cities_li_tags_b is None or len(cities_li_tags_b) != 2:
        print("Doesn't find 2 LI tags with B tag (found {}) for state {}".format(len(cities_li_tags_b), state_name))
        sys.exit(1)

    city_idx = 0
    for cities_li_tag_b in cities_li_tags_b:
        if not re.search(r".*{}.*".format(cities[city_idx][1]), cities_li_tag_b):
            print("{} not found or not sorted".format(cities_li_tag_b))
            sys.exit(1)
        city_idx += 1

    state_idx += 1

print("OK", end="")
