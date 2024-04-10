class Obra:
    def __init__(self, nomeArq: str, aberto: bool) -> None:
        self.anoDaObra = ""
        self.mesDaObra = ""
        self.estilo = ""
        self.nomeDaObra = ""
        self.autorDaObra = ""
        self.valorEstimado = ""
        self.urlFoto = ""

        self._abertoParaGravacao = aberto
        if self._abertoParaGravacao:
            self._arquivo = open(nomeArq, 'a', encoding='utf-8')
        else:
            self._arquivo = open(nomeArq, 'r', encoding='utf-8')
    
    def lerCamposDoArquivo(self) -> None:
        if not self._abertoParaGravacao:
            linha = self._arquivo.readline()
            self.anoDaObra = linha[:4].rstrip()
            self.mesDaObra = linha[4:6].rstrip()
            self.estilo = linha[6:21].rstrip()
            self.nomeDaObra = linha[21:41].rstrip()
            self.autorDaObra = linha[41:61].rstrip()
            self.valorEstimado = float(linha[61:71].rstrip())
            self.urlFoto = linha[71:171].rstrip()

    def gravarCamposNoArquivo(self) -> None:
        if self._abertoParaGravacao:
            self._arquivo.writelines(
                self.anoDaObra.ljust(4) + 
                self.mesDaObra.ljust(2) + 
                self.estilo.ljust(15) +
                self.nomeDaObra.ljust(20) + 
                self.autorDaObra.ljust(20) + 
                self.valorEstimado.ljust(15) +
                self.urlFoto.ljust(100) + '\n'
                )

    def preencherCampos(self, novoAno: str, novoMes: str, novoEstilo: str, novoNome: str, nomeAutor: str, novoValor: str, novoURL: str) -> None:
        self.anoDaObra = novoAno
        self.mesDaObra = novoMes
        self.estilo = novoEstilo
        self.nomeDaObra = novoNome
        self.autorDaObra = nomeAutor
        self.valorEstimado = novoValor
        self.urlFoto = novoURL

    def fecharArquivo(self) -> None:
        self._arquivo.close()

    def __str__(self) -> str:
        return f"{
            self.anoDaObra.ljust(4) + 
            self.mesDaObra.ljust(2) + 
            self.estilo.ljust(15) +
            self.nomeDaObra.ljust(20) + 
            self.autorDaObra.ljust(20) + 
            str(self.valorEstimado).ljust(15) +
            self.urlFoto.ljust(100)
            }"

    def compararCom(self, outraObra) -> int:
        if not isinstance(outraObra, Obra): # verifica se o parâmetro 'outraObra' é uma instância da classe 'Obra'
            raise TypeError("O parâmetro deve ser instância da classe \"Obra\"")

        inst_atual = self.anoDaObra + self.mesDaObra + self.autorDaObra + self.nomeDaObra
        outra_inst = outraObra.anoDaObra + outraObra.mesDaObra + outraObra.autorDaObra + outraObra.nomeDaObra

        if len(inst_atual) < len(outra_inst):
            return -1
        elif len(inst_atual) == len(outra_inst):
            return 0
        elif len(inst_atual) > len(outra_inst):
            return 1