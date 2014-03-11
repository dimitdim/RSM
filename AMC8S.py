import shutil
import os
import time
import datetime
import math
import urllib
from array import array
import timeit

start = timeit.timeit()

c = 0
n = -1
s = []
for year in range(1985, 2013):
    for problem in range(1, 26):
        if year < 1999:
            f = urllib.urlopen('http://www.artofproblemsolving.com/Wiki/index.php?title='+str(year)+'_AJHSME_Problems/Problem_'+str(problem)+'&printable=yes')
        else:
            f = urllib.urlopen('http://www.artofproblemsolving.com/Wiki/index.php?title='+str(year)+'_AMC_8_Problems/Problem_'+str(problem)+'&printable=yes')
        for l in f.readlines():
            if l[:38] == '<h2> <span class="mw-headline" id="See':
                c = 0
            if c == 1:
                s[n] = s[n] + l
            if l[:38] == '<h2> <span class="mw-headline" id="Sol':
                c = 1
                n = n + 1
                s.append('ProbID'+str(25*(year-1985)+problem-1).zfill(3))
    print year

c1 = 0
c2 = 0
n = 0
u = ''
for l in s:
    while 0 == 0:
        c1 = l.find('<a')
        c2 = 4 + l.find('</a>')
        if l[c1:c1+11]== '<a href="/W':
            break
        if c1 > -1:
            latex = urllib.urlopen(str(l[(c1+9):(c1+104)]))
            for line in latex.readlines():
                if line[2:8] == '<code>':
                    u = line.replace('\t\t<code>', '<span class="tex">')
                    u = u.replace('</code>\n', '</span>')
            latex.close()
            s[n] = l[:c1] + u + l[c2:]
            l = s[n]
        else:
            break
    n = n + 1

f = open('solutions.htm', 'w')
f.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Solutions</title>\n</head>\n<body>\n')
for l in range(len(s)):
        f.write(s[l])
        f.write('\n')
f.write('ProbID</body></html>')
f.close()

end = timeit.timeit()
time = end-start
print time
