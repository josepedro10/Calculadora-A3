# -*- coding: utf-8 -*-
import tkinter as tk
from theme import ThemeConfig


class TelaHome(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Referências dos widgets
        self.moldura = None
        self.card = None
        self.label_titulo = None
        self.btn_entrar = None
        self.btn_tema = None
        self.btn_sobre = None
        self.frame_funcs = None
        self.frame_botoes_inferiores = None
        self.btn_sobre_borda = None
        self.btn_tema_borda = None
        self.label_funcionalidades = None  
        self.linha_separadora = None      
        
        self.criar_interface()

    def criar_interface(self):
        cores = ThemeConfig.pegar_paleta(self.controller.tema_atual)
        self.configure(bg=cores["bg_janela"])

        card_largura = 1350
        card_altura = 675
        
        self.moldura = tk.Frame(self, bg="#000000", padx=3, pady=3)
        self.moldura.place(relx=0.5, rely=0.5, anchor="center", width=card_largura, height=card_altura)

        self.card = tk.Frame(self.moldura, bg=cores["bg_card"])
        self.card.pack(fill="both", expand=True)

        # Título maior
        self.label_titulo = tk.Label(self.card, text="CALCULADORA", 
                                    font=("Georgia", 48, "bold"),
                                    bg=cores["bg_card"], fg=cores["texto_principal"])
        self.label_titulo.pack(pady=(60, 30))

        # Botão Entrar
        btn_entrar_borda = tk.Frame(self.card, bg="#000000", padx=1, pady=1)
        btn_entrar_borda.pack(pady=20)
        
        self.btn_entrar = tk.Button(btn_entrar_borda, text="Entrar", 
                                   font=("Georgia", 18, "bold"),
                                   bg=cores["bg_botao_primario"], 
                                   fg=cores["texto_botao_primario"],
                                   bd=0, padx=50, pady=12, cursor="hand2",
                                   command=lambda: self.controller.mostrar_tela("CALCULADORA"))
        self.btn_entrar.pack()

        # Linha separadora
        self.linha_separadora = tk.Frame(self.card, height=2, bg="#666666")
        self.linha_separadora.pack(fill="x", padx=80, pady=30)

        # Texto "Funcionalidades:"
        self.label_funcionalidades = tk.Label(self.card, text="Funcionalidades disponíveis:", 
                                              font=("Georgia", 14, "bold"),
                                              bg=cores["bg_card"], fg=cores["texto_principal"])
        self.label_funcionalidades.pack(pady=(10, 15))

        # Frame para as funcionalidades
        self.frame_funcs = tk.Frame(self.card, bg=cores["bg_card"])
        self.frame_funcs.pack(pady=10, padx=80, fill="x")

        # Lista de funcionalidades
        funcionalidades = [
            "🧮 Calculadora completa (+, -, x, ÷, %, √)",
            "⚡ Consumo de energia elétrica",
            "📊 Cálculo de média de valores",
            "⚖️ Índice de Massa Corporal (IMC)",
            "📖 Sobre o projeto"
        ]


        for i, func in enumerate(funcionalidades):
            linha = i // 2
            coluna = i % 2
            
            lbl = tk.Label(self.frame_funcs, text=func, 
                          font=("Helvetica", 12),
                          bg=cores["bg_card"], fg=cores["texto_secundario"],
                          anchor="w")
            lbl.grid(row=linha, column=coluna, padx=20, pady=8, sticky="w")

        # Botoôes inferiores (Sobre e Tema)
        self.frame_botoes_inferiores = tk.Frame(self.card, bg=cores["bg_card"])
        self.frame_botoes_inferiores.pack(side="bottom", fill="x", pady=(0, 20))

        # Botão Sobre (ESQUERDA)
        self.btn_sobre_borda = tk.Frame(self.frame_botoes_inferiores, bg="#000000", padx=1, pady=1)
        self.btn_sobre_borda.pack(side="left", padx=20)
        
        self.btn_sobre = tk.Button(self.btn_sobre_borda, text="ℹ️ Sobre",
                                  font=("Helvetica", 10, "bold"),
                                  bg=cores["bg_botao_primario"],
                                  fg=cores["texto_botao_primario"],
                                  bd=0, width=12, height=1, pady=6, cursor="hand2",
                                  command=lambda: self.controller.mostrar_tela("SOBRE"))
        self.btn_sobre.pack()

        # Botão Tema (DIREITA)
        self.btn_tema_borda = tk.Frame(self.frame_botoes_inferiores, bg="#000000", padx=1, pady=1)
        self.btn_tema_borda.pack(side="right", padx=20)
        
        if self.controller.tema_atual == "DARK":
            texto_tema = "☀️ Tema Claro"
        else:
            texto_tema = "🌙 Tema Escuro"

        self.btn_tema = tk.Button(self.btn_tema_borda, text=texto_tema,
                                 font=("Helvetica", 10, "bold"),
                                 bg=cores["bg_botao_primario"],
                                 fg=cores["texto_botao_primario"],
                                 bd=0, width=12, height=1, pady=6, cursor="hand2",
                                 command=self.controller.alternar_tema)
        self.btn_tema.pack()

    def atualizar_tema(self):
        """Atualiza apenas as cores, sem recriar a tela"""
        cores = ThemeConfig.pegar_paleta(self.controller.tema_atual)
        
        # Atualiza fundo da tela
        self.configure(bg=cores["bg_janela"])
        
        # Atualiza o card
        self.card.configure(bg=cores["bg_card"])
        
        # Atualiza o frame dos botões inferiores
        self.frame_botoes_inferiores.configure(bg=cores["bg_card"])
        
        # Atualiza o título principal
        self.label_titulo.configure(bg=cores["bg_card"], fg=cores["texto_principal"])
        
        # Atualiza o título "Funcionalidades disponíveis"
        self.label_funcionalidades.configure(bg=cores["bg_card"], fg=cores["texto_principal"])
        
        # Atualiza o botão Entrar
        self.btn_entrar.configure(bg=cores["bg_botao_primario"], fg=cores["texto_botao_primario"])
        
        # Atualiza frame das funcionalidades e seus labels
        self.frame_funcs.configure(bg=cores["bg_card"])
        for child in self.frame_funcs.winfo_children():
            if isinstance(child, tk.Label):
                child.configure(bg=cores["bg_card"], fg=cores["texto_secundario"])
        
        # Atualiza o botão Sobre
        self.btn_sobre.configure(bg=cores["bg_botao_primario"], fg=cores["texto_botao_primario"])
        
        # Atualiza o botão de tema
        if self.controller.tema_atual == "DARK":
            texto_tema = "☀️ Tema Claro"
        else:
            texto_tema = "🌙 Tema Escuro"
        
        self.btn_tema.configure(text=texto_tema, 
                                bg=cores["bg_botao_primario"], 
                                fg=cores["texto_botao_primario"])