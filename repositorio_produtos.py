import csv
from models import Produto

def salvar_produto(produto):
    with open('data/produtos.csv', 'a', newline='', encoding='utf-8') as arquivo: #'a' adicionar no arquivo, sem apagar o que existe, newline = não pular linhas em branco
        escritor = csv.writer(arquivo)
        escritor.writerow([produto.codigo,produto.nome,produto.quantidade_estoque,produto.preco])

def listar_produto():
    lista_de_produtos = [] #lista vazia para guardar os objetos

    try:
        with open('data/produtos.csv', 'r', newline='', encoding = 'utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor) #pular primeira linha (o cabeçalho criado)

            for linha in leitor:
                #[1,coxinha,5.0,10]
                p = Produto(linha[0],linha[1], float(linha[3]), int(linha[2]))
                lista_de_produtos.append(p)
    except FileExistsError:
        print('Arquivo ainda não existente!')
        return[]
    
    return lista_de_produtos


def atualizar_estoque(lista):
    with open('data/produtos.csv', 'w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['codigo', 'nome', 'quantidade_estoque', 'preco'])
    
        for p in lista:
            escritor.writerow([p.codigo, p.nome, p.quantidade_estoque, p.preco])