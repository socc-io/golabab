#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 becxer <becxer87@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
import sys
import json

if len(sys.argv) < 3:
    print "usage html_parser.py <html-file> <out-file>"
    exit()

filename = sys.argv[1]
outfilename =sys.argv[2]
print filename
content = open(filename).read()
ttag_1='<h1 id="bo_v_title" class="view-subject">'
ttag_2='</h1>'

ptag_1 = '<div class="view-tag">'
ptag_2 = '/<div>'

dtag_1='rel="tag">'
dtag_2='</a>'

'''
{
    [
        {
            title : 음식이름1,
            tags : [짠맛, 짭조름 등등]
        }
        ,
        {
            title : 음식이름2,
            tags : [짠맛, 짭조름 등등]
        }
    ]
}
'''

title = content.split(ttag_1)[1].split(ttag_2)[0].strip()
print title

tags = map(lambda x : x.split(dtag_2)[0] ,\
        content.split(ptag_1)[1].split(dtag_1))
tags.pop(0)
for t in tags:
    print t

json_file = "{ title:"+title+", tags:["
for t in tags:
    json_file+=t+","

json_file = json_file[:-1] + "] }"
test = json.dumps(json_file, ensure_ascii=False)
print test


#
# TODO: outfile에 제이슨 객체 쓰기
# 
