#!/usr/bin/env python
import os, sys

from BeautifulSoup import BeautifulSoup

def parse_svg(file):
    svg = open(file, "r").read()
    soup = BeautifulSoup(svg, selfClosingTags=["defs", "sodipodi:namedview"])
    return soup

if __name__ == "__main__":
    print >> sys.stdout, parse_svg(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../resources/2010UKElectionMap.svg')))
