# -*- coding: utf-8 -*-
import tkinter as tk

from theme import ThemeConfig
from telas.home import TelaHome
from telas.calculadora import TelaCalculadora
from telas.consumo import TelaConsumo
from telas.media import TelaMedia
from telas.imc import TelaIMC
from telas.sobre import TelaSobre


class AppCalculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Calculadora Multifuncional")
        self.geometry("1040x920")
        self.minsize(580, 600)
        
        self.tema_atual = "DARK"
        
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.telas = {}
        self.tela_atual = None
        
        self.telas_disponiveis = {
            "HOME": TelaHome,
            "CALCULADORA": TelaCalculadora,
            "CONSUMO": TelaConsumo,
            "MEDIA": TelaMedia,
            "IMC": TelaIMC,
            "SOBRE": TelaSobre
        }
        
        self.mostrar_tela("HOME")

    def mostrar_tela(self, nome_tela):
        print(f"Abrindo tela: {nome_tela}")
        
        if nome_tela not in self.telas:
            classe = self.telas_disponiveis[nome_tela]
            frame = classe(parent=self.container, controller=self)
            self.telas[nome_tela] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.tela_atual = nome_tela
        self.telas[nome_tela].tkraise()

    def alternar_tema(self):
        # Troca o tema
        if self.tema_atual == "DARK":
            self.tema_atual = "LIGHT"
        else:
            self.tema_atual = "DARK"
        
        # Atualiza a cor da janela principal
        cores = ThemeConfig.pegar_paleta(self.tema_atual)
        self.configure(bg=cores["bg_janela"])
        
        # Atualiza APENAS a tela que está visível no momento
        if self.tela_atual and self.tela_atual in self.telas:
            self.telas[self.tela_atual].atualizar_tema()


if __name__ == "__main__":
    app = AppCalculadora()
    app.mainloop()