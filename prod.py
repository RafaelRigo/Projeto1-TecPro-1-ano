import math

class Produtorio:
    def __init__(self):
        self._produto = 1.0
        self._quantosForamMultiplicados = 0
        
    def multiplicar(self, valorAMultiplicar):
        self._produto = self._produto * valorAMultiplicar
        self._quantosForamMultiplicados += 1  # contando as multiplicações
        
    @property
    def valor(self):    # retorna o produtório atual para o programa principal
        return self._produto
    
    @property
    def quantos(self):  # retorna a quantidade de multiplicações para o programa principal
        return self._quantosForamMultiplicados
    
    def media_geometrica(self):
        if self._quantosForamMultiplicados <= 0:
            raise "Raiz da média geométrica inválida."
        
        media = math.pow(self._produto, 1 /  self._quantosForamMultiplicados)
        return media
        