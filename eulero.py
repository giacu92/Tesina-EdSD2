import time
import sys

def eulero(t0, tmax, n, y0, f):

    h = (tmax-t0)/n
    #m = len(y0)
    m=1
    a = 1
    t=t0
    y=y0
    T=[t0]
    Y=[y0]
    toolbar_width = 40

    sys.stdout.write("[%s]" % (" " * (toolbar_width)))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1))
    for j in xrange(toolbar_width):
        #time.sleep(0.1)

        #code here
        for i in xrange(1,n):
            #for j in xrange(1,m):
            k = eval(f)
        
            y=y+k*h
            t=t+h
            T.append(t)
            Y.append(y)

            if i*41 / n >= m:
                sys.stdout.write("#")
                sys.stdout.write("%s" % (" " * (toolbar_width-m)))
                a = 100*m/40
                sys.stdout.write("]" + str(a) + "%")
                if a < 10:
                    sys.stdout.write("\b" * (toolbar_width-m+3))
                else:
                    sys.stdout.write("\b" * (toolbar_width-m+4))
                sys.stdout.flush()
                m = m+1
   
        T.append(tmax)
        sys.stdout.write("\n")

        return (T,Y)
    

"""
Qui risolvo l'equazione differenziale della forma:
  -
 |  y'(t) = f(y(t),t)
< 
 |  y(t0) = t0
  -
"""

print 'intel i3 benchmark: risoluzione di una equazione differenziale lineare con Eulero a 1e6 iterazioni'

t0 = 0.0
tmax = 1.0
n = 1000000
y0 = 1
f = '-y**2.0'

prevMil=time.time()
T,Y = eulero(t0,tmax,n,y0,f)
curMil=time.time()

print 'err = ' + str(Y[n-1]-0.5)

print 'time elapsed: ' + str(curMil-prevMil) + ' sec'

