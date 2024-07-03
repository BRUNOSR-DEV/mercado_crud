from utils.helper import conectar, desconectar, formata_float_str_moeda
from time import sleep
class Produto:

    def __init__(self: object, nome: str, preco: float  ) -> None:
        self.__nome: str = nome
        self.__preco:float = preco
    
    @property
    def nome(self)-> str:
        return self.__nome
    
    @property
    def preco(self)-> float:
        return self.__preco
    
    
    def __str__(self) -> str:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM produtos')
        produtos = cursor.fetchall()

        for produto in produtos:
            return f'Código: {produto[0]} \nNome:{produto[1]} \nPreço:{formata_float_str_moeda(produto[2])}'
        desconectar(conn)

    def cadastrar_produto(self):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(f"INSERT INTO produtos (nome, preco) VALUES ('{self.nome}',{self.preco})")
        conn.commit()

        if cursor.rowcount == 1:
            print(f'O produto {self.nome} foi cadastrado com sucesso.')
        else:
            print('Não foi possível cadastrar o produto.')
        desconectar(conn)
    



    







    '''def retorna_id(self):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM produtos')
        produtos = cursor.fetchall()

        for produto in produtos:
            return produto[0]'''

    

    
