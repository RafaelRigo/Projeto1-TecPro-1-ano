from prod import Produtorio

class Matematica:
    def __init__(self, numeroBase) -> None:
        self._numeroBase = numeroBase
    
    def fatorial(self, x: int) -> int:
        produtorio = Produtorio()

        num = 2
        while num != x:
            produtorio.multiplicar(num)
            num += 1

        return produtorio.valor

    def triangulo_de_Pascal(self):
        L = self._numeroBase
        triangulo = []

        for n in range(0, L-1):
            linha = ''
            for k in range(0, n):
                linha += f'{self.fatorial(n) / (self.fatorial(k) * self.fatorial(n-k))} '
            
            triangulo.append(linha.ljust(6))

        return triangulo