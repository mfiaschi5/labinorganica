

from __future__ import print_function
import array
import numpy as np
import matplotlib.pyplot as plt
from specio import specread



n = input("Quanti spettri vuoi plottare? ")
for i in range(int(n)): 
    print(str(i+1)+"°")
    sp_filename = input("/path/to/file -->  ")
print(sp_filename)


spectra = specread(sp_filename)

plt.rcParams["figure.autolayout"] = True
plt.title("Laboratorio di chimica inorganica - FTIR")
plt.xlabel("Numero d'onda $cm^{-1}$")
plt.ylabel("Trasmittanza %")

plt.plot(spectra.wavelength, spectra.amplitudes , label='Cobalto salen')
plt.gca().invert_xaxis()
plt.legend(loc='best')
plt.show()
