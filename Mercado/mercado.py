def main() -> None:
    main()

from typing import List, Dict

from time import sleep # sleep da um tempo na execução para rodar o código
from time import sleep
from models.produtos import Produto
from utils.helper import formata_float_str_moeda, conectar, desconectar

list_produtos: list[Produto] = []
carrinho: list[dict[Produto,int]] = []



def Menu() -> None:
    print('*********** Bem Vindo ***********')
    print('******** Mercado Da Vila *********')

    try:

        while True:
            escolha = int(input(f' \n[1]- Cadastrar Produto \n[2]- Listar Produto \n[3]- Compra o produto \n[4]- Visualizar Carrinho \n[5]- Finalizar Pedido \n[6] Sair \nEscolha: '))

            if escolha == 1:
                cadastrar_produto()
                break
            elif escolha == 2:
                listar_produto()
                break
            elif escolha == 3:
                comprar_produto()
                break
            elif escolha == 4:
                Visualizar_carrinho()
                break
            elif escolha == 5:
                fechar_pedido()
                break
            elif escolha == 6:
                print('Obrigado! Volte sempre!')
                break
            else:
                print('Escolha uma opção valida! ')

    except(ValueError,NameError) as err:
        print('Valor invalido!')
        Menu()


def cadastrar_produto() -> None:  #Inserir
    print('Cadastro de Produto')
    print('===================')

    try:
            obt = input('Informe o prduto: ')
            preco = float(input('Informe o preço: '))

            conn = conectar()
            cursor = conn.cursor()

            cursor.execute(f"INSERT INTO produtos (nome, preco) VALUES ('{obt}',{preco})")
            conn.commit()

            if cursor.rowcount == 1:
                print(f'O produto {obt} foi cadastrado com sucesso.')
            else:
                print('Não foi possível cadastrar o produto.')
            desconectar(conn)

            op = input('Inserir novo produto? [sS] Sim - [nN] Não, voltar para o Menu \nInforme: ')
            if op == 's' or op == 'S':
                cadastrar_produto()
            elif op == 'n' or op == 'N':
                Menu()
            else:
                print("Valor invalido! Tente 's' ou 'n' ")

    except(ValueError) as err:
        print("Valor invalido! Tente 's' ou 'n'")
        sleep(1)
        Menu()


def listar_produto() -> None:  #Listar
    
        """
        Função para listar os produtos
        """
        conn= conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM produtos')
        produtos = cursor.fetchall()

        if len(produtos) > 0:
            print('listando Produtos...')
            print('***************')
            for produto in produtos:
                print('--------------------------')
                print(f'Código: {produto[0]}')
                print(f'Produto: {produto[1]}')
                print(f'Preço: {produto[2]}')
                print('--------------------------')
                sleep(1)
        else:
            print('Não existe produtos cadastrados.')
            sleep(1)
        desconectar(conn)


def comprar_produto() -> None:
        
    conn= conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()

    if len(produtos) > 0:
        print("Informe o código do produto que deseja add ao carrinho.")
        print("======================================================")
        print("===============Lista de Produtos=================")

        listar_produto()
    

        codigo: int = int(input('Digite o código do produto dejado: '))

        prod: int = pega_codigo(codigo)

        for produto in produtos:

            if prod:
                
                if len(carrinho) > 0:
                    qtd = 1
                    if prod in carrinho:

                        pass
                    tem_no_carrinho: bool = False

                    for item in carrinho:
                        quant: int = item.get(produto)
                        if quant:
                            item[produto] = quant + 1
                            print(f'O produto {produto[1]} agora possui{quant + 1} unidades no carrinho.')
                            tem_no_carrinho = True
                            sleep(2)
                            Menu()
                    if not tem_no_carrinho:
                        prod: produto = {produto:1}
                        carrinho.append(prod)
                        print(f'O produto {produto.nome} foi add ao carrinho.')
                        sleep(2)
                        Menu()


                else:
                    item = {produto: 1}
                    carrinho.append(item)
                    print(f'O produto {produto.nome} foi add ao carrinho.')
                    sleep(1)
                    Menu()
            else:
                print(F"O PRODUTO COM O CÓDIGO {codigo} NÃO FOI ENCONTRADO ")
                sleep(2)
                Menu()

    else:
        print('Não tem produtos cadastrados.')
        sleep(2)
        Menu()


def Visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print("=================")
        print('Produtos do carrinho.')
        print("=================")

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print(f'-----------------------')
                sleep(1)
            Menu()

    else:
        print('Ainda não existe produtos no carrinho')
        sleep(2)
        Menu()


def fechar_pedido()-> None:
    if len(carrinho) >0:
        valor_total: float = 0

        print("Produtos do Carrinho")
        for item in carrinho:
            for dados in item.itens():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('----------------------------------')
                sleep(2)
        print(f"Sua fatura é {formata_float_str_moeda(valor_total)}")
        print('Volte sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Não tem itens no carrinho')
        sleep(2)
        Menu()


def pega_codigo(codigo: int) -> int:
    p: int = None

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()

    for produto in produtos:
        if produto[0] == codigo:
            p = produto[0]
    desconectar(conn)
    return p
    






if __name__ == '__main__':
    Menu()