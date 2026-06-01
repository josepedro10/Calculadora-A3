# -*- coding: utf-8 -*-
import tkinter as tk
import math
from theme import ThemeConfig


class TelaCalculadora(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.expressao = "0"
        self.novo_numero = False
        
        # Referências
        self.cabecalho = None
        self.botoes_aba = []
        self.calc_container = None
        self.visor_borda = None
        self.lbl_display = None
        self.grid_botoes = None
        self.botoes = []
        self.home_borda = None
        self.btn_home = None
        
        self.criar_interface()

    def criar_interface(self):
        cores = ThemeConfig.pegar_paleta(self.controller.tema_atual)
        self.configure(bg=cores["bg_janela"])
        
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
            ativa = (chave == "CALCULADORA")
            cor = cores["texto_principal"] if ativa else cores["texto_secundario"]
            fonte = ("Georgia", 11, "bold" if ativa else "normal")
            btn = tk.Button(self.cabecalho, text=nome, font=fonte, fg=cor,
                           bg=cores["bg_janela"], bd=0, cursor="hand2",
                           command=lambda k=chave: self.controller.mostrar_tela(k))
            btn.pack(side="left", expand=True, fill="x", padx=5)
            self.botoes_aba.append(btn)

        # Container da calculadora
        self.calc_container = tk.Frame(self, bg=cores["bg_janela"])
        self.calc_container.place(relx=0.5, rely=0.52, anchor="center", width=400, height=520)

        # Visor
        self.visor_borda = tk.Frame(self.calc_container, bg="#000000", padx=1, pady=1)
        self.visor_borda.pack(fill="x", pady=(10, 10))
        
        self.display_var = tk.StringVar(value=self.expressao)
        self.lbl_display = tk.Label(self.visor_borda, textvariable=self.display_var,
                                   font=ThemeConfig.FONTE_DISPLAY,
                                   bg=cores["bg_display"], fg=cores["texto_display"],
                                   anchor="e", padx=15, pady=15)
        self.lbl_display.pack(fill="x")

        # Botões
        self.grid_botoes = tk.Frame(self.calc_container, bg=cores["bg_janela"])
        self.grid_botoes.pack(fill="both", expand=True)

        for c in range(4):
            self.grid_botoes.columnconfigure(c, weight=1, minsize=80)
        for r in range(6):
            self.grid_botoes.rowconfigure(r, weight=1, minsize=65)

        botoes_config = [
            ("AC", "cinza", 0, 0), ("+/-", "cinza", 0, 1), ("%", "cinza", 0, 2), ("÷", "laranja", 0, 3),
            ("7", "numero", 1, 0), ("8", "numero", 1, 1), ("9", "numero", 1, 2), ("x", "laranja", 1, 3),
            ("4", "numero", 2, 0), ("5", "numero", 2, 1), ("6", "numero", 2, 2), ("-", "laranja", 2, 3),
            ("1", "numero", 3, 0), ("2", "numero", 3, 1), ("3", "numero", 3, 2), ("+", "laranja", 3, 3),
            ("0", "numero", 4, 0), (",", "numero", 4, 1), ("=", "laranja", 4, 2), ("√", "cinza", 4, 3),
            ("(", "numero", 5, 0), (")", "numero", 5, 1)
        ]

        self.botoes = []
        for texto, tipo, linha, coluna in botoes_config:
            if tipo == "numero":
                bg_cor = cores["bg_botao_numero"]
                fg_cor = cores["texto_botao_numero"]
            elif tipo == "cinza":
                bg_cor = cores["bg_botao_cinza"]
                fg_cor = cores["texto_botao_cinza"]
            else:
                bg_cor = cores["bg_botao_laranja"]
                fg_cor = cores["texto_botao_laranja"]

            btn_borda = tk.Frame(self.grid_botoes, bg="#000000", padx=1, pady=1)
            btn_borda.grid(row=linha, column=coluna, padx=3, pady=3, sticky="nsew")

            btn = tk.Button(btn_borda, text=texto,
                           font=("Georgia", 16, "bold") if tipo in ["numero", "laranja"] else ("Helvetica", 16, "bold"),
                           bg=bg_cor, fg=fg_cor, bd=0, cursor="hand2",
                           command=lambda t=texto: self.clique_botao(t))
            btn.pack(fill="both", expand=True)
            self.botoes.append(btn)

        # Botão Home
        self.home_borda = tk.Frame(self, bg="#000000", padx=1, pady=1)
        self.home_borda.place(relx=0.05, rely=0.95, anchor="sw")
        self.btn_home = tk.Button(self.home_borda, text="⌂", font=("Helvetica", 14, "bold"),
                                 bg=cores["bg_botao_numero"], fg=cores["texto_botao_numero"],
                                 bd=0, padx=10, pady=4, cursor="hand2",
                                 command=lambda: self.controller.mostrar_tela("HOME"))
        self.btn_home.pack()

    def atualizar_tema(self):
        """Atualiza as cores sem recriar a tela"""
        cores = ThemeConfig.pegar_paleta(self.controller.tema_atual)
        
        # Atualiza fundo
        self.configure(bg=cores["bg_janela"])
        self.cabecalho.configure(bg=cores["bg_janela"])
        self.calc_container.configure(bg=cores["bg_janela"])
        self.grid_botoes.configure(bg=cores["bg_janela"])
        
        # Atualiza botões do cabeçalho
        abas = ["CALCULADORA", "CONSUMO", "MEDIA", "IMC", "SOBRE"]
        for i, btn in enumerate(self.botoes_aba):
            ativa = (abas[i] == "CALCULADORA")
            cor = cores["texto_principal"] if ativa else cores["texto_secundario"]
            btn.configure(fg=cor, bg=cores["bg_janela"])
        
        # Atualiza visor
        self.lbl_display.configure(bg=cores["bg_display"], fg=cores["texto_display"])
        
        # Atualiza botões da calculadora
        tipos_botoes = [
            "cinza", "cinza", "cinza", "laranja",
            "numero", "numero", "numero", "laranja",
            "numero", "numero", "numero", "laranja",
            "numero", "numero", "numero", "laranja",
            "numero", "numero", "laranja", "cinza",
            "numero", "numero"
        ]
        
        for i, btn in enumerate(self.botoes):
            tipo = tipos_botoes[i] if i < len(tipos_botoes) else "numero"
            if tipo == "numero":
                btn.configure(bg=cores["bg_botao_numero"], fg=cores["texto_botao_numero"])
            elif tipo == "cinza":
                btn.configure(bg=cores["bg_botao_cinza"], fg=cores["texto_botao_cinza"])
            else:
                btn.configure(bg=cores["bg_botao_laranja"], fg=cores["texto_botao_laranja"])
        
        # Atualiza botão home
        self.btn_home.configure(bg=cores["bg_botao_numero"], fg=cores["texto_botao_numero"])

    def clique_botao(self, valor):
        # ... (mesmo código de antes)
        if valor == "AC":
            self.expressao = "0"
            self.novo_numero = False
        elif valor == "+/-":
            if self.expressao != "0" and self.expressao != "Erro":
                if self.expressao.startswith("-"):
                    self.expressao = self.expressao[1:]
                else:
                    self.expressao = "-" + self.expressao
        elif valor == "%":
            try:
                expr = self.expressao.replace(",", ".")
                resultado = float(eval(expr)) / 100.0
                self.expressao = str(resultado).replace(".", ",")
            except:
                self.expressao = "Erro"
        elif valor == "√":
            try:
                expr = self.expressao.replace(",", ".")
                resultado = math.sqrt(float(eval(expr)))
                if resultado == int(resultado):
                    resultado = int(resultado)
                else:
                    resultado = round(resultado, 5)
                self.expressao = str(resultado).replace(".", ",")
            except:
                self.expressao = "Erro"
        elif valor == "=":
            try:
                expr = self.expressao.replace(",", ".").replace(" ", "")
                resultado = eval(expr, {"__builtins__": None, "math": math}, {})
                if isinstance(resultado, float):
                    if resultado.is_integer():
                        resultado = int(resultado)
                    else:
                        resultado = round(resultado, 5)
                self.expressao = str(resultado).replace(".", ",")
                self.novo_numero = True
            except:
                self.expressao = "Erro"
            self.atualizar_display()
            return
        elif valor in ["+", "-", "x", "÷"]:
            if self.novo_numero:
                self.novo_numero = False
            if self.expressao == "Erro":
                self.expressao = "0"
            if valor == "+":
                self.expressao += " + "
            elif valor == "-":
                self.expressao += " - "
            elif valor == "x":
                self.expressao += " * "
            elif valor == "÷":
                self.expressao += " / "
        else:
            if self.expressao == "0" or self.novo_numero or self.expressao == "Erro":
                if valor == ",":
                    self.expressao = "0,"
                else:
                    self.expressao = valor
                self.novo_numero = False
            else:
                self.expressao += valor
        
        self.atualizar_display()

    def atualizar_display(self):
        texto = self.expressao
        if len(texto) > 20:
            texto = texto[:19] + "…"
        self.display_var.set(texto)