#!/usr/bin/env python

import sys
from BeautifulSoup import BeautifulSoup
from parse_svg import parse_svg
from id_map import ID_MAP

def prepare(filename):
    fp=open(filename)
    data = [row.strip().split("\t") for row in fp.readlines()]
    fp.close()
    return dict([(int(key), int(val)) for key, val in data[1:]])

def assign_colors(filename, colors):
    data = prepare(filename)
    maximum = max(data.values())
    step = maximum/float(len(colors))
    steps = [step * i for i in range(0, len(colors))]
    # Assign color to each step
    steps.reverse()
    colors.reverse()
    assigned_colors = dict()
    for id in data:
        for idx in range(0, len(steps)):
            if data[id] >= steps[idx]:
                assigned_colors[id] = (colors[idx], data[id])
                break
    
    return assigned_colors

def colorize(filename, colors, id_map=ID_MAP, svg="2010UKElectionMap.svg"):
    soup = parse_svg(svg)
    paths = soup.findAll("path")
    colors = assign_colors(filename, colors)
    id_map = dict(zip(id_map.values(), id_map.keys()))
    # path_style = """font-size:12px;fill-rule:nonzero;stroke:#000000;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:0;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:"""
    path_style = "stroke:#fff;stroke-width:0.1;fill:"
    for path in paths:
        try:
            svg_id = path["id"]
            sys.stderr.write(svg_id + ":" + id_map[svg_id] + "\n")
            path["style"] = path_style + colors[int(id_map[svg_id])][0]
        except:
            path["style"] = path_style + "#ffffff"
    
    return soup.prettify()

if __name__ == "__main__":
    print colorize("data.txt", colors=["#EFF3FF", "#C6DBEF", "#9ECAE1", "#6BAED6", "#4292C6", "#2171B5", "#084594"])
