from models import Produto, Venda
import repositorio_vendas as rep_ven
import repositorio_produtos as rep_pro
import menus
from datetime import date #DATA PARA A VENDA REALIZADA AUTOMATICAMENTE

def menu_principal():
    while True:
        print('\nLanchonete escolar online:')
        print('1 - Cadastrar produto') # ok
        print('2 - Listar produtos') #ok
        print('3 - Registrar Venda')
        print('4 - Relatorios (produtos e vendas)')
        print('0 - SAIR') # ok

        opcao = input('Escolha uma opção: ')

        if opcao == "1":
            novo_produto = menus.menu_cadastrar_produto()
            if novo_produto:
                rep_pro.salvar_produto(novo_produto)
                print("Novo produto salvo com sucesso!")

        elif opcao == "2":
            print("Listando produtos...")
            produtos = rep_pro.listar_produto()
            menus.exibir_produtos(produtos)
        
        elif opcao == "3":
            cod,qtd_compra = menus.registrar_venda()

            if cod:
                produtos = rep_pro.listar_produto()
                produto_encontrado = None

                for p in produtos: # Busca do produto
                    if p.codigo == cod:
                        produto_encontrado = p
                        break

                if produto_encontrado:
                    if produto_encontrado.quantidade_estoque >= qtd_compra:
                        produto_encontrado.quantidade_estoque -= qtd_compra #estoque novo
                        
                        rep_pro.atualizar_estoque(produtos) #atualizar estoque
                        
                        print(f"Venda aprovada! Novo estoque: {produto_encontrado.quantidade_estoque}")
                        
                        data_atual = str(date.today())

                        venda_concluida = Venda(produto_encontrado.codigo, produto_encontrado.preco, produto_encontrado.nome, qtd_compra, data_atual)
                        rep_ven.salvar_venda(venda_concluida)

                    else:
                        print("Estoque insuficiente!")
                else:
                    print("Produto não encontrado!")
        elif opcao == "4":
            vendas = rep_ven.listar_vendas()
            total_vendas = 0

            for v in vendas:
                total_vendas += v.preco * v.quantidade_vendida
            print(f"\nRelatorio de venda: Lucro: {total_vendas: .2f}")

            produtos = rep_pro.listar_produto()
            print("\nRelatorio de Produtos: Estoque abaixo de 5 unidades = REPOR!")
            for p in produtos:
                if p.quantidade_estoque < 5:
                    print(f"Produto: {p.nome} com estoque baixo!")

        
            data_filtro = input("Digite a data para o relatorio (ANO-MES-DIA): ")
            total_dia = 0
            encontrou_venda = False

            for v in vendas:
                if v.data == data_filtro: 
                    total_dia += (v.preco * v.quantidade_vendida)
                    encontrou_venda = True
                    print(f"Produto: {v.produto}  Qtd: {v.quantidade_vendida}  Total: R$ {v.preco * v.quantidade_vendida:.2f}")

            if encontrou_venda:
                print(f"\nTOTAL VENDIDO NO DIA {data_filtro}: R$ {total_dia:.2f}")
            else:
                print(f"\nNenhuma venda encontrada para a data digitada.")

        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu_principal()