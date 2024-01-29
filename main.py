import tkinter as tk
from tkinter import ttk
from gui.chegada_veiculo import ChegadaVeiculoTab
from gui.Ordem_de_servico import OrdemDeServicoTab

class OficinaMecanicaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gerenciamento da Oficina Mecânica")

        self.tabControl = ttk.Notebook(root)
        self.tab_chegada_veiculo = ChegadaVeiculoTab(self.tabControl)
        self.tab_ordem_de_servico = OrdemDeServicoTab(self.tabControl)

        self.tabControl.add(self.tab_chegada_veiculo.tab, text="Chegada do Veículo")
        self.tabControl.add(self.tab_ordem_de_servico.tab, text="Ordem de Serviço")

        self.tabControl.pack(expand=1, fill="both")

        def reiniciar_aplicacao(self):
            self.root.quit()  # Fecha a janela atual
            root = tk.Tk()  # Cria uma nova instância da aplicação
            app = OficinaMecanicaApp(root)
            root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = OficinaMecanicaApp(root)
    root.mainloop()