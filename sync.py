import os

home = '/Users/noah/scripts/GIT_ER/'
h = open(home + 'watchList.txt')
d = h.read()
paths = d.split('\n')

for i in paths:
    if not i == '':
        print 'git push ', i
        os.system('cd "' + i + '"; git push;')
