#!/usr/bin/env python3
from bs4 import BeautifulSoup as bs
import re
def read_html(fstr):
    """TODO: Docstring for read_html.

    :fstr: TODO
    :returns: TODO

    """
    with open(fstr, "r") as f:
        contents=f.read()
    return contents

class HtmlParcer(object):
    """docstring for HtmlParcer"""
    def __init__(self, filestr):
        super(HtmlParcer, self).__init__()
        self.content =read_html( filestr)
        self.soup=bs(self.content, 'lxml')

    def check_type(self):
        sp=re.search(r'СП \d*', self.soup.title.text, re.M|re.I)
        if sp:
            self.lawtype='SP'


