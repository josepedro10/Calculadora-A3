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

        # Container principal
        container = tk.Frame(self, bg=cores["bg_janela"])
        container.place(relx=0.5, rely=0.52, anchor="center", width=500, height=620)

        # Título
        tk.Label(container, text="Calculadora de Média", 
                font=("Georgia", 20, "bold"),
                bg=cores["bg_janela"], fg=cores["texto_principal"]).pack(pady=(20, 5))
        
        tk.Label(container, text="Adicione quantos valores quiser", 
                font=("Helvetica", 11),
                bg=cores["bg_janela"], fg=cores["texto_secundario"]).pack(pady=(0, 20))

        # Área dos campos de valores (com scroll)
        frame_campos = tk.Frame(container, bg=cores["bg_janela"])
        frame_campos.pack(fill="both", expand=True, padx=30, pady=10)

        # Canvas para scroll
        canvas = tk.Canvas(frame_campos, bg=cores["bg_janela"], highlightthickness=0)
        scrollbar = tk.Scrollbar(frame_campos, orient=tk.VERTICAL, command=canvas.yview)
        self.frame_valores = tk.Frame(canvas, bg=cores["bg_janela"])

        self.frame_valores.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.frame_valores, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Frame para os botões (centralizado)
        frame_botoes = tk.Frame(container, bg=cores["bg_janela"])
        frame_botoes.pack(pady=15)

        # Botão Adicionar Valor
        btn_add_borda = tk.Frame(frame_botoes, bg="#000000", padx=1, pady=1)
        btn_add_borda.pack(side="left", padx=10)
        
        btn_adicionar = tk.Button(btn_add_borda, text="+ Adicionar Valor", 
                                 font=("Georgia", 11, "bold"),
                                 bg=cores["cor_sucesso"], fg="#FFFFFF",
                                 bd=0, padx=20, pady=8, cursor="hand2",
                                 command=self.adicionar_campo)
        btn_adicionar.pack()

        # Botão Calcular Média
        btn_calc_borda = tk.Frame(frame_botoes, bg="#000000", padx=1, pady=1)
        btn_calc_borda.pack(side="left", padx=10)
        
        btn_calcular = tk.Button(btn_calc_borda, text="Calcular Média", 
                                font=("Georgia", 11, "bold"),
                                bg=cores["bg_botao_acao"], fg=cores["texto_botao_acao"],
                                bd=0, padx=20, pady=8, cursor="hand2",
                                command=self.calcular)
        btn_calcular.pack()

        # Área de resultado
        self.resultado_var = tk.StringVar(value="---")
        
        res_borda = tk.Frame(container, bg="#000000", padx=1, pady=1)
        res_borda.pack(fill="x", padx=30, pady=(10, 10))
        
        res_frame = tk.Frame(res_borda, bg=cores["bg_display"], pady=15)
        res_frame.pack(fill="x")
        
        tk.Label(res_frame, text="RESULTADO", font=("Helvetica", 9, "bold"),
                bg=cores["bg_display"], fg=cores["texto_secundario"]).pack()
        
        self.lbl_resultado = tk.Label(res_frame, textvariable=self.resultado_var, 
                                      font=("Georgia", 24, "bold"),
                                      bg=cores["bg_display"], fg=cores["cor_sucesso"])
        self.lbl_resultado.pack()

        # Rodapé com informações (POR, PTB2, Data)
        frame_rodape = tk.Frame(container, bg=cores["bg_janela"])
        frame_rodape.pack(fill="x", pady=(15, 10))
        
        # Centralizar os textos do rodapé
        tk.Label(frame_rodape, text="POR", font=("Helvetica", 9, "bold"),
                bg=cores["bg_janela"], fg=cores["texto_secundario"]).pack(side="left", padx=20)
        
        tk.Label(frame_rodape, text="PTB2", font=("Helvetica", 9, "bold"),
                bg=cores["bg_janela"], fg=cores["texto_secundario"]).pack(side="left", padx=20)
        
        tk.Label(frame_rodape, text="01/06/2026", font=("Helvetica", 9, "bold"),
                bg=cores["bg_janela"], fg=cores["texto_secundario"]).pack(side="right", padx=20)

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

    def adicionar_campo(self):
        """Adiciona um novo campo de entrada dinamicamente"""
        idx = len(self.lista_entries) + 1
        cores = ThemeConfig.pegar_paleta(self.controller.tema_atual)
        
        # Frame do campo
        frame_campo = tk.Frame(self.frame_valores, bg=self.frame_valores["bg"])
        frame_campo.pack(fill="x", pady=5)

        # Label com borda preta
        label_borda = tk.Frame(frame_campo, bg="#000000", padx=1, pady=1)
        label_borda.pack(side="left", padx=(0, 10))
        
        label = tk.Label(label_borda, text=f"Valor {idx}:", 
                        font=("Helvetica", 11, "bold"),
                        bg=cores["bg_botao_primario"], fg=cores["texto_botao_primario"],
                        width=10, padx=5, pady=5)
        label.pack()

        # Campo de entrada com borda preta
        entry_borda = tk.Frame(frame_campo, bg="#000000", padx=1, pady=1)
        entry_borda.pack(side="left", expand=True, fill="x")
        
        entry = tk.Entry(entry_borda, font=("Helvetica", 11), 
                        bg=cores["bg_input"], fg=cores["texto_input"],
                        bd=0, insertbackground=cores["texto_input"],
                        justify="center")
        entry.pack(fill="x", ipady=5, padx=5, pady=2)

        # Botão remover com borda preta
        remover_borda = tk.Frame(frame_campo, bg="#000000", padx=1, pady=1)
        remover_borda.pack(side="right", padx=(10, 0))
        
        btn_remover = tk.Button(remover_borda, text="✖", font=("Helvetica", 10, "bold"),
                               bg=cores["cor_perigo"], fg="#FFFFFF", bd=0,
                               padx=8, pady=4, cursor="hand2",
                               command=lambda: self.remover_campo(frame_campo, entry))
        btn_remover.pack()

        self.lista_entries.append(entry)
        self.renomear_labels()

    def remover_campo(self, frame_campo, entry):
        """Remove um campo de entrada"""
        if entry in self.lista_entries:
            self.lista_entries.remove(entry)
        frame_campo.destroy()
        self.renomear_labels()

    def renomear_labels(self):
        """Renomeia os labels dos campos após remoção"""
        for i, entry in enumerate(self.lista_entries):
            parent = entry.master.master
            for child in parent.winfo_children():
                if isinstance(child, tk.Frame):
                    for subchild in child.winfo_children():
                        if isinstance(subchild, tk.Label) and "Valor" in subchild.cget("text"):
                            subchild.config(text=f"Valor {i + 1}:")

    def calcular(self):
        """Calcula a média dos valores inseridos"""
        try:
            valores = []
            for entry in self.lista_entries:
                valor = entry.get().strip()
                if valor:
                    valores.append(valor)
            
            if not valores:
                raise ValueError("Adicione pelo menos um valor!")
            
            media = calcular_media(valores)
            self.resultado_var.set(f"{media:.2f}")
            
            # Muda a cor do resultado para verde
            cores = ThemeConfig.pegar_paleta(self.controller.tema_atual)
            self.lbl_resultado.configure(fg=cores["cor_sucesso"])
            
        except ValueError as e:
            self.resultado_var.set("Erro!")
            self.lbl_resultado.configure(fg="#E74C3C")  # Vermelho
            messagebox.showerror("Erro", str(e))
        except Exception:
            self.resultado_var.set("Erro!")
            self.lbl_resultado.configure(fg="#E74C3C")  # Vermelho
            messagebox.showerror("Erro", "Valores inválidos. Use números.")

    def atualizar_tema(self):
        """Atualiza as cores sem recriar a tela"""
        self.criar_interface()