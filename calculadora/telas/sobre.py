# -*- coding: utf-8 -*-
import tkinter as tk
from theme import ThemeConfig


class TelaSobre(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.criar_interface()

    def criar_interface(self):
        cores = ThemeConfig.pegar_paleta(self.controller.tema_atual)
        self.configure(bg=cores["bg_janela"])
        
        for widget in self.winfo_children():
            widget.destroy()
        
        # Cabeçalho
        cabecalho = tk.Frame(self, bg=cores["bg_janela"])
        cabecalho.pack(fill="x", padx=30, pady=(20, 0))

        abas = [
            ("Calculadora", "CALCULADORA"),
            ("Consumo", "CONSUMO"),
            ("Média", "MEDIA"),
            ("IMC", "IMC"),
            ("Sobre", "SOBRE")
        ]

        for nome, chave in abas:
            ativa = (chave == "SOBRE")
            cor = cores["texto_principal"] if ativa else cores["texto_secundario"]
            fonte = ("Georgia", 11, "bold" if ativa else "normal")
            btn = tk.Button(cabecalho, text=nome, font=fonte, fg=cor,
                           bg=cores["bg_janela"], bd=0, cursor="hand2",
                           command=lambda k=chave: self.controller.mostrar_tela(k))
            btn.pack(side="left", expand=True, fill="x", padx=5)

        # Container
        container = tk.Frame(self, bg=cores["bg_janela"])
        container.place(relx=0.5, rely=0.52, anchor="center", width=520, height=500)
        
        # Área com scroll
        canvas = tk.Canvas(container, bg=cores["bg_janela"], highlightthickness=0)
        scroll = tk.Scrollbar(container, orient=tk.VERTICAL, command=canvas.yview)
        frame_scroll = tk.Frame(canvas, bg=cores["bg_janela"])
        
        frame_scroll.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=frame_scroll, anchor="nw")
        canvas.configure(yscrollcommand=scroll.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        
        # Cards
        self.criar_card(frame_scroll, cores, "📱 Calculadora Multifuncional",
                       "Projeto desenvolvido para a disciplina de Programação\ncom Python e Tkinter")
        
        self.criar_card(frame_scroll, cores, "👥 Desenvolvedores",
                       "João Silva - Programação\nMaria Santos - Design\nPedro Oliveira - Testes")
        
        self.criar_card(frame_scroll, cores, "🛠️ Tecnologias",
                       "• Python 3\n• Tkinter (GUI)\n• Biblioteca Math")
        
        self.criar_card(frame_scroll, cores, "⚙️ Funcionalidades",
                       "• Calculadora (+, -, x, ÷, %, √)\n• Consumo de energia elétrica\n• Média de valores\n• Cálculo de IMC\n• Tema claro/escuro")
        
        self.criar_card(frame_scroll, cores, "🎯 Objetivo",
                       "Criar uma aplicação prática que reúna várias\nferramentas úteis em uma interface moderna.")
        
        self.criar_card(frame_scroll, cores, "📅 Versão", "Versão 2.0 - 2024")
        
        tk.Frame(frame_scroll, height=20, bg=cores["bg_janela"]).pack()
        
        # Botão Home
        home_borda = tk.Frame(self, bg="#000000", padx=1, pady=1)
        home_borda.place(relx=0.05, rely=0.95, anchor="sw")
        tk.Button(home_borda, text="⌂", font=("Helvetica", 14, "bold"),
                 bg=cores["bg_botao_numero"], fg=cores["texto_botao_numero"],
                 bd=0, padx=10, pady=4, cursor="hand2",
                 command=lambda: self.controller.mostrar_tela("HOME")).pack()

    def criar_card(self, parent, cores, titulo, conteudo):
        card_borda = tk.Frame(parent, bg="#000000", padx=1, pady=1)
        card_borda.pack(fill="x", padx=20, pady=8)
        
        card = tk.Frame(card_borda, bg=cores["bg_card"], padx=15, pady=10)
        card.pack(fill="both", expand=True)
        
        tk.Label(card, text=titulo, font=("Georgia", 12, "bold"),
                bg=cores["bg_card"], fg=cores["texto_principal"]).pack(anchor="w")
        tk.Label(card, text=conteudo, font=("Helvetica", 10),
                bg=cores["bg_card"], fg=cores["texto_secundario"], justify="left").pack(anchor="w", pady=(5, 0))

    def atualizar_tela(self):
        self.criar_interface()