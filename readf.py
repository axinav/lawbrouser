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
    strs=re.search(r'\bСП|ГОСТ|СанПиН', self.soup.title.text, re.M)
        if strs[0]=="СП":
            self.lawtype='SP'
        elif strs[0]=="ГОСТ":
            self.lawtype='GOST'
        elif strs[0]=="СанПиН":
            self.lawtype='SANPIN'
            
            



if __name__ == "__main__":
    html=HtmlParcer("~/coding/lawbrouser/LAW/Urban/Sp18_13330_2011.htm")
    html.check_type()
    print (html.lawtype)
