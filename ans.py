#num=0
#f=open('all.txt', 'w')
#for year in range(1985,2013):
#    for prob in range(1,26):
#        f.write(str(n).zfill(3)+'.'+str(year)+'.'+str(prob).zfill(2)+'\n')
#        num=num+1
#f.close()

n = ''
d = 0
c = -1
f = open('all.txt', 'r')
a = open('solutions4.htm', 'r')
b = open('allanswers.txt', 'w')
for l in f.readlines():
    n = str(25*(int(l[4:8])-1985)+ int(l[9:12]) - 1).zfill(3)
    a.seek(0)
    for m in a.readlines():
        if m[:6] == 'ProbID':
            d = 0
        if m[:9] == 'ProbID' + n:
            d = 1
        if d == 1:
            if m.find('boxed{\\text{(') != -1: c = m.find('boxed{\\text{(')+13
            elif m.find('boxed{\\text{') != -1: c = m.find('boxed{\\text{')+12
            elif m.find('boxed{\\textbf{(') != -1: c = m.find('boxed{\\textbf{(')+15
            elif m.find('boxed{\\mathrm{(') != -1: c = m.find('boxed{\\mathrm{(')+15
            elif m.find('boxed{\\mathrm{') != -1: c = m.find('boxed{\\mathrm{')+14
            elif m.find('boxed{(') != -1: c = m.find('boxed{(')+7
            elif m.find('boxed{') != -1: c = m.find('boxed{')+6
        if c != -1:
            b.write(l[0:3]+'. '+m[c:c+1]+'\n')
            c = -1
            d = 0


f.close()
a.close()
b.close()

b = open('allanswers.txt', 'r')
e = open('wrong.txt', 'w')
for l in b.readlines():
    if l[5:6] != 'A':
        if l[5:6] != 'B':
            if l[5:6] != 'C':
                if l[5:6] != 'D':
                    if l[5:6] != 'E':
                        e.write(l[0:3]+'\n')
e.close()
b.close()

f=open('C:\\Users\\Mitko\\Desktop\\answers.txt', 'r')
g=open('C:\\Users\\Mitko\\Desktop\\answers2.txt', 'w')
for l in f.readlines():
	if int(l[0:3])>n:
		g.write(l); n=int(l[0:3])
f.close()
g.close()
