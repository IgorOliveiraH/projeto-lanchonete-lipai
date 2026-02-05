from models import Produto

def menu_cadastrar_produto(): #OPCAO 1
    print("CADASTRO DE PRODUTO: ")
    codigo = input ("Codigo do produto: ")
    nome =  input ("Nome do produto: ")
    preco = input ("Preço do produto: ")
    quantidade = input ("Quantidade do produto: ")

    if codigo and nome and preco and quantidade: #verifica se todos os campos estao preenchidos
        p = Produto(codigo, nome, float(preco), int(quantidade)) #objeto
        return p
    else:
        print("Produto invalido! Preencha todos os campos")
        return None

def exibir_produtos(lista): #opcao 2
    if lista:
        for p in lista:
            print(f"\n{p.codigo} - {p.nome}  Estoque: {p.quantidade_estoque}  Preço: R${p.preco}")
    else:
        print("Lista vazia!")
        return None

def registrar_venda():
    print("\nREGISTRO DE NOVA VENDA:")
    codigo = input("Codigo do produto: ")
    quantidade_vendido = input("Quantidade vendido: ")

    if codigo and quantidade_vendido:
        return codigo, int(quantidade_vendido)
    else:
        print("Codigo ou quantidade nula!")
        return None, None
