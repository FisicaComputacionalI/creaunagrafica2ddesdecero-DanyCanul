import numpy as np
import pylab as pl 
x=[1,2,3,4]
y=[7.75,9.0,8.5,9.0]
pl.ylabel('PROMEDIO')
pl.xlabel('SEMESTRE')
pl.title('PROMEDIO POR SEMESTRE')
pl.plot(x,y,'mD')
pl.plot(x,y, 'y')
pl.axis([1,4, 7,10])
pl.savefig('temp1.png') 