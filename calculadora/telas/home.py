# -*- coding: utf-8 -*-
import tkinter as tk
from theme import ThemeConfig


class TelaHome(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Referências dos widgets que vão mudar de cor
        self.moldura = None
        self.card = None
        self.label_titulo = None
        self.btn_entrar = None
        self.btn_tema = None
        
        self.criar_interface()

    def criar_interface(self):
        cores = ThemeConfig.pegar_paleta(self.controller.tema_atual)
        self.configure(bg=cores["bg_janela"])

        card_largura = 700
        card_altura = 650
        
        self.moldura = tk.Frame(self, bg="#000000", padx=3, pady=3)
        self.moldura.place(relx=0.5, rely=0.5, anchor="center", width=card_largura, height=card_altura)

        self.card = tk.Frame(self.moldura, bg=cores["bg_card"])
        self.card.pack(fill="both", expand=True)

        # Título
        self.label_titulo = tk.Label(self.card, text="CALCULADORA", 
                                    font=("Georgia", 28, "bold"),
                                    bg=cores["bg_card"], fg=cores["texto_principal"])
        self.label_titulo.pack(pady=(50, 30))

        # Botão Entrar
        btn_entrar_borda = tk.Frame(self.card, bg="#000000", padx=1, pady=1)
        btn_entrar_borda.pack(pady=20)
        
        self.btn_entrar = tk.Button(btn_entrar_borda, text="Entrar", 
                                   font=("Georgia", 16, "bold"),
                                   bg=cores["bg_botao_primario"], 
                                   fg=cores["texto_botao_primario"],
                                   bd=0, padx=40, pady=8, cursor="hand2",
                                   command=lambda: self.controller.mostrar_tela("CALCULADORA"))
        self.btn_entrar.pack()

        # Botão de tema
        btn_tema_borda = tk.Frame(self.card, bg="#000000", padx=1, pady=1)
        btn_tema_borda.pack(side="left", padx=15, pady=(0, 15))
        
        texto_tema = "☀️ Tema Claro" if self.controller.tema_atual == "DARK" else "🌙 Tema Escuro"

        self.btn_tema = tk.Button(btn_tema_borda, text=texto_tema,
                                 font=("Helvetica", 9, "bold"),
                                 bg=cores["bg_botao_primario"],
                                 fg=cores["texto_botao_primario"],
                                 bd=0, padx=10, pady=4, cursor="hand2",
                                 command=self.controller.alternar_tema)
        self.btn_tema.pack()

    def atualizar_tema(self):
        """Atualiza apenas as cores, sem recriar a tela"""
        cores = ThemeConfig.pegar_paleta(self.controller.tema_atual)
        
        # Atualiza fundo da tela
        self.configure(bg=cores["bg_janela"])
        
        # Atualiza o card
        self.card.configure(bg=cores["bg_card"])
        
        # Atualiza o título
        self.label_titulo.configure(bg=cores["bg_card"], fg=cores["texto_principal"])
        
        # Atualiza o botão Entrar
        self.btn_entrar.configure(bg=cores["bg_botao_primario"], fg=cores["texto_botao_primario"])
        
        # Atualiza o botão de tema
        texto_tema = "☀️ Tema Claro" if self.controller.tema_atual == "DARK" else "🌙 Tema Escuro"
        self.btn_tema.configure(text=texto_tema, bg=cores["bg_botao_primario"], fg=cores["texto_botao_primario"])