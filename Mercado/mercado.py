def main() -> None:
    main()

from time import sleep # sleep da um tempo na execução para rodar o código
from utils.helper import formata_float_str_moeda, conectar, desconectar

carrinho: list[list[int,int]] = []


def Menu() -> None:
    print('*********** Bem Vindo ***********')
    print('******** Mercado Da Vila *********')

    try:

        while True:
            escolha = int(input(f' \n[1]- Cadastrar Produto \n[2]- Listar Produtos \n[3]- Alterar Produto \n[4]- Deletar Produto \n[5]- Comprar o produto \n[6]- Visualizar, Alterar ou Deletar item do Carrinho \n[7]- Finalizar Pedido \n[8] Sair \nDigite: '))

            if escolha == 1:
                cadastrar_produto()
                break
            elif escolha == 2:
                listar_produto()
                break
            elif escolha == 3:
                alterar_produto()
                break
            elif escolha == 4:
                apagar_produto()
                break
            elif escolha == 5:
                comprar_produto()
                break
            elif escolha == 6:
                Visualizar_carrinho()
                break
            elif escolha == 7:
                fechar_pedido()
                break
            elif escolha == 8:
                print('Obrigado! Volte sempre!')
                break
            else:
                print('Escolha uma opção valida! ')

    except(ValueError,NameError) as err:
        print('Valor invalido!')
        Menu()


def cadastrar_produto() -> None:  #Inserir
    print('--------Cadastro de Produto-----------')
    print('--------------------------------------')
    print("-----Digite 'menu' para voltar--------)")

    try:
            obt = input('Informe o prduto: ')

            if obt == 'menu':
                Menu()
            else:
                preco = float(input('Informe o preço: '))

                conn = conectar()
                cursor = conn.cursor()

                cursor.execute(f"INSERT INTO produtos (produto, preco) VALUES ('{obt}',{preco})")
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
            print('--- Listando Produtos ---')
            print('-------------------------')
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


def alterar_produto(): #Update nos produtos

    print('--------- Alterar de Produtos-------------')
    print('------------------------------------------')

    listar_produto()

    op_alt = int(input('Qual o código do produto que deseja alterar? '))

    escolha = int(input('Qual campo deseja alterar : [1] Nome Produto [2] Preço Produto\n Digite [3] Para voltar para o Menu ')) 

    cod_prod = pega_codigo(op_alt)

    if cod_prod:
        conn= conectar()
        cursor = conn.cursor()

        if escolha == 1:
            alt = input('Digite o nome do produto: ')
            cursor.execute(f"UPDATE produtos set produto = '{alt}' WHERE id = {cod_prod} ")
            conn.commit()

        elif escolha == 2:
            alt = input('Digite o preço do produto: ')
            cursor.execute(f"UPDATE produtos set preco = '{alt}' WHERE id = {cod_prod} ")
            conn.commit()
        
        elif escolha == 3:
            Menu()

        else:
            print('Valor incorreto! Tente [1] ou [2] ')
            sleep(2)
            alterar_produto()
        
        if cursor.rowcount == 1:
            print(f'O dado {alt} foi inserido com sucesso. att bem sucedido')
        else:
            print('Não foi possível atualizar o valor.')

        continuar = int(input('Dejesa continuar alterando ? [1] Sim [2] Não '))
        if continuar == 1:
            alterar_produto()
        elif continuar == 2:
            Menu()
        else:
            print('Valor incorreto! ')
            sleep(2)
            Menu()

        desconectar(conn)
    
    else:
        print('Código não encontrado, ou valor incorreto! ')
        sleep(3)
        alterar_produto()


def apagar_produto(): # Deletar produtos

    print('--------- Deletar Produtos-------------')
    print('---------------------------------------')

    listar_produto()

    escolha = int(input('Qual o código do produto que deseja apagar ? '))

    cod_prod = pega_codigo(escolha)

    if cod_prod:
        nome_p = busca_nome_preco(cod_prod)

        duvida = int(input(f'Tem certeza que dejesa apagar o produto {nome_p[0]} de código {cod_prod} \n[1] Sim [2] Não  '))

        if duvida == 1:
            conn= conectar()
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM produtos WHERE id= {cod_prod}")
            conn.commit()

            if cursor.rowcount == 1:
                print(f'O Produto {nome_p[0]} foi Apagado com sucesso. Atualização bem sucedido')
            else:
                print('Não foi possível Deletar o valor.')

            desconectar(conn)

            continuar = int(input('Dejesa Apagar outro produto ? [1] Sim [2] Não '))
            if continuar == 1:
                apagar_produto()
            elif continuar == 2:
                Menu()
            else:
                print('Valor incorreto! ')
                sleep(2)
                Menu()

        elif duvida == 2:
            Menu()
            sleep(2)
        else:
            print('Valor incorreto! ')
            sleep(2)
            Menu()
    else:
        print('Código não correspondente ou valor incorreto! ')
        sleep(2)
        Menu()


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
    
        codigo: int = int(input('Digite o código do produto desejado: '))

        prod: int = pega_codigo(codigo)

        if prod:
            qtd = int(input("Qual é a quantidade desejada ?"))
            compra = [codigo,qtd]
            carrinho.append(compra)
            print('Compra Registrada com sucesso!')


            op = input('Inserir novo produto no carrinho? [sS] Sim - [nN] Não, voltar para o Menu \nInforme: ')

            if op == 's' or op == 'S':
                comprar_produto()
            elif op == 'n' or op == 'N':
                Menu()
            else:
                print("Valor invalido! Tente 's' ou 'n' ")

        else:
            print(f"O código digitado [{codigo}] não corresponde a um produto da lista. ")
            sleep(1)
            comprar_produto()


    else:
        print('Não tem produtos cadastrados.')
        sleep(2)
        Menu()
        
    desconectar(conn)


def Visualizar_carrinho() -> None: #Update e Deletar no carrinho

    if len(carrinho) > 0:
        print("=================")
        print('Produtos no carrinho.')
        print("=================")

        print(carrinho)
        
        total = 0

        for item in carrinho:
            dado = busca_nome_preco(item[0])
            print(f'Código: {item[0]} Produto: {dado[0]} Preço: {dado[1]} Quantidade: {item[1]}')
            print("----------------------------------------------------------")
            sleep(1)

            calc = dado[1] * item[1]
            total = total + calc

        up_drop = int(input(f'Deseja alterar a quantidade ou apagar algum item do carrinho ? \n[1] Sim [2] Não  '))

        if up_drop == 1:

            op = int(input('alterar ou apagar ? \n[1] Alterar [2] Apagar '))

            if op == 1:
                cod_alt = int(input('Digite o código do produto para alterar:  '))
                nova_qtd = int(input('Digite a nova quantidade: '))

                alterar_qtd(cod_alt,nova_qtd)
                Visualizar_carrinho()

            elif op == 2:
                cod_drop = int(input("Digite o código do produto para deletar: "))
                apagar_prod(cod_drop)
                sleep(2)
                Visualizar_carrinho()

            else:
                print('Valor incorreto tente os números correspondentes.')
                sleep(3)
                Visualizar_carrinho()


        elif up_drop == 2:

            print(f'Total da compra: {formata_float_str_moeda(total)} ')

            op = input(f'Finalizar compra [1] SIM [2] Não ?')

            if op == 1:
                fechar_pedido()
            elif op == 2:
                Menu()
            else:
                print("Valor invalido! Tente 's' ou 'n' ")

        else:
            print('Valor incorreto tente os números correspondentes.')
            sleep(3)
            Visualizar_carrinho()




    else:
        print('Ainda não existe produtos no carrinho')
        sleep(2)
        Menu()


def fechar_pedido()-> None:

    if len(carrinho) > 0:
        valor_total: float = 0

        print("---------Produtos do Carrinho---------------")
        print("--------------------------------------------")
        

        for item in carrinho:
            dado = busca_nome_preco(item[0])
            print(f'Produto: {dado[0]} Preço: {dado[1]} Quantidade: {item[1]}')
            print("----------------------------------------------------------")
            sleep(1)

            calc = dado[1] * item[1]
            valor_total = valor_total + calc

        finalizar = int(input(f'Deseja finalizar o pedido? [1] Sim - [2] Não (Menu) '))

        if finalizar == 1:
            print(f'Sua fatura é: {formata_float_str_moeda(valor_total)} ')
            print('Obrigado volte sempre!')
            carrinho.clear()
            sleep(6)
            Menu()
        elif finalizar == 2:
            Menu()
            sleep(2)
        else:
            print('Valor incorreto, tente 1 para sim, 2 para não (Menu)')
            fechar_pedido()

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
    

def busca_nome_preco(id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    
    for produto in produtos:
        if produto[0] == id:
            nome = produto[1]
            preco = produto[2]
            return (nome,preco)
    desconectar(conn)


def alterar_qtd(cod,qtd): # Altera produto do carrinho

    for item in carrinho:

        if cod == item[0]:
            item[1] = qtd
            print('Ateração bem sucedida! ')
            sleep(2)
        elif cod != item[0]:
            continue
        else:
            print('oioi número não correspondente')
    
    return carrinho


def apagar_prod(cod): #Deleta produto do carrinho

    cont = 0

    for item in carrinho:
        if item[0] == cod:
            carrinho.pop(cont)
            print('Produto apagado do carrinho com sucesso! ')
        elif item[0] != cod:
            cont = cont + 1
        else:
            print(f'Valor incorreto! tente novamente')
        
        



if __name__ == '__main__':
    Menu()