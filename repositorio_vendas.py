import csv
from models import Venda

def salvar_venda(venda):
    with open('data/vendas.csv', 'a', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([venda.id_venda, venda.preco, venda.produto, venda.quantidade_vendida, venda.data])

def listar_vendas():
    lista_de_vendas = []
    try:
        with open('data/vendas.csv', 'r', newline='', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor) 
            for linha in leitor:
                v = Venda(linha[0], float(linha[1]), linha[2], int(linha[3]), linha[4])
                lista_de_vendas.append(v)
    except FileNotFoundError:
        return []
    
    return lista_de_vendas

