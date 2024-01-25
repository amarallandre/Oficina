import tkinter as tk
from tkinter import ttk, filedialog
from datetime import datetime
from tkcalendar import DateEntry
from DB import inserir_veiculo, fechar_conexao, conectar_banco

class ChegadaVeiculoTab:
    def __init__(self, parent):
        self.tab = ttk.Frame(parent)

        self.placa_label = ttk.Label(self.tab, text="Placa:")
        self.placa_entry = ttk.Entry(self.tab)


        self.placa_label.pack(pady=10)
        self.placa_entry.pack(pady=10)


        self.anexar_button = ttk.Button(self.tab, text="Anexar Foto", command=self.anexar_foto)
        self.anexar_button.pack(pady=10)

        self.foto_anexada_label = ttk.Label(self.tab, text="")
        self.foto_anexada_label.pack(pady=10)


        self.descricao_label = ttk.Label(self.tab, text="Descrição do problema:")
        self.descricao_entry = ttk.Entry(self.tab)


        self.descricao_label.pack(pady=10)
        self.descricao_entry.pack(pady=10)

        self.data_label = ttk.Label(self.tab, text="Data de Chegada:")
        self.data_entry = DateEntry(self.tab, date_pattern="yyyy-mm-dd", width=12)

        self.hora_label = ttk.Label(self.tab, text="Hora de Chegada:")
        self.hora_entry = ttk.Entry(self.tab)

        self.data_label.pack(pady=5)
        self.data_entry.pack(pady=5)
        self.hora_label.pack(pady=5)
        self.hora_entry.pack(pady=5)

        self.cadastrar_button = ttk.Button(self.tab, text="Cadastrar", command=self.cadastrar_veiculo)
        self.cadastrar_button.pack(pady=10)

        self.mensagem_label = ttk.Label(self.tab, text="")
        self.mensagem_label.pack(pady=10)

    def anexar_foto(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.foto_anexada_label.config(text="Foto anexada")

    def registrar_evento(self, evento):
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Evento registrado em {data_hora}: {evento}")

    def cadastrar_veiculo(self):
        placa = self.placa_entry.get()
        descricao_problema = self.descricao_entry.get()
        data_chegada = self.data_entry.get()
        hora_chegada = self.hora_entry.get()

        inserir_veiculo(placa, descricao_problema, data_chegada, hora_chegada)
        self.mensagem_label.config(text="Veículo cadastrado com sucesso!")