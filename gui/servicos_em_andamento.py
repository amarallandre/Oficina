import tkinter as tk
from tkinter import ttk
import os
import xml.etree.ElementTree as ET

class ServicoEmAndamentoTab:
    def __init__(self, parent):
        self.tab = ttk.Frame(parent)
        self.tab.pack()

        # Adicione widgets à sua tab aqui (exemplo: Label)
        self.label_placa = tk.Label(self.tab, text="Placa:")
        self.label_diagnostico = tk.Label(self.tab, text="Diagnóstico:")

        self.label_placa.grid(row=0, column=0, pady=5)
        self.label_diagnostico.grid(row=4, column=0, pady=5)

        self.contador = 0
        self.label_contador = ttk.Label(self.tab, text="Tempo: 00:00:00")
        self.label_contador.grid(row=6, column=0, pady=5)

        self.label_status = tk.Label(self.tab, text=f"Status: ")
        self.label_status.grid()

        self.finalizar_button = ttk.Button(self.tab, text="Finalizar serviço")
        self.finalizar_button.grid(row=10, column=0, pady=10)

        self.observacao_button = ttk.Button(self.tab, text="Observação")
        self.observacao_button.grid(row=11, column=0, pady=10)

        self.fechar_button = ttk.Button(self.tab, text="Fechar")
        self.fechar_button.grid(row=13, column=0, pady=10)

        self.mensagem_label = ttk.Label(self.tab, text="")
        self.mensagem_label.grid(row=8, column=0, pady=10)  # Use grid em vez de pack

        # Chama automaticamente a função carregar_xml ao criar a interface
        self.carregar_xml()
        self.atualizar_contador()

    def carregar_xml(self):
        pasta_servicos = "C:/Users/Usuario/Desktop/Codigos/Python/workshop/pythonProject/servicos"

        # Lista todos os arquivos na pasta
        lista_arquivos = os.listdir(pasta_servicos)

        # Filtra apenas os arquivos XML
        arquivos_xml = [arquivo for arquivo in lista_arquivos if arquivo.lower().endswith('.xml')]

        if arquivos_xml:
            # Abre o primeiro arquivo XML encontrado
            primeiro_arquivo_xml = arquivos_xml[0]
            caminho_arquivo_xml = os.path.join(pasta_servicos, primeiro_arquivo_xml)

            tree = ET.parse(caminho_arquivo_xml)
            root_xml = tree.getroot()

            # Obter informações do XML
            placa = root_xml.find('placa').text
            diagnostico = root_xml.find('diagnostico').text

            # Atualizar os widgets Tkinter com as informações do XML
            self.label_placa.config(text=f"Placa: {placa}")
            self.label_diagnostico.config(text=f"Diagnóstico: {diagnostico}")
        else:
            self.mensagem_label.config(text="Sem serviço")

    def atualizar_contador(self):
        horas = self.contador // 3600
        minutos = (self.contador % 3600) // 60
        segundos = self.contador % 60
        self.label_contador.config(text=f"Tempo: {hora_formatada(horas)}:{minuto_formatado(minutos)}:{segundo_formatado(segundos)}")

        # Incrementar o tempo
        self.contador += 1

        # Chamar novamente após 1000ms (1 segundo)
        self.tab.after(1000, self.atualizar_contador)

def hora_formatada(valor):
    return f"{valor:02d}"

def minuto_formatado(valor):
    return f"{valor:02d}"

def segundo_formatado(valor):
    return f"{valor:02d}"