#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#/*
#*    Copyright (C) 2019 Jimmy Olano (http://www.ks7000.net.ve/)
#*
#*    This program is free software: you can redistribute it and/or modify
#*    it under the terms of the GNU General Public License as published by
#*    the Free Software Foundation, either version 3 of the License, or
#*    https://www.gnu.org/licenses/gpl-3.0.en.html any later version.
#*    This program is distributed in the hope that it will be useful,
#*    but WITHOUT ANY WARRANTY; without even the implied warranty of
#*    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#*    GNU General Public License for more details.
#*
#*    You should have received a copy of the GNU General Public License
#*    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#*
#*    Special thanks to Kenneth Reitz for created "Requests" <http for humans>
#*    https://requests.kennethreitz.org/en/master/dev/authors/
#*/

import requests
from bs4 import BeautifulSoup
import gettext
gettext.bindtextdomain('WikipediaUserEditsCounter', '/docs/i18n')
gettext.textdomain('WikipediaUserEditsCounter')
_ = gettext.gettext

user = "Jimmy_Olano"
url = "https://xtools.wmflabs.org/ec/en.wikipedia.org/"+user
my_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

try:
  page = requests.get(url, headers=my_headers)
  if page.status_code == "200":
    wiki_soup = BeautifulSoup(page.text, 'html.parser')
    count_edits = wiki_soup.find_all(class_="xt-test--total-edits")[0].get_text()
    print(_("User "+user+" has "+count_edits+" editions."))
except:
  print(_("No connection with wmflabs!"));


