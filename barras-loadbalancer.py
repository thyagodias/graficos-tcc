import matplotlib.pyplot as plt

import csv


# Balanceamento de carga
sdn = [134.5, 99.5]
sdnErro = []
x = ['Com Sobrecarga', 'Sem Sobrecarga']

naoSDN = [281.5, 88]
naoSdnErro = [0.23, 0.57]
x2 = ['Com Sobrecarga', 'Sem Sobrecarga']

sdnComSobrecarga = [134.5]
s = ['Com Sobrecarga']

sdnSemSobrecarga = [99.5]
d = ['Sem Sobrecarga']

'''
with open('data_loadbalancer.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.bar(x,y, label='Load from file!')
'''

# Primeiro Gráfico
plt.bar(s, sdnComSobrecarga, label='Balanceamento de Carga com Sobrecarga')
plt.bar(d, sdnSemSobrecarga, label='Balanceamento de Carga sem Sobrecarga')


#plt.xlabel('SDN com Sobrecarga')
plt.ylabel('Tempo de Carregamento em milissegundos (ms)')
plt.title('SDN com Balanceamento de Carga')
plt.ylim(0, 300)
plt.legend()

plt.show()
