import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkcalendar import DateEntry


class ChegadaVeiculoTab:
    def __init__(self, parent):
        self.tab = ttk.Frame(parent)

        self.placa_label = ttk.Label(self.tab, text="Placa:")
        self.placa_entry = ttk.Entry(self.tab)
        self.buscar_button = ttk.Button(self.tab, text="Buscar")

        self.placa_label.pack(pady=10)
        self.placa_entry.pack(pady=10)
        self.buscar_button.pack(pady=10)

        self.anexar_button = ttk.Button(self.tab, text="Anexar Foto")
        self.anexar_button.pack(pady=10)

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


    def registrar_evento(self, evento):
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Evento registrado em {data_hora}: {evento}")