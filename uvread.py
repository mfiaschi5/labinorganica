import numpy as np
import matplotlib.pyplot as plt 

n = input("Quanti spettri vuoi plottare? ")
filename = []
namefile = []
for i in range(int(n)):
    name = input("Nome del composto formato Latex --> " )
    file = input("/path/to/file/ --> " )
    filename.append(file)
    namefile.append(name)


for i in range(len(filename)):
    x_data,y_data = np.loadtxt(filename[i], unpack=True,skiprows=18)
    plt.rcParams["figure.autolayout"] = True
    plt.title("Laboratorio di chimica inorganica - UV-VIS")
    plt.xlabel("Lunghezza d'onda(nm)")
    plt.ylabel("Assorbanza")
    plt.plot(x_data, y_data, label=namefile[i])
    plt.legend(loc='best')
    plt.show()


plt.rcParams["figure.autolayout"] = True
plt.title("Laboratorio di chimica inorganica - UV-VIS")
plt.xlabel("Lunghezza d'onda(nm)")
plt.ylabel("Assorbanza")
for i in range(len(filename)):
    x_data,y_data = np.loadtxt(filename[i], unpack=True,skiprows=18)
    plt.plot(x_data, y_data, label=namefile[i])
plt.legend(loc='best')
plt.show()