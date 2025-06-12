import tkinter as tk
from tkinter import messagebox

class AppListaTarefas:
    def __init__(self, master):
        self.master = master
        master.title("Minha Lista de Tarefas")

        self.frame_tarefas = tk.Frame(master)
        self.frame_tarefas.pack(pady=10)

        self.lista_tarefas = tk.Listbox(self.frame_tarefas, height=10, width=50, border=0)
        self.lista_tarefas.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar_tarefas = tk.Scrollbar(self.frame_tarefas)
        self.scrollbar_tarefas.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.lista_tarefas.config(yscrollcommand=self.scrollbar_tarefas.set)
        self.scrollbar_tarefas.config(command=self.lista_tarefas.yview)

        # Campo de entrada e botão adicionar
        self.entrada_tarefa = tk.Entry(master, width=50)
        self.entrada_tarefa.pack(pady=10)

        self.btn_adicionar = tk.Button(master, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        self.btn_adicionar.pack(pady=5)

        self.btn_remover = tk.Button(master, text="Remover Tarefa", command=self.remover_tarefa)
        self.btn_remover.pack(pady=5)

    def adicionar_tarefa(self):
        tarefa = self.entrada_tarefa.get()
        if tarefa:
            self.lista_tarefas.insert(tk.END, tarefa)
            self.entrada_tarefa.delete(0, tk.END)
        else:
            messagebox.showwarning("Atenção", "Por favor, digite uma tarefa!")

    def remover_tarefa(self):
        try:
            indice_selecionado = self.lista_tarefas.curselection()
            self.lista_tarefas.delete(indice_selecionado)
        except:
            messagebox.showwarning("Atenção", "Selecione uma tarefa para remover.")

root = tk.Tk()
app = AppListaTarefas(root)
root.mainloop() 