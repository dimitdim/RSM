import shutil
import os
import time
import datetime
import math
import urllib
from array import array
import timeit

start = timeit.timeit()

#for year in range(1999, 2013):
#    f = open('tests/' + str(year) + '.htm', 'w')
#    f.close()
tr = 1
f = open('new' + str(tr) + '.htm', 'w')
f.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Problems</title>\n</head>\n<body>\n')
f.close

year = 1985
while year < 2013:
    
    p = []
    a = []
    n = -1
    c = 0
    b = ''
    if year < 1999:
        f = urllib.urlopen('http://www.artofproblemsolving.com/Wiki/index.php?title=' + str(year) + '_AJHSME_Problems&printable=yes')
    else:
        f = urllib.urlopen('http://www.artofproblemsolving.com/Wiki/index.php?title=' + str(year) + '_AMC_8_Problems&printable=yes')
        
    for l in f.readlines():
        if c == 1:
            if l[:13] == '</p><p><br />':
                c = 1
            elif l[:12] == '</p><p><a hr':
                cl = l.find('class')
                if l[:18] == '</p><p><a href="/W':
                    c = 0
                if l[cl+7:cl+13] == 'latexc':
                    p[n]=p[n]+'</p><p>' + str(l[l.find('<img'):l.find(' alt')]) + str('>') + '\n'
                if l[cl+7:cl+13] == 'latex"':
                    c1 = 1 + l.find('"')
                    c2 = l.find('" cla')
                    a[n]=l[c1:c2]
            elif l[:12] == '<p><a href="':
                cl = l.find('class')
                if l[:14] == '<p><a href="/W':
                    c = 0
                if l[cl+7:cl+13] == 'latexc':
                    p[n]=p[n]+'</p><p>' + str(l[l.find('<img'):l.find(' alt')]) + str('>') + '\n'
                if l[cl+7:cl+13] == 'latex"':
                    c1 = 1 + l.find('"')
                    c2 = l.find('" cla')
                    a[n]=l[c1:c2]
            else:
                p[n]=p[n]+str(l)
        if l[5:43] == '<span class="mw-headline" id="Problem_':
            c = 1
            p.append('')
            a.append('')
            n = n + 1
    f.close()
    
#    n = 0
#    for l in p:
#        n = n+1
#        print n
#        print '::::'
#        print l
#    print '====ANS===='
#    n = 0
#    for l in a:
#        n = n+1
#        print n
#        print '::::'
#        print l
    
    c = 0
    n = 0
    c2 = 0
    u = 'test'
    for l in p:
        n = n+1
        while n < 26:
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
                p[c] = l[:c1] + u + l[c2:]
                l = p[c]
            else:
                break
        c2 = l.rfind('\n')
        p[c] = 'ProbID' + str(25*(year-1985)+c).zfill(3) +'<p>' + l[3:c2] + ' (' + str(year) + '.' + str(c+1) + ')</p>\n'
        c = c+1
        
#    n = 0
#    for l in p:
#        n = n+1
#        print n
#        print '::::'
#        print l


    u = 'test'
    c = 0
    for l in a:
        if l != '':
            latex = urllib.urlopen(l)
            for line in latex.readlines():
                if line[2:8] == '<code>':
                    u = line
                    u = u.replace("\t\t<code>$ \\textbf{(A)}\\hspace{.05in}", '<p>(A) <span class="tex">$ ')
                    u = u.replace('\\qquad\\textbf{(B)}\\hspace{.05in}', ' $</span> (B) <span class="tex">$ ')
                    u = u.replace('\\qquad\\textbf{(C)}\\hspace{.05in}', ' $</span> (C) <span class="tex">$ ')
                    u = u.replace('\\qquad\\textbf{(D)}\\hspace{.05in}', ' $</span> (D) <span class="tex">$ ')
                    u = u.replace('\\qquad\\textbf{(E)}\\hspace{.05in}', ' $</span> (E) <span class="tex">$ ')
                    u = u.replace("\t\t<code>$ \\textbf{(A)}\\ ", '<p>(A) <span class="tex">$ ')
                    u = u.replace('\\qquad\\textbf{(B)}\\ ', ' $</span> (B) <span class="tex">$ ')
                    u = u.replace('\\qquad\\textbf{(C)}\\ ', ' $</span> (C) <span class="tex">$ ')
                    u = u.replace('\\qquad\\textbf{(D)}\\ ', ' $</span> (D) <span class="tex">$ ')
                    u = u.replace('\\qquad\\textbf{(E)}\\ ', ' $</span> (E) <span class="tex">$ ')
                    u = u.replace("\t\t<code>$ \\textbf{(A) }", '<p>(A) <span class="tex">$ ')
                    u = u.replace('\\qquad\\textbf{(B) }', ' $</span> (B) <span class="tex">$ ')
                    u = u.replace('\\qquad\\textbf{(C) }', ' $</span> (C) <span class="tex">$ ')
                    u = u.replace('\\qquad\\textbf{(D) }', ' $</span> (D) <span class="tex">$ ')
                    u = u.replace('\\qquad\\textbf{(E) }', ' $</span> (E) <span class="tex">$ ')
                    u = u.replace("\t\t<code>$ \\textbf{(A)}", '<p>(A) <span class="tex">$ ')
                    u = u.replace('\\qquad\\textbf{(B)}', ' $</span> (B) <span class="tex">$ ')
                    u = u.replace('\\qquad\\textbf{(C)}', ' $</span> (C) <span class="tex">$ ')
                    u = u.replace('\\qquad\\textbf{(D)}', ' $</span> (D) <span class="tex">$ ')
                    u = u.replace('\\qquad\\textbf{(E)}', ' $</span> (E) <span class="tex">$ ')
                    u = u.replace("\t\t<code>$ \\mathrm{(A)}\\ ", '<p>(A) <span class="tex">$ ')
                    u = u.replace('\\qquad\\mathrm{(B)}\\ ', ' $</span> (B) <span class="tex">$ ')
                    u = u.replace('\\qquad\\mathrm{(C)}\\ ', ' $</span> (C) <span class="tex">$ ')
                    u = u.replace('\\qquad\\mathrm{(D)}\\ ', ' $</span> (D) <span class="tex">$ ')
                    u = u.replace('\\qquad\\mathrm{(E)}\\ ', ' $</span> (E) <span class="tex">$ ')
                    u = u.replace("\t\t<code>$ \\text{(A)}\\ ", '<p>(A) <span class="tex">$ ')
                    u = u.replace('\\qquad\\text{(B)}\\ ', ' $</span> (B) <span class="tex">$ ')
                    u = u.replace('\\qquad\\text{(C)}\\ ', ' $</span> (C) <span class="tex">$ ')
                    u = u.replace('\\qquad\\text{(D)}\\ ', ' $</span> (D) <span class="tex">$ ')
                    u = u.replace('\\qquad\\text{(E)}\\ ', ' $</span> (E) <span class="tex">$ ')
                    u = u.replace("\t\t<code>$ \\text{(A)}\\", '<p>(A) <span class="tex">$ ')
                    u = u.replace('\\qquad\\text{(B)}\\', ' $</span> (B) <span class="tex">$ ')
                    u = u.replace('\\qquad\\text{(C)}\\', ' $</span> (C) <span class="tex">$ ')
                    u = u.replace('\\qquad\\text{(D)}\\', ' $</span> (D) <span class="tex">$ ')
                    u = u.replace('\\qquad\\text{(E)}\\', ' $</span> (E) <span class="tex">$ ')
                    if u.find('</code>') == -1: u = u + '</code>'
                    if u.find('<code>') == -1: u = u.replace('</code>', '</span></p>')
            latex.close()
            a[c] = u
        c = c + 1
    
#    f = open('tests/' + str(year) + '.htm', 'a')
    f = open('new' + str(tr) + '.htm', 'a')
#    f.write('<!DOCTYPE html>\n<html>\n<head>\n<title>' + str(year) + '</title>\n</head>\n<body>\n')
    for l in range(len(p)):
        f.write(p[l])
        f.write(a[l])
        f.write('\n')
    f.close()
    print(str(year))
    year = year + 1

f = open('new' + str(tr) + '.htm', 'a')
f.write('ProbID</body></html>')
f.close()

end = timeit.timeit()
time = end-start
print time
