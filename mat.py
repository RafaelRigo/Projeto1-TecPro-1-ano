class Matematica:
    def __init__(self, numeroBase) -> None:
        self._numeroBase = numeroBase
    
    def fatorial(self, x: int) -> int:
        fatorial = 1
        
        while x >= 2:
            fatorial *= x
            x-= 1

        return fatorial

    def triangulo_de_Pascal(self):
        L = self._numeroBase
        triangulo = []

        for n in range(0, L):
            linha = ''
            for k in range(0, n+1):
                linha += f'{int(self.fatorial(n) // (self.fatorial(k) * self.fatorial(n-k)))} '
            
            triangulo.append(linha.ljust(6))

        return triangulo
