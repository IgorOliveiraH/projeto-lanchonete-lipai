'''classes'''

class Produto:
    def __init__(self,codigo,nome,preco,quantidade_estoque):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

class Venda:
    def __init__ (self,id_venda,preco,produto, quantidade_vendida,data):
        self.id_venda = id_venda
        self.preco = preco
        self.produto = produto
        self.quantidade_vendida = quantidade_vendida
        self.data = data
        