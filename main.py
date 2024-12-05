import tkinter as tk
from view import View
from model import criar_tabela

if __name__ == "__main__":
    criar_tabela()

    root = tk.Tk()
    app = View(root)
    root.mainloop()
