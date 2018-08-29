# Contribuicao 3 - 8 Puzzle

import random

class Estado:

    def __init__(self):
        
        self.tamanho_mapa = 3
        self.quantidade_pecas = 9
        self.meta = [1,2,3,4,5,6,7,8,0]

    def mostra_estado(self, estado):
        for (indice, valor) in enumerate(estado):
            print ' %s ' % valor, 
            if indice in [x for x in range(self.tamanho_mapa - 1, self.quantidade_pecas, self.tamanho_mapa)]:
                print 
        print 

    def movimentos_validos(self, chave):

        valores = [1, -1, self.tamanho_mapa, -self.tamanho_mapa]
        validos = []
        for x in valores:
            if 0 <= chave + x < self.quantidade_pecas:
                if x == 1 and chave in range(self.tamanho_mapa - 1, self.quantidade_pecas, 
                        self.tamanho_mapa):
                    continue
                if x == -1 and chave in range(0, self.quantidade_pecas, self.tamanho_mapa):
                    continue
                validos.append(x)
        return validos

    def expandir(self, estado):

        expansoes_possiveis = {}
        for chave in range(self.quantidade_pecas):
            expansoes_possiveis[chave] = self.movimentos_validos(chave)
        posicao = estado.index(0)
        movimentos = expansoes_possiveis[posicao]
        estados_possiveis = []
        for mv in movimentos:
            nEstado = estado[:]
            (nEstado[posicao + mv], nEstado[posicao]) = (nEstado[posicao], nEstado[posicao + 
                    mv])
            estados_possiveis.append(nEstado)
        return estados_possiveis

    def escolhe_um_estado(self, estado):

        possiveis_estados = self.expandir(estado)
        estado_aleatorio = random.choice(possiveis_estados)
        return estado_aleatorio

    def estado_inicial(self, embaralhamentos=1000):

        estado_inicial = (self.meta)[:]
        for estados in range(embaralhamentos):
            estado_inicial = self.escolhe_um_estado(estado_inicial)
        return estado_inicial

    def estado_final(self, estado):

        return estado == self.meta

    def distancia_manhattan(self, estado):
       
        dist_manhattan = 0
        for peca in estado:
            if peca != 0:
                gdist = abs(self.meta.index(peca) - estado.index(peca))
                (pulos, passos) = (gdist // self.tamanho_mapa, gdist % self.tamanho_mapa)
                dist_manhattan += pulos + passos
        return dist_manhattan

    def heuristica_proximo_estado(self, estado):
       
        possiveis_estados = self.expandir(estado)
        dists_manhattan = []
        for estado in possiveis_estados:
            dists_manhattan.append(self.distancia_manhattan(estado))
        dists_manhattan.sort()
        caminho_mais_curto = dists_manhattan[0]
        if dists_manhattan.count(caminho_mais_curto) > 1:
            caminhos = [estado for estado in possiveis_estados if self.distancia_manhattan(estado) == caminho_mais_curto]
            return random.choice(caminhos)
        else:
            for estado in possiveis_estados:
                if self.distancia_manhattan(estado) == caminho_mais_curto:
                    return estado

    def solucionar(self, estado):
        while not self.estado_final(estado):
            estado = self.heuristica_proximo_estado(estado)
            self.mostra_estado(estado)


if __name__ == '__main__':
    print 10 * '-'
    estado = Estado()
    print 'Estado inicial:'
    inicio = estado.estado_inicial(10)
    estado.mostra_estado(inicio)
    print 'Objetivo:'
    estado.mostra_estado(estado.meta)
    print 'Passos:'
    estado.mostra_estado(inicio)
    estado.solucionar(inicio)