import tkinter as tk
from tkinter import messagebox
from controller import Controller

class View:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")

        self.controller = Controller(self)

        # Campo de texto para descrever a tarefa
        self.tarefa_entry = tk.Entry(self.root, width=40)
        self.tarefa_entry.pack(pady=10)

        # Botão para adicionar a tarefa
        self.adicionar_button = tk.Button(self.root, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        self.adicionar_button.pack(pady=5)

        # Campos que lista todas as tarefas
        self.lista_frame = tk.Frame(self.root)
        self.lista_frame.pack(pady=10)

        self.atualizar_lista()

    def adicionar_tarefa(self):
        tarefa = self.tarefa_entry.get()
        if tarefa:
            self.controller.adicionar_tarefa(tarefa)
            self.tarefa_entry.delete(0, tk.END)
            self.atualizar_lista()
        else:
            messagebox.showwarning("Entrada inválida", "Por favor, insira uma tarefa.")

    def excluir_tarefa(self, id):
        self.controller.excluir_tarefa(id)
        self.atualizar_lista()

    def atualizar_lista(self):
        for widget in self.lista_frame.winfo_children():
            widget.destroy()

        tarefas = self.controller.listar_tarefas()
        for tarefa in tarefas:
            tarefa_text = tarefa[1]
            tarefa_id = tarefa[0]
            tarefa_label = tk.Label(self.lista_frame, text=tarefa_text, width=40, anchor='w')
            tarefa_label.pack(pady=5)

            # Botão para excluir a tarefa
            excluir_button = tk.Button(self.lista_frame, text="Excluir", command=lambda id=tarefa_id: self.excluir_tarefa(id))
            excluir_button.pack(pady=5)
