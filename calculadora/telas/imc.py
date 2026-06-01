# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
from theme import ThemeConfig
from calculations import calcular_imc


class TelaIMC(tk.Frame):
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
            ativa = (chave == "IMC")
            cor = cores["texto_principal"] if ativa else cores["texto_secundario"]
            fonte = ("Georgia", 11, "bold" if ativa else "normal")
            btn = tk.Button(cabecalho, text=nome, font=fonte, fg=cor,
                           bg=cores["bg_janela"], bd=0, cursor="hand2",
                           command=lambda k=chave: self.controller.mostrar_tela(k))
            btn.pack(side="left", expand=True, fill="x", padx=5)

        # Container
        container = tk.Frame(self, bg=cores["bg_janela"])
        container.place(relx=0.5, rely=0.52, anchor="center", width=400, height=450)
        
        self.peso = tk.StringVar()
        self.altura = tk.StringVar()
        
        # Peso
        tk.Label(container, text="Peso (kg)", font=ThemeConfig.FONTE_BOTAO,
                bg=cores["bg_janela"], fg=cores["texto_principal"]).pack(fill="x", pady=(15, 3))
        input_peso = tk.Frame(container, bg="#000000", padx=1, pady=1)
        input_peso.pack(fill="x", pady=(0, 15))
        tk.Entry(input_peso, textvariable=self.peso, font=ThemeConfig.FONTE_TEXTO,
                bg=cores["bg_input"], fg=cores["texto_input"], bd=0,
                insertbackground=cores["texto_input"], justify="center").pack(fill="x", ipady=8)
        
        # Altura
        tk.Label(container, text="Altura (m)", font=ThemeConfig.FONTE_BOTAO,
                bg=cores["bg_janela"], fg=cores["texto_principal"]).pack(fill="x", pady=(5, 3))
        input_altura = tk.Frame(container, bg="#000000", padx=1, pady=1)
        input_altura.pack(fill="x", pady=(0, 20))
        tk.Entry(input_altura, textvariable=self.altura, font=ThemeConfig.FONTE_TEXTO,
                bg=cores["bg_input"], fg=cores["texto_input"], bd=0,
                insertbackground=cores["texto_input"], justify="center").pack(fill="x", ipady=8)
        
        # Botão
        btn_calc = tk.Frame(container, bg="#000000", padx=1, pady=1)
        btn_calc.pack(pady=(5, 20))
        tk.Button(btn_calc, text="Calcular IMC", font=("Georgia", 11, "bold"),
                 bg=cores["bg_botao_acao"], fg=cores["texto_botao_acao"],
                 bd=0, padx=35, pady=6, cursor="hand2",
                 command=self.calcular).pack()
        
        # Resultado
        self.valor_imc = tk.StringVar(value="--.--")
        self.status_imc = tk.StringVar(value="---")
        
        res_borda = tk.Frame(container, bg="#000000", padx=1, pady=1)
        res_borda.pack(fill="x")
        res_frame = tk.Frame(res_borda, bg=cores["bg_display"], pady=15)
        res_frame.pack(fill="x")
        
        tk.Label(res_frame, text="Seu IMC é:", font=("Helvetica", 8, "bold"),
                bg=cores["bg_display"], fg=cores["texto_display"]).pack()
        
        self.lbl_valor = tk.Label(res_frame, textvariable=self.valor_imc, font=("Georgia", 28, "bold"),
                                 bg=cores["bg_display"], fg=cores["texto_display"])
        self.lbl_valor.pack()
        
        self.lbl_status = tk.Label(res_frame, textvariable=self.status_imc, font=("Georgia", 10, "bold"),
                                  bg=cores["bg_display"])
        self.lbl_status.pack()
        
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
            p = self.peso.get().strip()
            a = self.altura.get().strip()
            
            if not p or not a:
                raise ValueError("Preencha peso e altura!")
            
            peso_val = float(p.replace(",", "."))
            altura_val = float(a.replace(",", "."))
            
            imc, classificacao, cor_tipo = calcular_imc(peso_val, altura_val)
            cores = ThemeConfig.pegar_paleta(self.controller.tema_atual)
            
            cores_map = {
                "sucesso": cores["cor_sucesso"],
                "alerta": cores["cor_alerta"],
                "perigo": cores["cor_perigo"]
            }
            
            self.valor_imc.set(f"{imc:.2f}".replace(".", ","))
            self.status_imc.set(classificacao)
            self.lbl_status.config(fg=cores_map.get(cor_tipo, cores["texto_principal"]))
            
        except ValueError as e:
            self.valor_imc.set("Erro")
            self.status_imc.set("---")
            messagebox.showerror("Erro", str(e))
        except:
            self.valor_imc.set("Erro")
            self.status_imc.set("---")
            messagebox.showerror("Erro", "Valores inválidos.")