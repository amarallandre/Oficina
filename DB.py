import mysql.connector
def conectar_banco():
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': '123456',
        'database': 'Workshop',
    }

    conexao = mysql.connector.connect(**config)
    return conexao




def inserir_veiculo(placa, descricao, data_chegada, hora_chegada):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    # Exemplo de query para inserção, ajuste conforme sua tabela
    query = "INSERT INTO veiculos (placa, descricao_problema, data_chegada, hora_chegada) VALUES (%s, %s, %s, %s)"
    valores = (placa, descricao, data_chegada, hora_chegada)

    cursor.execute(query, valores)
    conexao.commit()

    fechar_conexao(conexao, cursor)


def fechar_conexao(conexao, cursor):
    cursor.close()
    conexao.close()
