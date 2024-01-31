
from tkinter import ttk
from DB import obter_ordens_servico, deletar_veiculo, obter_descricao_veiculo
from gui.detalhes_janela import DetalhesJanela

class OrdemDeServicoTab:

    def __init__(self, parent):
        self.tab = ttk.Frame(parent)
        self.tab.pack()

        self.ordem_servico_tree = ttk.Treeview(self.tab, columns=('Placa', 'Descrição'))
        self.ordem_servico_tree.heading('Placa', text="Placa")
        self.ordem_servico_tree.heading('Descrição', text="Descrição do problema")
        self.ordem_servico_tree['show'] = 'headings'

        self.ordem_servico_tree.pack(pady=5)

        self.selecionar_button = ttk.Button(self.tab, text="Selecionar", command=self.abrir_janela_detalhes)
        self.selecionar_button.pack(pady=10)

        self.excluir_button = ttk.Button(self.tab, text="Excluir", command=self.deletar_veiculo)
        self.excluir_button.pack(pady=10)

        self.fechar_button = ttk.Button(self.tab, text="Fechar Janela", command=self.fechar_janela)
        self.fechar_button.pack(pady=10)

        self.atualizar_tabela_ordem_servico()

    def atualizar_tabela_ordem_servico(self):

        ordens_servico = obter_ordens_servico()

        for ordens_servico_item in ordens_servico:
            self.ordem_servico_tree.insert('', 'end', values=ordens_servico_item)

    def abrir_janela_detalhes(self):
        item_selecionado = self.ordem_servico_tree.selection()

        if item_selecionado:
            valores_selecionados = self.ordem_servico_tree.item(item_selecionado, 'value')

            placa = valores_selecionados[0] if valores_selecionados else None

            self.exibir_detalhes(placa)

    def exibir_detalhes(self, placa):
        detalhes_descricao_veiculo = obter_descricao_veiculo(placa)

        if detalhes_descricao_veiculo:
            DetalhesJanela(self.tab.master, placa, *detalhes_descricao_veiculo)


    def deletar_veiculo(self):
        # Obtenha o item selecionado na Treeview
        item_selecionado = self.ordem_servico_tree.selection()

        if item_selecionado:
            # Obtém os valores da linha selecionada
            valores_selecionados = self.ordem_servico_tree.item(item_selecionado, 'values')

            # Se o valor existe, pegue a placa (substitua 'coluna_placa' pelo nome real da coluna)
            placa = valores_selecionados[0] if valores_selecionados else None


            deletar_veiculo(placa)
            self.ordem_servico_tree.delete(item_selecionado)

    def fechar_janela(self):
        self.tab.master.destroy()

