import os
import time
import datetime
import math
import urllib
from array import array

d = 0
d2 = 0
n = 0
r = 'C'
a = open('problems5.htm', 'r')
a2 = open('solutions4.htm', 'r')
b = open('cue.txt', 'r')
c = open('out/blank.htm', 'w')
c2 = open('out/blank2.htm', 'w')
for l in b.readlines():
    n = n + 1
    if l[:1] == '@':
        c.write('</body></html>')
        c2.write('</body></html>')
        c.close()
        c2.close()
        c = open('out/' + l[1:l.rfind('\n')] + '.htm', 'w')
        c2 = open('out/' + l[1:l.rfind('\n')] + '_SOL.htm', 'w')
        c.write('<!DOCTYPE html>\n<html>\n<head>\n<title>' + l[1:l.rfind('\n')] + '</title>\n</head>\n<body>\n')
        c2.write('<!DOCTYPE html>\n<html>\n<head>\n<title>' + l[1:l.rfind('\n')] + '</title>\n</head>\n<body>\n')
        n = 0
    else:
        a.seek(0)
        a2.seek(0)
        for m in a.readlines():
            if m[:6] == 'ProbID':
                d = 0
            if m[:9] == 'ProbID' + str(l[:3]):
                d = 1
            if d == 2:
                if m.rfind(')</p>') > -1:
                    if l[3:4] == str(0): r = ' A'
                    if l[3:4] == str(1): r = ' AB'
                    if l[3:4] == str(2): r = ' B'
                    if l[3:4] == str(3): r = ''
                    m = m[:m.rfind(')</p>')] + ' ' + r + m[m.rfind(')</p>'):]
                c.write(m)
            if d == 1:
                if m.rfind(')</p>') > -1:
                    if l[3:4] == str(0): r = 'A'
                    if l[3:4] == str(1): r = 'AB'
                    if l[3:4] == str(2): r = 'B'
                    m = m[:m.rfind(')</p>')] + r + m[m.rfind(')</p>'):]
                c.write('<p>' + str(n) + '. ' + m[12:])
                d = 2
        for m in a2.readlines():
            if m[:6] == 'ProbID':
                d2 = 0
            if m[:9] == 'ProbID' + str(l[:3]):
                d2 = 1
            if d2 == 2:
                c2.write(m)
            if d2 == 1:
                c2.write('<p>' + str(n) + '. ' + m[12:])
                d2 = 2
