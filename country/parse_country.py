# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import re
from bs4 import BeautifulSoup

# http://www.resgain.net/country.html

with open("raw_country.txt", "r") as fs:
    page = fs.read()

soup = BeautifulSoup(page, "html5lib")
tbody = soup.find("tbody")


trs = tbody.find_all("tr")

all_nation = []

for tr in trs:
    tds = tr.find_all("td")
    all_nation.append(tds[2].text)


open("all_nation.txt", "w+").write("\n".join(all_nation))

