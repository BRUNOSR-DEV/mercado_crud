from utils.helper import formata_float_str_moeda

class Produto:
    contador: int = 1

    def __init__(self: object, nome: str, preco: float  ) -> None:
        self.__codigo: int = Produto.contador
        self.__nome: str = nome
        self.__preco:float = preco
        Produto.contador = Produto.contador +  1
    
    @property
    def nome(self)-> str:
        return self.__nome
    
    @property
    def preco(self)-> float:
        return self.__preco
    
    @property
    def codigo(self)-> int:
        return self.__codigo
    
    def __str__(self) -> str:
        return f'Código: {self.codigo} \nNome:{self.nome} \nPreço:{formata_float_str_moeda(self.preco)}'
    
