import tkinter as tk
from tkinter import ttk
from gui.chegada_veiculo import ChegadaVeiculoTab
from gui.Ordem_de_servico import OrdemDeServicoTab

class OficinaMecanicaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gerenciamento da Oficina Mecânica")

        # Botão para abrir a janela Chegada do Veículo
        self.btn_chegada_veiculo = ttk.Button(self.root, text="Chegada do Veículo", command=self.abrir_chegada_veiculo)
        self.btn_chegada_veiculo.pack(pady=10)

        # Botão para abrir a janela Ordem de Serviço
        self.btn_ordem_de_servico = ttk.Button(self.root, text="Ordem de Serviço", command=self.abrir_ordem_de_servico)
        self.btn_ordem_de_servico.pack(pady=10)

    def abrir_chegada_veiculo(self):
        # Cria e exibe a janela Chegada do Veículo
        janela_chegada_veiculo = tk.Toplevel(self.root)
        ChegadaVeiculoTab(janela_chegada_veiculo)
        janela_chegada_veiculo.title("Chegada do Veículo")

    def abrir_ordem_de_servico(self):
        # Cria e exibe a janela Ordem de Serviço
        janela_ordem_de_servico = tk.Toplevel(self.root)
        OrdemDeServicoTab(janela_ordem_de_servico)
        janela_ordem_de_servico.title("Ordem de Serviço")

if __name__ == "__main__":
    root = tk.Tk()
    app = OficinaMecanicaApp(root)
    root.mainloop()