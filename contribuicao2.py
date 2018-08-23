mapaInicial = [1,1,1,1,0,-1,-1,-1,-1]
mapaFinal = [-1,-1,-1,-1,0,1,1,1,1]

def movimentos_validos(mapa):
	movimentos = []
	for posicao, seta in enumerate(mapa):
		salto = posicao + (seta * 2)
		avanco = posicao + (seta)

		if seta == 0:
			continue

		if not (salto < 0 or salto >= len(mapa)):
			if (mapa[salto] == 0):
				temp = list(mapa)
				temp[posicao] = 0
				temp[salto] = seta
				movimentos.append(temp)

		if not (avanco < 0 or avanco >= len(mapa)):
			if (mapa[avanco] == 0):
				temp = list(mapa)
				temp[posicao] = 0
				temp[avanco] = seta
				movimentos.append(temp)

	return movimentos


def bfs( mapaAtual, mapaFinal ):
    proximo = []
    for seta in mapaAtual:
        filhos = movimentos_validos(seta[-1])
        for elem in filhos:
            temp = list(seta)
            temp.append(elem)
            if ( elem == mapaFinal ):
                return temp
            proximo.append(temp)
    return proximo


def resolve_problema(mapaInicial, mapaFinal):
    temp = [[mapaInicial]]

    while(temp[-1] != mapaFinal):
        temp = bfs(temp, mapaFinal)

    for estado in temp:
    	print estado	

    return temp

resolve_problema(mapaInicial, mapaFinal)