import tkinter as tk
from theme import ThemeConfig


class TelaSobre(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.cabecalho = None
        self.botoes_aba = []
        self.container = None
        self.canvas = None
        self.scroll = None
        self.frame_scroll = None
        self.cards = []
        
        self.criar_interface()

    def criar_interface(self):
        cores = ThemeConfig.pegar_paleta(self.controller.tema_atual)
        self.configure(bg=cores["bg_janela"])
        
        for widget in self.winfo_children():
            widget.destroy()
        self.cards = []
        
        # Cabeçalho
        self.cabecalho = tk.Frame(self, bg=cores["bg_janela"])
        self.cabecalho.pack(fill="x", padx=30, pady=(20, 0))

        abas = [
            ("Calculadora", "CALCULADORA"),
            ("Consumo", "CONSUMO"),
            ("Média", "MEDIA"),
            ("IMC", "IMC"),
            ("Sobre", "SOBRE")
        ]

        self.botoes_aba = []
        for nome, chave in abas:
            ativa = (chave == "SOBRE")
            cor = cores["texto_principal"] if ativa else cores["texto_secundario"]
            fonte = ("Georgia", 11, "bold" if ativa else "normal")
            btn = tk.Button(self.cabecalho, text=nome, font=fonte, fg=cor,
                           bg=cores["bg_janela"], bd=0, cursor="hand2",
                           command=lambda k=chave: self.controller.mostrar_tela(k))
            btn.pack(side="left", expand=True, fill="x", padx=5)
            self.botoes_aba.append(btn)

        # Container
        self.container = tk.Frame(self, bg=cores["bg_janela"])
        self.container.place(relx=0.5, rely=0.52, anchor="center", width=650, height=600)
        
        # Área com scroll
        self.canvas = tk.Canvas(self.container, bg=cores["bg_janela"], highlightthickness=0)
        self.scroll = tk.Scrollbar(self.container, orient=tk.VERTICAL, command=self.canvas.yview)
        self.frame_scroll = tk.Frame(self.canvas, bg=cores["bg_janela"])
        
        self.frame_scroll.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.frame_scroll, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scroll.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scroll.pack(side="right", fill="y")
        
        # Cards
        self.criar_card(self.frame_scroll, cores, "📱 Calculadora Multifuncional",
                       "Projeto desenvolvido para as disciplinas de Algoritmos de Programação e \nInteração Humano Computador")
        
        self.criar_card(self.frame_scroll, cores, "👥 Desenvolvedores",
                       "• José Pedro Costa Alves Dionsio\n"
                       "• Riquelme Vieira Barbosa\n"
                       "• Gustavo Brito Almeida Santana\n"
                       "• Guilherme Eduardo Figueiredo Pereira\n"
                       "• Pedro Almeida Ribeiro Dobarco\n"
                       "• Caio Santos Fraga\n"
                       "• Maria Clara Dias Matos\n"
                       "• Icaro Carlos Silva Santos")
        
        self.criar_card(self.frame_scroll, cores, "🛠️ Tecnologias",
                       "• Python 3\n• Tkinter (GUI)\n• Biblioteca Math")
        
        self.criar_card(self.frame_scroll, cores, "⚙️ Funcionalidades",
                       "• Calculadora (+, -, x, ÷, %, √)\n• Consumo de energia elétrica\n• Média de valores\n• Cálculo de IMC\n• Tema claro/escuro")
        
        self.criar_card(self.frame_scroll, cores, "🎯 Objetivo",
                       "Criar uma aplicação prática que reúna várias\nferramentas úteis em uma interface moderna.")
        
        self.criar_card(self.frame_scroll, cores, "📅 Ano", "2026")
        
        tk.Frame(self.frame_scroll, height=20, bg=cores["bg_janela"]).pack()
        
        # Botão Home
        home_borda = tk.Frame(self, bg="#000000", padx=1, pady=1)
        home_borda.place(relx=0.05, rely=0.95, anchor="sw")
        tk.Button(home_borda, text="⌂", font=("Helvetica", 14, "bold"),
                 bg=cores["bg_botao_numero"], fg=cores["texto_botao_numero"],
                 bd=0, padx=10, pady=4, cursor="hand2",
                 command=lambda: self.controller.mostrar_tela("HOME")).pack()

    def criar_card(self, parent, cores, titulo, conteudo):
        """Cria um card com título e conteúdo"""
        card_borda = tk.Frame(parent, bg="#000000", padx=1, pady=1)
        card_borda.pack(fill="x", padx=20, pady=8)
        
        card = tk.Frame(card_borda, bg=cores["bg_card"], padx=15, pady=10)
        card.pack(fill="both", expand=True)
        
        lbl_titulo = tk.Label(card, text=titulo, font=("Georgia", 12, "bold"),
                             bg=cores["bg_card"], fg=cores["texto_principal"])
        lbl_titulo.pack(anchor="w")
        
        lbl_conteudo = tk.Label(card, text=conteudo, font=("Helvetica", 10),
                               bg=cores["bg_card"], fg=cores["texto_secundario"], justify="left")
        lbl_conteudo.pack(anchor="w", pady=(5, 0))
        
        # Guarda referências para atualizar depois
        self.cards.append({
            "borda": card_borda,
            "card": card,
            "titulo": lbl_titulo,
            "conteudo": lbl_conteudo
        })

    def atualizar_tema(self):
        """Atualiza as cores sem recriar a tela"""
        cores = ThemeConfig.pegar_paleta(self.controller.tema_atual)
        
        # Atualiza fundo da tela
        self.configure(bg=cores["bg_janela"])
        
        # Atualiza cabeçalho
        self.cabecalho.configure(bg=cores["bg_janela"])
        
        # Atualiza botões do cabeçalho
        abas = ["CALCULADORA", "CONSUMO", "MEDIA", "IMC", "SOBRE"]
        for i, btn in enumerate(self.botoes_aba):
            ativa = (abas[i] == "SOBRE")
            cor = cores["texto_principal"] if ativa else cores["texto_secundario"]
            btn.configure(fg=cor, bg=cores["bg_janela"])
        
        # Atualiza container e canvas
        self.container.configure(bg=cores["bg_janela"])
        self.canvas.configure(bg=cores["bg_janela"])
        self.frame_scroll.configure(bg=cores["bg_janela"])
        
        # Atualiza todos os cards
        for card_info in self.cards:
            card_info["card"].configure(bg=cores["bg_card"])
            card_info["titulo"].configure(bg=cores["bg_card"], fg=cores["texto_principal"])
            card_info["conteudo"].configure(bg=cores["bg_card"], fg=cores["texto_secundario"])
        
        # Atualiza botão home (se existir)
        for widget in self.winfo_children():
            if isinstance(widget, tk.Frame):
                for sub in widget.winfo_children():
                    if isinstance(sub, tk.Button) and sub.cget("text") == "⌂":
                        sub.configure(bg=cores["bg_botao_numero"], fg=cores["texto_botao_numero"])
