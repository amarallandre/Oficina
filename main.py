import tkinter as tk
from tkinter import ttk
from gui.chegada_veiculo import ChegadaVeiculoTab
from gui.Ordem_de_servico import OrdemDeServicoTab
from gui.servicos_em_andamento import ServicoEmAndamentoTab

class OficinaMecanicaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gerenciamento da Oficina Mecânica")

        largura = 250
        altura = 250

        # Use o método geometry para definir o tamanho da janela
        self.root.geometry(f"{largura}x{altura}")

        # Botão para abrir a janela Chegada do Veículo
        self.btn_chegada_veiculo = ttk.Button(self.root, text="Chegada do Veículo", command=self.abrir_chegada_veiculo)
        self.btn_chegada_veiculo.pack(pady=10)

        # Botão para abrir a janela Ordem de Serviço
        self.btn_ordem_de_servico = ttk.Button(self.root, text="Ordem de Serviço", command=self.abrir_ordem_de_servico)
        self.btn_ordem_de_servico.pack(pady=10)

        self.btn_servicos_em_andamento = ttk.Button(self.root, text="Serviços em andamento", command=self.abrir_servicos_em_andamento)
        self.btn_servicos_em_andamento.pack(pady=10)

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

    def abrir_servicos_em_andamento(self):
        # Cria e exibe a janela Ordem de Serviço
        janela_servicos_em_andamento = tk.Toplevel(self.root)
        ServicoEmAndamentoTab(janela_servicos_em_andamento)
        janela_servicos_em_andamento.title("Serviços em andamento")

if __name__ == "__main__":
    root = tk.Tk()
    app = OficinaMecanicaApp(root)
    root.mainloop()