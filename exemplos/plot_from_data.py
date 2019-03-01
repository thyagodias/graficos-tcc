import matplotlib.pyplot as plt
import numpy as np

# Part 1
'''
import csv
x = []
y = []

with open('data_loadbalancer.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label='Load from file!')
'''

x, y = np.loadtxt('data_loadbalancer.csv', delimiter=',', unpack=True)
plt.bar(x,y, label='Load from file!')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Teste de plot \n Subtitulo')
plt.legend()

plt.show()
