# Important Functions

import sys
import scipy.special as sp
from scipy import pi

def mand(c,lim,pow=2):#Manderbrot set
    z=0+0j
    n=1
    while abs(z)<=2 and n<=lim:
        z=z**pow+c
        n+=1
        #print(n)
    return n

def zeta_r(s,lim):#only run s>1
    a=0+0j
    for i in range(lim):
        a+=(i+1)**(s*-1)
        #print(a)
    return a

def zeta(s,lim):
    if s>1:
        return zeta_r(s,lim)
    else:
        return zeta_r(1-s,lim)*sp.gamma((1-s)/2)*(pi**(s/2-(1-s)/2))/sp.gamma(s/2)

# --- Progress Bar ----------
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + ' ' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()