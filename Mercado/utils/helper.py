import MySQLdb 


def formata_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'


def conectar():

    """
    Função para conectar ao servidor
    """
    try:
        conn = MySQLdb.connect(
            db= 'mydb',
            host= 'localhost',
            user= 'hey',
            passwd= 'boney',
        )
        return conn

    except MySQLdb.Error as e:
        print(f'Erro na conexão ao MySql Server: {e}')


def desconectar(conn):
    """ 
    Função para desconectar do servidor.
    """
    if conn:
        conn.close()









