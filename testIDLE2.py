#  eseguibile su IDLE
import numpy as np
import matplotlib.pyplot as pl
#
#X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
X = np.linspace(-100, 100, 1000, endpoint=True)
#
C= 10*np.cos(X)
S= 10*np.sin(X)
R=np.sqrt((X*X+2)/(X*X-2))
RE=(1/X)
AB= np.abs(X)

#creo una figura di 8x6 pollici con risoluzione di 80 punti/pollice
pl.figure(figsize=(8,6),dpi=72)
# creo un unico sistema di assi cartesiani nella figura
pl.subplot(1, 1, 1) #(1riga,1colonna,grafico1)
# Plot cosine with a blue continuous line of width 1 (pixels)
pl.plot(X, C, color="blue", linewidth=1.0, linestyle="-")
# Plot sine with a green continuous line of width 1 (pixels)
pl.plot(X, S, color="green", linewidth=1.0, linestyle="-")
# Set x limits
pl.xlim(-100.0, 100.0)
# Set x ticks
pl.ylim(-10.0, 100.0)
# Set y ticks
#pl.yticks(np.linspace(-1, 1, 5, endpoint=True))

#pl.xticks(np.linspace(-4, 4, 9, endpoint=True))
# Set y limits
#print(X)
#pl.plot(X, C)
#pl.plot(X, S)
#pl.plot(X, R)
pl.plot(X,AB)
#pl.plot(X,RE)
#pl.savefig("./img/matplotlib00.png", dpi=72)
pl.show()
