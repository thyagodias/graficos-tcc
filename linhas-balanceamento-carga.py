#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import lines
import random
import pylab


x, y = np.loadtxt('data_loadbalancer.csv', delimiter=',', unpack=True)
#plt.bar(x,y, label='Load from file!')


x2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
#x2 = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']


years = list(range(1,31))
plt.xticks(years,[str(i) for i in years],rotation=45) # Usa isto para definires as tuas labels


#plt.plot(x, y, label='First Line')
plt.plot(x2, x, 'bo')
plt.plot(x2, x, label='Com sobrecarga', color='blue')

plt.plot(x2, y, 'ro')
plt.plot(x2, y, label='Sem sobrecarga', color='red')

plt.xlabel('Numero da Simulacao')
plt.ylabel('Tempo de Carregamento da Pagina em Milessegundos')
plt.ylim(0, 600)
#plt.xlim(0,30)
plt.xlim([1,30])
plt.title('SDN com Balanceamento de Carga')
plt.legend()
plt.grid(True)
plt.rcParams['figure.figsize'] = (20,7)
plt.savefig('nome_da_imagem.svg')

plt.show()
