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

def obter_ordens_servico():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    query = "SELECT placa, descricao_problema FROM veiculos"
    cursor.execute(query)

    ordens_servico = cursor.fetchall()


    fechar_conexao(conexao, cursor)

    return ordens_servico

def obter_descricao_veiculo(placa):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    query = f"SELECT descricao_problema, data_chegada, hora_chegada FROM veiculos WHERE placa = '{placa}' "
    cursor.execute(query)

    descricao_veiculo = cursor.fetchone()

    fechar_conexao(conexao, cursor)

    return descricao_veiculo

def deletar_veiculo(placa):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    query = "DELETE FROM veiculos WHERE placa = %s"
    valores = (placa,)

    try:
        cursor.execute(query, valores)
        conexao.commit()
    except mysql.connector.Error as err:
        print(f"Erro ao deletar veiculo: {err}")

    fechar_conexao(conexao, cursor)



def fechar_conexao(conexao, cursor):
    cursor.close()
    conexao.close()
