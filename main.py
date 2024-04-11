import os, tkinter as tk
from tkinter import filedialog
from obra import Obra

clear = lambda:os.system('cls') or None

root = tk.Tk()
root.withdraw()
root.attributes("-topmost", True)

def selecionar_arquivo():
    tipos_arq = (
        ('Texto', '*.txt'),
        ('HTML', '*.html'),
        ('Outros', '*.*')
    )

    arq = filedialog.askopenfilename(title='Escolha o arquivo que contém as obras',
                                          initialdir='C:',
                                          multiple = False,
                                          filetypes=tipos_arq)
    
    return arq

def cadastro_de_obras():
    root.update()

    nome_arq = selecionar_arquivo()
    obra = Obra(nome_arq, True)

    ano = ''
    while ano != '0':
        ano = input('Digite o ano da obra ("0" para sair e registrar as obras) -> ')
        if ano != '0':
            mes = input('Digite o mês da obra -> ')
            estilo = input('Digite o estilo da obra -> ')
            nome_obra = input('Digite o nome da obra -> ')
            nome_autor = input('Digite o nome do autor -> ')
            valor = input('Digite o valor estimado da obra -> ')
            url_foto = input('Digite o URL da foto da obra -> ')

            obra.preencherCampos(ano, mes, estilo, nome_obra, nome_autor, valor, url_foto)
            obra.gravarCamposNoArquivo()

            clear()
    obra.fecharArquivo()
    print('Suas obras foram registradas com êxito!')
    
def listagem_de_obras():
    root.update()

    nome_arq = selecionar_arquivo()
    obra = Obra(nome_arq, False)

    print('+-=••=-+-=••=-+-=••=--=••=--=••=--=••=--=••=-+-=••=--=••=--=••=--=••=-+-=••=--=••=--=••=-+-=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=-+')
    print('| Ano  | Mês  | Nome da Obra                 | Autor                  | Valor            | URL                                                                                                  |')
    print('+-=••=-+-=••=-+-=••=--=••=--=••=--=••=--=••=-+-=••=--=••=--=••=--=••=-+-=••=--=••=--=••=-+-=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=-+')

    while obra.anoDaObra != '':
        obra.lerCamposDoArquivo()
        if obra.anoDaObra != '':
            print(f'| {obra.anoDaObra.ljust(4)} | {obra.mesDaObra.ljust(4)} | {obra.nomeDaObra.ljust(28)} | {obra.autorDaObra.ljust(22)} | {str(obra.valorEstimado).ljust(16)} | {obra.urlFoto.ljust(100)} |')

    print('+-=••=-+-=••=-+-=••=--=••=--=••=--=••=--=••=-+-=••=--=••=--=••=--=••=-+-=••=--=••=--=••=-+-=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=--=••=-+')

def pagina_web_de_obras():
    pass

def triangulo_de_pascal():
    pass

def menu():
    clear()
    print('>=-•-•-•-•-•-=< MENU >=-•-•-•-•-•-=<')
    print('|1| - Cadastro de obras de arte')
    print('|2| - Listagem de obras de arte')
    print('|3| - Página Web de obras de arte')
    print('|4| - Triangulo de Pascal')
    print('|0| - Sair')
    print('>=-•-•-•-•-•-•-•-•-•-•--•-•-•-•-•-=<')

def seletor():
    continuar = lambda:input('\nDeseja continuar? [ENTER] -> ')
    opcao = ''
    while opcao != '0':
        menu()
        opcao = input('Digite a opção desejada -> ')
        clear()
        match opcao:
            case '1': cadastro_de_obras(), continuar()
            case '2': listagem_de_obras(), continuar()
            case '3': pagina_web_de_obras(), continuar()
            case '4': triangulo_de_pascal(), continuar()
    
    print("\nObrigado pelo uso, até mais!\n")

if __name__ == "__main__":
    seletor()
