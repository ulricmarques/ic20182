class Seta():
	def __init__(self, sentido, proximo, anterior):
		self.sentido = sentido
		self.proximo = proximo
		self.anterior = anterior

	def mostra_seta(self):
		print(self.sentido, end=' ')

	def pode_mover(self):
		if self.sentido == 'vazio':
			return False


		if self.sentido == '->':
			if (self.proximo.sentido == 'vazio' or (self.proximo.sentido != 'vazio' and self.proximo.sentido != self.sentido)):
				return True
		else:
			if (self.anterior.sentido == 'vazio' or (self.anterior.sentido != 'vazio' and self.anterior.sentido != self.sentido)):
				return True

		return False


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

		setaAtual.proximo = Seta('vazio', None, setaAtual)
		setaAtual = setaAtual.proximo
		self.mapa.append(setaAtual)
		i = 0
		while i < quant_setas:
			setaAtual.proximo = Seta('<-', None, setaAtual)
			setaAtual = setaAtual.proximo
			self.mapa.append(setaAtual)
			i+=1


	def mostra_mapa(self):
		for s in self.mapa:
			s.mostra_seta()
		print('\n#########')


estado = Estado(4)
estado.mostra_mapa()
for s in estado.mapa:
	print(s.sentido, s.pode_mover())











