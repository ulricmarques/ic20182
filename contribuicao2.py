class Seta():
	def __init__(self, sentido, proximo, anterior):
		self.sentido = sentido
		self.proximo = proximo
		self.anterior = anterior

	def mostra_seta(self):
		print(self.sentido, end=' ')


class Estado():
	def __init__(self, quant_setas):
		# inicializa o problema
		self.mapa = []
		setaAtual = Seta('->', None, None)
		self.mapa.append(setaAtual)
		i = 1
		while i < quant_setas:
			setaAtual.proximo = Seta('->', None, setaAtual)
			setaAtual = setaAtual.proximo
			self.mapa.append(setaAtual)
			i+=1

		setaAtual = Seta('vazio', None, setaAtual)
		self.mapa.append(setaAtual)
		i = 0
		while i < quant_setas:
			setaAtual.proximo = Seta('<-', setaAtual, None)
			setaAtual = setaAtual.proximo
			self.mapa.append(setaAtual)
			i+=1



	def mostra_mapa(self):
		for s in self.mapa:
			s.mostra_seta()
		print('\n#########')



estado = Estado(4)
estado.mostra_mapa()











