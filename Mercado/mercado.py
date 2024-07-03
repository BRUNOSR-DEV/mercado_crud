def main() -> None:
    main()

from typing import List, Dict

from time import sleep # sleep da um tempo na execução para rodar o código

from models.produtos import Produto
from utils.helper import formata_float_str_moeda

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

            produto = Produto(obt,preco)
            
            list_produtos.append(produto)
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
    
   try:
       if len(list_produtos) > 0:
           print('Lista de Produtos')
           print('=================')

           for i in list_produtos:
               print(i)
               print('--------------------')
               sleep(1)
           Menu()
       else:
           print('Ainda não tem produtos cadastrados')
           sleep(2)
           Menu()
       
   except(ValueError):
       print('Valor informado incorreto! Tente novamente!')
       sleep(2)
       listar_produto()


def comprar_produto() -> None:
    if len(list_produtos) > 0:
        print("Informe o código do produto que deseja add ao carrinho.")
        print("======================================================")
        print("===============Lista de Produtos=================")

        if len(list_produtos) > 0:
           print('Lista de Produtos')
           print('=================')

           for i in list_produtos:
               print(i)
               print('--------------------')
               sleep(1)
        else:
            print('não tem produto cadastrado!')
            sleep(1)
            Menu()

        codigo: int = int(input('Digite o código do produto dejado: '))

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui quantidade {quant + 1} unidade no carrinho.')
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


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in list_produtos:
        if produto.codigo == codigo:
            p = produto
    return p






if __name__ == '__main__':
    Menu()