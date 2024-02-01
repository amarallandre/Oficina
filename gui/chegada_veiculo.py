import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkcalendar import DateEntry
from DB import inserir_veiculo
import time

class ChegadaVeiculoTab:
    def __init__(self, parent):
        self.tab = ttk.Frame(parent)
        self.tab.pack()

        self.placa_label = ttk.Label(self.tab, text="Placa:")
        self.placa_label.pack(pady=10)
        self.placa_entry = ttk.Entry(self.tab)
        self.placa_entry.pack(pady=10)

        self.descricao_label = ttk.Label(self.tab, text="Descrição do problema:")
        self.descricao_label.pack(pady=10)
        self.descricao_entry = ttk.Entry(self.tab)
        self.descricao_entry.pack(pady=10)

        self.data_label = ttk.Label(self.tab, text="Data de Chegada:")
        self.data_label.pack(pady=5)
        self.data_entry = DateEntry(self.tab, date_pattern="yyyy-mm-dd", width=12)
        self.data_entry.pack(pady=5)

        self.hora_label = ttk.Label(self.tab, text="Hora de Chegada:")
        self.hora_label.pack(pady=5)
        self.hora_entry = ttk.Entry(self.tab)
        self.hora_entry.pack()
        self.hora_entry.pack(pady=5)

        self.atualizar_hora()

        self.cadastrar_button = ttk.Button(self.tab, text="Cadastrar", command=self.cadastrar_veiculo)
        self.cadastrar_button.pack(pady=10)

        self.fechar_button = ttk.Button(self.tab, text="Fechar Janela", command=self.fechar_janela)
        self.fechar_button.pack(pady=10)

        self.mensagem_label = ttk.Label(self.tab, text="")
        self.mensagem_label.pack(pady=10)




    def registrar_evento(self, evento):
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(f"Evento registrado em {data_hora}: {evento}")

    def atualizar_hora(self):
        hora_atual = time.strftime("%H:%M")

        self.hora_entry.delete(0, tk.END)
        self.hora_entry.insert(0, hora_atual)

        self.tab.after(1000, self.atualizar_hora)


    def cadastrar_veiculo(self):
        placa = self.placa_entry.get()
        descricao_problema = self.descricao_entry.get()
        data_chegada = self.data_entry.get()
        hora_chegada = self.hora_entry.get()
        if not placa or not  descricao_problema:
            self.mensagem_label.config(text="Por favor preencha todos os dados")
        else:
            inserir_veiculo(placa, descricao_problema, data_chegada, hora_chegada)
            self.mensagem_label.config(text="Veículo cadastrado com sucesso!")

    def fechar_janela(self):
        self.tab.master.destroy()





