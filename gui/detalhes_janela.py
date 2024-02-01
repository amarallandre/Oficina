import os
import tkinter as tk
from tkinter import ttk
import xml.etree.ElementTree as ET
import xml.dom.minidom

class DetalhesJanela:
    def __init__(self, master, placa, descricao, data_chegada, hora_chegada):
        self.master = master
        self.placa = placa
        self.descricao = descricao
        self.hora_chegada = hora_chegada
        self.data_chegada = data_chegada

        self.detalhes_window = tk.Toplevel(master)
        self.detalhes_window.title(f"Detalhes para a placa {placa}")

        # Adicione rótulos com informações detalhadas
        self.label_placa = tk.Label(self.detalhes_window, text=f"Placa: {placa}")
        self.label_placa.pack()



        self.label_descricao = tk.Label(self.detalhes_window, text=f"Descrição do problema: {descricao}")
        self.label_descricao.pack()

        self.label_data_chegada = tk.Label(self.detalhes_window, text=f"Data de Chegada: {data_chegada}")
        self.label_data_chegada.pack()

        self.label_hora_chegada = tk.Label(self.detalhes_window, text=f"Hora de Chegada: {hora_chegada}")
        self.label_hora_chegada.pack()

        self.diagnostico_label = ttk.Label(self.detalhes_window, text="Diagnostico:")
        self.diagnostico_label.pack(pady=5)

        self.diagnostico_text = tk.Text(self.detalhes_window, wrap='word', width=30, height=5)
        self.diagnostico_text.pack(pady=10)


        self.valor_label = ttk.Label(self.detalhes_window, text="Orçamento:")
        self.valor_label.pack(pady=5)

        self.valor_entry = ttk.Entry(self.detalhes_window)
        self.valor_entry.pack(pady=10)

        self.adicionar_valor_button = ttk.Button(self.detalhes_window, text="Iniciar Serviço", command=self.adicionar_valor)
        self.adicionar_valor_button.pack(pady=10)

        self.fechar_button = ttk.Button(self.detalhes_window, text="Fechar Janela", command=self.fechar_janela)
        self.fechar_button.pack(pady=10)

        self.mensagem_label = ttk.Label(self.detalhes_window, text="")
        self.mensagem_label.pack(pady=10)

    def adicionar_valor(self):

        # Obter informações dos widgets
        diagnostico = self.diagnostico_text.get("1.0", "end-1c")
        valor = self.valor_entry.get()

        # Especificar o caminho da pasta onde deseja salvar o arquivo XML
        pasta_destino = "./servicos"

        # Chamar a função para criar o XML
        self.criar_xml(self.placa, self.descricao, self.data_chegada, self.hora_chegada, diagnostico, valor,
                       pasta_destino)

    def criar_xml(self, placa, descricao, data_chegada, hora_chegada, diagnostico, valor, pasta_destino):
        # Criação de um elemento raiz para o arquivo XML
        root = ET.Element("servico")

        # Adicionando elementos com informações
        ET.SubElement(root, "placa").text = placa
        ET.SubElement(root, "descricao").text = descricao
        ET.SubElement(root, "data_chegada").text = data_chegada.isoformat()
        ET.SubElement(root, "hora_chegada").text = str(hora_chegada)
        ET.SubElement(root, "diagnostico").text = diagnostico
        ET.SubElement(root, "valor").text = valor

        # Criação de uma árvore XML a partir do elemento raiz
        ET.ElementTree(root)

        xml_string = ET.tostring(root, encoding="utf-8").decode("utf-8")
        dom = xml.dom.minidom.parseString(xml_string)
        pretty_xml_string = dom.toprettyxml(indent="  ")

        # Combinando o caminho da pasta de destino e o nome do arquivo
        caminho_completo = os.path.join(pasta_destino, f"{placa}_detalhes.xml")

        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        # Salvando a árvore XML no caminho completo

        if not diagnostico or not valor:
            self.mensagem_label.config(text="Por favor preencha todos os dados")
        else:
            with open(caminho_completo, "w", encoding="utf-8") as arquivo:
                arquivo.write(pretty_xml_string)
                self.mensagem_label.config(text="Serviço iniciado")

    def fechar_janela(self):
        self.detalhes_window.destroy()







