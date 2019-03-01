import matplotlib.pyplot as plt

naoSDNSobrecarga = [281.5]
x2 = ['Com Sobrecarga']

naoSDN = [88] 
x = ['Sem Sobrecarga']

sobrecargaerro = [0.23]
semsobrecargaerro = [0.57]


plt.bar(x2, naoSDNSobrecarga, label='Rede nao SDN, com Sobrecarga', yerr=sobrecargaerro)
plt.bar(x, naoSDN, label='Rede nao SDN, sem Sobrecarga', yerr=semsobrecargaerro)

#plt.xlabel('SDN com Sobrecarga')
plt.ylabel('Tempo de Carregamento da Pagina em milissegundos')
plt.title('Rede nao SDN, sem Balanceamento de Carga')
plt.ylim(0, 300)
plt.legend()

plt.show()
