


class Mercado:

    def __init__(self) -> None:
        self.__mostrar_carrinho = self.mostrar_carrinho
        self.__listar_produtos = self.listar_produtos
    
    def mostrar_carrinho(self:object):
        pass

    def listar_produtos(self: object, interavel: list):
        for i in interavel:
            print(i)
    
    def _produtos(self:object):
        return self.produtos
        



class Cliente:

    def __init__(self, nome: str, cpf: str) -> None:
        self.__nome = nome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    

#produtos = {1:['arroz',23.50],2:['feijão',15.90],3:['miojo',1.90],4:['miojo',1.90],5:['miojo',1.90],6:['feijão',15.90],7:['baguete de pão',10.50]}