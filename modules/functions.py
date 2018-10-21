# Important Functions

import sys

def mand(c,lim):#Manderbrot set
    z=0+0j
    n=1
    while abs(z)<=2 and n<=lim:
        z=z**2+c
        n+=1
        #print(n)
    return n
def zeta(s,lim):
    a=0+0j
    for i in range(lim):
        a+=(i+1)**(s*-1)
        print(a)
    return a


# --- Progress Bar ----------
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + ' ' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()