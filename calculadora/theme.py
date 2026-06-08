# -*- coding: utf-8 -*-

class ThemeConfig:
    # Fontes
    FONTE_TITULO_GRANDE = ("Georgia", 24, "bold")
    FONTE_TITULO_MEDIO = ("Georgia", 16, "bold")
    FONTE_TEXTO = ("Helvetica", 11)
    FONTE_BOTAO = ("Helvetica", 10, "bold")
    FONTE_DISPLAY = ("Consolas", 28, "bold")
    FONTE_DISPLAY_MEDIO = ("Consolas", 14, "bold")
    
    # TEMA ESCURO
    CORES_ESCURO = {
        "bg_janela": "#1e1e1e",        # Fundo principal
        "bg_card": "#2c2c2c",          # Fundo dos cards
        "texto_principal": "#ECF0F1",  # Texto principal (branco)
        "texto_secundario": "#95A5A6", # Texto secundário (cinza claro)
        "bg_input": "#3c3c3c",         # Fundo dos inputs
        "texto_input": "#ECF0F1",      # Texto dos inputs
        "bg_display": "#2c2c2c",       # Fundo do display
        "texto_display": "#ECF0F1",    # Texto do display
        "bg_botao_numero": "#2c2c2c",  # Botões numéricos
        "texto_botao_numero": "#ECF0F1",
        "bg_botao_cinza": "#7F8C8D",   # Botões AC, +/-, %
        "texto_botao_cinza": "#FFFFFF",
        "bg_botao_laranja": "#E67E22", # Botões de operação
        "texto_botao_laranja": "#FFFFFF",
        "bg_botao_primario": "#000000",# Botão Entrar e Sobre
        "texto_botao_primario": "#FFFFFF",
        "bg_botao_acao": "#D35400",    # Botão Calcular
        "texto_botao_acao": "#FFFFFF",
        "cor_sucesso": "#27AE60",      # Verde
        "cor_perigo": "#E74C3C",       # Vermelho
        "cor_alerta": "#F39C12"        # Laranja
    }
    
    # TEMA CLARO (TODAS AS CORES CORRIGIDAS)
    CORES_CLARO = {
        "bg_janela": "#F0F0F0",        # Fundo principal (cinza claro)
        "bg_card": "#FFFFFF",          # Fundo dos cards (branco)
        "texto_principal": "#2C3E50",  # Texto principal (azul escuro)
        "texto_secundario": "#7F8C8D", # Texto secundário (cinza)
        "bg_input": "#FFFFFF",         # Fundo dos inputs (branco)
        "texto_input": "#2C3E50",      # Texto dos inputs (azul escuro)
        "bg_display": "#FFFFFF",       # Fundo do display (branco)
        "texto_display": "#2C3E50",    # Texto do display (azul escuro)
        "bg_botao_numero": "#F0F0F0",  # Botões numéricos (cinza claro)
        "texto_botao_numero": "#2C3E50",
        "bg_botao_cinza": "#95A5A6",   # Botões AC, +/-, % (cinza)
        "texto_botao_cinza": "#FFFFFF",
        "bg_botao_laranja": "#E67E22", # Botões de operação (laranja)
        "texto_botao_laranja": "#FFFFFF",
        "bg_botao_primario": "#000000",# Botão Entrar e Sobre (preto)
        "texto_botao_primario": "#FFFFFF",
        "bg_botao_acao": "#000000",    # Botão Calcular (preto)
        "texto_botao_acao": "#FFFFFF",
        "cor_sucesso": "#27AE60",      # Verde
        "cor_perigo": "#E74C3C",       # Vermelho
        "cor_alerta": "#F39C12"        # Laranja
    }

    @classmethod
    def pegar_paleta(cls, modo: str) -> dict:
        if modo == "DARK":
            return cls.CORES_ESCURO
        return cls.CORES_CLARO