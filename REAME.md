# Projeto F - Controle de Estoque da Lanchonete Escolar

## Descrição
Este sistema foi desenvolvido para gerenciar o estoque e as vendas de uma lanchonete escolar, permitindo o cadastro de itens, controle de saldo e geração de relatórios financeiros e de reposição.

## Funcionalidades
- **Gestão de Produtos:** Cadastro e listagem com controle de preço e estoque.
- **Registro de Vendas:** Venda de produtos com baixa automática no estoque e impedimento de saldo negativo.
- **Relatórios:** - Faturamento total por período/dia.
  - Alerta de produtos com estoque baixo (limite de 5 unidades).

## ecnologias Utilizadas
- Python 3
- CSV (Persistência de dados)
- Programação Orientada a Objetos (POO)

##  Como Executar
1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório.
3. Certifique-se de que a pasta `data/` contenha os arquivos `produtos.csv` e `vendas.csv`.
4. Execute o arquivo principal:
   ```bash
   python main.py