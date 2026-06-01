# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
from theme import ThemeConfig
from calculations import calcular_consumo


class TelaConsumo(tk.Frame):
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
            ativa = (chave == "CONSUMO")
            cor = cores["texto_principal"] if ativa else cores["texto_secundario"]
            fonte = ("Georgia", 11, "bold" if ativa else "normal")
            btn = tk.Button(cabecalho, text=nome, font=fonte, fg=cor,
                           bg=cores["bg_janela"], bd=0, cursor="hand2",
                           command=lambda k=chave: self.controller.mostrar_tela(k))
            btn.pack(side="left", expand=True, fill="x", padx=5)

        # Container principal
        container = tk.Frame(self, bg=cores["bg_janela"])
        container.place(relx=0.5, rely=0.52, anchor="center", width=420, height=520)

        self.potencia = tk.StringVar()
        self.horas = tk.StringVar()
        self.dias = tk.StringVar()
        self.preco = tk.StringVar(value="0.75")

        # Potência
        tk.Label(container, text="Potência do aparelho (W)", 
                font=ThemeConfig.FONTE_BOTAO,
                bg=cores["bg_janela"], fg=cores["texto_principal"]).pack(fill="x", pady=(5, 3))
        input_pot = tk.Frame(container, bg="#000000", padx=1, pady=1)
        input_pot.pack(fill="x", pady=(0, 10))
        tk.Entry(input_pot, textvariable=self.potencia, font=ThemeConfig.FONTE_TEXTO,
                bg=cores["bg_input"], fg=cores["texto_input"], bd=0,
                insertbackground=cores["texto_input"], justify="center").pack(fill="x", ipady=8)

        # Horas
        tk.Label(container, text="Horas de uso por dia", 
                font=ThemeConfig.FONTE_BOTAO,
                bg=cores["bg_janela"], fg=cores["texto_principal"]).pack(fill="x", pady=(5, 3))
        input_horas = tk.Frame(container, bg="#000000", padx=1, pady=1)
        input_horas.pack(fill="x", pady=(0, 10))
        tk.Entry(input_horas, textvariable=self.horas, font=ThemeConfig.FONTE_TEXTO,
                bg=cores["bg_input"], fg=cores["texto_input"], bd=0,
                insertbackground=cores["texto_input"], justify="center").pack(fill="x", ipady=8)

        # Dias
        tk.Label(container, text="Dias por mês", 
                font=ThemeConfig.FONTE_BOTAO,
                bg=cores["bg_janela"], fg=cores["texto_principal"]).pack(fill="x", pady=(5, 3))
        input_dias = tk.Frame(container, bg="#000000", padx=1, pady=1)
        input_dias.pack(fill="x", pady=(0, 10))
        tk.Entry(input_dias, textvariable=self.dias, font=ThemeConfig.FONTE_TEXTO,
                bg=cores["bg_input"], fg=cores["texto_input"], bd=0,
                insertbackground=cores["texto_input"], justify="center").pack(fill="x", ipady=8)

        # Preço
        tk.Label(container, text="Preço do kWh (R$)", 
                font=ThemeConfig.FONTE_BOTAO,
                bg=cores["bg_janela"], fg=cores["texto_principal"]).pack(fill="x", pady=(5, 3))
        input_preco = tk.Frame(container, bg="#000000", padx=1, pady=1)
        input_preco.pack(fill="x", pady=(0, 15))
        tk.Entry(input_preco, textvariable=self.preco, font=ThemeConfig.FONTE_TEXTO,
                bg=cores["bg_input"], fg=cores["texto_input"], bd=0,
                insertbackground=cores["texto_input"], justify="center").pack(fill="x", ipady=8)

        # Botão
        btn_calc = tk.Frame(container, bg="#000000", padx=1, pady=1)
        btn_calc.pack(pady=(5, 15))
        tk.Button(btn_calc, text="Calcular Consumo", font=("Georgia", 11, "bold"),
                 bg=cores["bg_botao_acao"], fg=cores["texto_botao_acao"],
                 bd=0, padx=25, pady=6, cursor="hand2",
                 command=self.calcular).pack()

        # Resultado
        self.resultado_var = tk.StringVar(value="Aguardando cálculo...")
        res_borda = tk.Frame(container, bg="#000000", padx=1, pady=1)
        res_borda.pack(fill="x")
        res_frame = tk.Frame(res_borda, bg=cores["bg_display"], pady=12)
        res_frame.pack(fill="x")
        
        tk.Label(res_frame, text="RESULTADO:", font=("Helvetica", 8, "bold"),
                bg=cores["bg_display"], fg=cores["texto_display"]).pack()
        tk.Label(res_frame, textvariable=self.resultado_var, font=("Georgia", 11, "bold"),
                bg=cores["bg_display"], fg=cores["texto_display"]).pack()

        # Botão Home
        home_borda = tk.Frame(self, bg="#000000", padx=1, pady=1)
        home_borda.place(relx=0.05, rely=0.95, anchor="sw")
        tk.Button(home_borda, text="⌂", font=("Helvetica", 14, "bold"),
                 bg=cores["bg_botao_numero"], fg=cores["texto_botao_numero"],
                 bd=0, padx=10, pady=4, cursor="hand2",
                 command=lambda: self.controller.mostrar_tela("HOME")).pack()

    def atualizar_tela(self):
        self.criar_interface()

    def calcular(self):
        try:
            p = self.potencia.get().strip()
            h = self.horas.get().strip()
            d = self.dias.get().strip()
            preco = self.preco.get().strip()
            
            if not p or not h or not d:
                raise ValueError("Preencha todos os campos!")
            
            potencia_val = float(p.replace(",", "."))
            horas_val = float(h.replace(",", "."))
            dias_val = int(d)
            preco_val = float(preco.replace(",", "."))
            
            resultado = calcular_consumo(potencia_val, horas_val, dias_val, preco_val)
            
            self.resultado_var.set(
                f"Consumo: {resultado['kwh_mes']} kWh/mês\n"
                f"Custo mensal: R$ {resultado['custo_mensal']:.2f}\n"
                f"Custo diário: R$ {resultado['custo_diario']:.2f}"
            )
        except ValueError as e:
            self.resultado_var.set("Erro nos dados!")
            messagebox.showerror("Erro", str(e))
        except:
            self.resultado_var.set("Erro!")
            messagebox.showerror("Erro", "Valores inválidos.")