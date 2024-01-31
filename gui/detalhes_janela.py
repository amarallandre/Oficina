import tkinter as tk
from tkinter import ttk


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

        self.label_descricao = tk.Label(self.detalhes_window, text=f"Status: ")
        self.label_descricao.pack()

        self.label_descricao = tk.Label(self.detalhes_window, text=f"Descrição do problema: {descricao}")
        self.label_descricao.pack()

        self.label_data_chegada = tk.Label(self.detalhes_window, text=f"Data de Chegada: {data_chegada}")
        self.label_data_chegada.pack()

        self.label_hora_chegada = tk.Label(self.detalhes_window, text=f"Hora de Chegada: {hora_chegada}")
        self.label_hora_chegada.pack()

        self.descricao_label = ttk.Label(self.detalhes_window, text="Diagnostico:")
        self.descricao_label.pack(pady=5)

        self.descricao_text = tk.Text(self.detalhes_window, wrap='word', width=30, height=5)
        self.descricao_text.pack(pady=10)


        self.valor_label = ttk.Label(self.detalhes_window, text="Orçamento:")
        self.valor_label.pack(pady=5)

        self.valor_entry = ttk.Entry(self.detalhes_window)
        self.valor_entry.pack(pady=10)





        self.adicionar_valor_button = ttk.Button(self.detalhes_window, text="Iniciar Serviço",
                                                 command=self.adicionar_valor)
        self.adicionar_valor_button.pack(pady=10)

    def adicionar_valor(self):
        novo_valor = self.valor_entry.get()
        float(novo_valor)




