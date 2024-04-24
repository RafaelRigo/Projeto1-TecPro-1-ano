import os, webbrowser, tkinter as tk
from tkinter import filedialog
from obra import Obra
from mat import Matematica

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
            valor = input('Digite o valor estimado da obra (em reais) -> ')
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
    root.update()

    arquivo = selecionar_arquivo()
    os.system(f'sort {arquivo} /o ordenado.txt /+1')
    obra = Obra('ordenado.txt', False)
    HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tabela das obras</title>
</head>
<style>
html {
    background-color: aliceblue;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}

table {
    margin: 50px auto;
}

table, tr, td, th {
    border: 4px solid aliceblue;
    border-collapse: collapse;
    padding: 10px;
    text-align: center;
}

img {
    width: 150px;
}

th {
    background-color: rgb(255, 220, 176);
}

td {
    background-image: radial-gradient(cornsilk, bisque);
}

tr:nth-child(1) th {
    border-top-left-radius: 30px;
    border-top-right-radius: 30px;
}

tr:nth-last-child(1) th:nth-child(1) {
    border-bottom-left-radius: 30px;
}

tr:nth-last-child(1) th:nth-last-child(1) {
    border-bottom-right-radius: 30px;
}

</style>
<body>
    <table>
        <tr>
            <th colspan="6">RELATÓRIO DE OBRAS DA GALERIA VIRTUAL</th>
        </tr>
        <tr>
            <th>Ano/Mês</th>
            <th>Dados</th>
            <th>Estilo</th>
            <th>Autor</th>
            <th>Valor</th>
            <th>Imagem</th>
        </tr>
"""
    ano = ""
    valor_ano = 0.0
    valor_geral = 0.0

    while obra.anoDaObra != "":
        obra.lerCamposDoArquivo()
        if obra.anoDaObra == ano or ano == "":
            HTML += f"""
        <tr>
            <td>{obra.anoDaObra} / {obra.mesDaObra}</td>
            <td>{obra.nomeDaObra}</td>
            <td>{obra.estilo}</td>
            <td>{obra.autorDaObra}</td>
            <td>{obra.valorEstimado}</td>
            <td><img src="{obra.urlFoto}"></td>
        </tr>
""" 
            if obra.valorEstimado != "...":
                valor_ano += obra.valorEstimado
                valor_geral += obra.valorEstimado

        else:
            HTML += f"""
        <tr>
            <th colspan="4">Total</th>
            <th>{valor_ano}</th>
            <th></th>
        </tr>
"""
            if obra.anoDaObra != "":
                HTML += f"""
        <tr>
            <td>{obra.anoDaObra} / {obra.mesDaObra}</td>
            <td>{obra.nomeDaObra}</td>
            <td>{obra.estilo}</td>
            <td>{obra.autorDaObra}</td>
            <td>{obra.valorEstimado}</td>
            <td><img src="{obra.urlFoto}"></td>
        </tr>
"""
                if obra.valorEstimado != "...":
                    valor_ano = obra.valorEstimado
                    valor_geral += obra.valorEstimado

        ano = obra.anoDaObra
    
    HTML += f"""
        <tr>
            <th colspan="4">Total Geral (R$)</th>
            <th>{valor_geral}</th>
            <th></th>
    </table>
</body>
</html>
"""
    
    arq_html = open("tabelaObras.html", "w", encoding='utf-8')

    arq_html.writelines(HTML)
    webbrowser.open_new_tab(arq_html.name)

    arq_html.close()

def triangulo_de_pascal():
    num = int(input("Digite o número de linhas do triângulo de Pascal -> "))

    mat = Matematica(num)

    clear()
    print("Triângulo de Pascal:")
    for linha in mat.triangulo_de_Pascal():
        print(linha)

def menu():
    clear()
    print('>=-•-•-•-•-•-=< MENU >=-•-•-•-•-•-=<')
    print('|1| - Cadastro de obras de arte')
    print('|2| - Listagem de obras de arte')
    print('|3| - Página Web de obras de arte')
    print('|4| - Triangulo de Pascal')
    print('|0| - Sair')
    print('>=-•-•-•-•-•-•-•-••-•-•-•-•-•-•-•-=<')

def seletor():
    continuar = lambda:input('\nDeseja continuar? [ENTER] -> ')
    opcao = ''
    while opcao != '0':
        menu()
        opcao = input('\nDigite a opção desejada -> ')
        clear()
        match opcao:
            case '1': cadastro_de_obras(), continuar()
            case '2': listagem_de_obras(), continuar()
            case '3': pagina_web_de_obras(), continuar()
            case '4': triangulo_de_pascal(), continuar()
    
    print("\nObrigado pelo uso, até mais!\n")

if __name__ == "__main__":
    seletor()
