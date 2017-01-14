import os
import sys

home = '/Users/noah/scripts/GIT_ER/'
h = open(home + 'watchList.txt')
d = h.read()
h.close()
paths = d.split('\n')

try:
    if sys.argv[1] == 'add':
        z = open(home + 'watchList.txt', 'w')
        z.write(d + sys.argv[2] + '\n')
    elif sys.argv[1] == 'show':
        print d
    elif sys.argv[1] == 'sync':
        for i in paths:
            if not i == '':
                print 'git push ', i
                os.system('cd "' + i + '"; git pull; git push;')
    else:
        print "Supplied argument found no match."
except:
    for i in paths:
        if not i == '':
            print 'git push ', i
            os.system('cd "' + i + '"; git pull; git push;')
