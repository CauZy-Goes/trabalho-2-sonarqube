from model import *

class Controller:
    def __init__(self, view):
        self.view = view

    def adicionar_tarefa(self, tarefa):
        adicionar_tarefa(tarefa)

    def listar_tarefas(self):
        return listar_tarefas()

    def excluir_tarefa(self, id):
        excluir_tarefa(id)
