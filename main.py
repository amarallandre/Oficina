import tkinter as tk
from tkinter import ttk
from gui.chegada_veiculo import ChegadaVeiculoTab

class OficinaMecanicaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gerenciamento da Oficina Mecânica")

        self.tabControl = ttk.Notebook(root)
        self.tab_chegada_veiculo = ChegadaVeiculoTab(self.tabControl)

        self.tabControl.add(self.tab_chegada_veiculo.tab, text="Chegada do Veículo")

        self.tabControl.pack(expand=1, fill="both")

if __name__ == "__main__":
    root = tk.Tk()
    app = OficinaMecanicaApp(root)
    root.mainloop()