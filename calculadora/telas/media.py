# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
from theme import ThemeConfig
from calculations import calcular_media


class TelaMedia(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.lista_entries = []
        self.criar_interface()

    def criar_interface(self):
        cores = ThemeConfig.pegar_paleta(self.controller.tema_atual)
        self.configure(bg=cores["bg_janela"])
        
        for widget in self.winfo_children():
            widget.destroy()
        self.lista_entries = []
        
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
            ativa = (chave == "MEDIA")
            cor = cores["texto_principal"] if ativa else cores["texto_secundario"]
            fonte = ("Georgia", 11, "bold" if ativa else "normal")
            btn = tk.Button(cabecalho, text=nome, font=fonte, fg=cor,
                           bg=cores["bg_janela"], bd=0, cursor="hand2",
                           command=lambda k=chave: self.controller.mostrar_tela(k))
            btn.pack(side="left", expand=True, fill="x", padx=5)

        # Container
        container = tk.Frame(self, bg=cores["bg_janela"])
        container.place(relx=0.5, rely=0.52, anchor="center", width=400, height=520)
        
        tk.Label(container, text="Calculadora de Média", 
                font=ThemeConfig.FONTE_TITULO_MEDIO,
                bg=cores["bg_janela"], fg=cores["texto_principal"]).pack(pady=(10, 5))
        tk.Label(container, text="Adicione quantos valores quiser", 
                font=ThemeConfig.FONTE_TEXTO,
                bg=cores["bg_janela"], fg=cores["texto_secundario"]).pack(pady=(0, 15))
        
        # Frame com scroll
        frame_scroll = tk.Frame(container, bg=cores["bg_janela"])
        frame_scroll.pack(fill="both", expand=True, padx=20)
        
        canvas = tk.Canvas(frame_scroll, bg=cores["bg_janela"], highlightthickness=0)
        scroll = tk.Scrollbar(frame_scroll, orient=tk.VERTICAL, command=canvas.yview)
        self.frame_notas = tk.Frame(canvas, bg=cores["bg_janela"])
        
        self.frame_notas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.frame_notas, anchor="nw")
        canvas.configure(yscrollcommand=scroll.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        
        # Botões
        frame_botoes = tk.Frame(container, bg=cores["bg_janela"])
        frame_botoes.pack(pady=15)
        
        btn_add = tk.Frame(frame_botoes, bg="#000000", padx=1, pady=1)
        btn_add.pack(side="left", padx=5)
        tk.Button(btn_add, text="+ Adicionar Valor", font=("Georgia", 10, "bold"),
                 bg=cores["cor_sucesso"], fg="#FFFFFF", bd=0, padx=15, pady=5, cursor="hand2",
                 command=self.adicionar_campo).pack()
        
        btn_calc = tk.Frame(frame_botoes, bg="#000000", padx=1, pady=1)
        btn_calc.pack(side="left", padx=5)
        tk.Button(btn_calc, text="Calcular Média", font=("Georgia", 10, "bold"),
                 bg=cores["bg_botao_acao"], fg=cores["texto_botao_acao"], bd=0, padx=15, pady=5,
                 cursor="hand2", command=self.calcular).pack()
        
        # Resultado
        self.resultado_var = tk.StringVar(value="Média: ---")
        res_borda = tk.Frame(container, bg="#000000", padx=1, pady=1)
        res_borda.pack(fill="x", padx=20, pady=(10, 15))
        res_frame = tk.Frame(res_borda, bg=cores["bg_display"], pady=10)
        res_frame.pack(fill="x")
        tk.Label(res_frame, textvariable=self.resultado_var, font=("Georgia", 14, "bold"),
                bg=cores["bg_display"], fg=cores["texto_display"]).pack()
        
        # Botão Home
        home_borda = tk.Frame(self, bg="#000000", padx=1, pady=1)
        home_borda.place(relx=0.05, rely=0.95, anchor="sw")
        tk.Button(home_borda, text="⌂", font=("Helvetica", 14, "bold"),
                 bg=cores["bg_botao_numero"], fg=cores["texto_botao_numero"],
                 bd=0, padx=10, pady=4, cursor="hand2",
                 command=lambda: self.controller.mostrar_tela("HOME")).pack()
        
        # Adiciona 2 campos iniciais
        for _ in range(2):
            self.adicionar_campo()

    def atualizar_tela(self):
        self.criar_interface()

    def adicionar_campo(self):
        idx = len(self.lista_entries)
        cores = ThemeConfig.pegar_paleta(self.controller.tema_atual)
        
        frame = tk.Frame(self.frame_notas, bg=self.frame_notas["bg"])
        frame.pack(fill="x", pady=3)
        
        tk.Label(frame, text=f"Valor {idx + 1}:", font=ThemeConfig.FONTE_BOTAO,
                bg=frame["bg"], fg=cores["texto_principal"]).pack(side="left", padx=5)
        
        entry = tk.Entry(frame, font=ThemeConfig.FONTE_TEXTO, width=15, justify="center")
        entry.pack(side="left", padx=5, expand=True, fill="x")
        
        tk.Button(frame, text="✖", font=("Helvetica", 8, "bold"), bg="#E74C3C", fg="white",
                 bd=0, padx=5, cursor="hand2",
                 command=lambda: self.remover_campo(frame, entry)).pack(side="right", padx=5)
        
        self.lista_entries.append(entry)

    def remover_campo(self, frame, entry):
        if entry in self.lista_entries:
            self.lista_entries.remove(entry)
        frame.destroy()
        
        for i, e in enumerate(self.lista_entries):
            parent = e.master
            for child in parent.winfo_children():
                if isinstance(child, tk.Label) and "Valor" in child.cget("text"):
                    child.config(text=f"Valor {i + 1}:")

    def calcular(self):
        try:
            valores = [e.get().strip() for e in self.lista_entries if e.get().strip()]
            if not valores:
                raise ValueError("Adicione pelo menos um valor!")
            
            media = calcular_media(valores)
            self.resultado_var.set(f"Média: {media:.2f}")
        except ValueError as e:
            self.resultado_var.set("Média: Erro!")
            messagebox.showerror("Erro", str(e))
        except:
            self.resultado_var.set("Média: Erro!")
            messagebox.showerror("Erro", "Valores inválidos.")