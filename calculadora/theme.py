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
        "bg_janela": "#1e1e1e",
        "bg_card": "#2c2c2c",
        "texto_principal": "#ECF0F1",
        "texto_secundario": "#95A5A6",
        "bg_input": "#3c3c3c",
        "texto_input": "#ECF0F1",
        "bg_display": "#2c2c2c",
        "texto_display": "#ECF0F1",
        "bg_botao_numero": "#2c2c2c",
        "texto_botao_numero": "#ECF0F1",
        "bg_botao_cinza": "#7F8C8D",
        "texto_botao_cinza": "#FFFFFF",
        "bg_botao_laranja": "#E67E22",
        "texto_botao_laranja": "#FFFFFF",
        "bg_botao_primario": "#000000",
        "texto_botao_primario": "#FFFFFF",
        "bg_botao_acao": "#D35400",
        "texto_botao_acao": "#FFFFFF",
        "cor_sucesso": "#27AE60",
        "cor_perigo": "#E74C3C",
        "cor_alerta": "#F39C12"
    }
    
    # TEMA CLARO
    CORES_CLARO = {
        "bg_janela": "#F0F0F0",
        "bg_card": "#FFFFFF",
        "texto_principal": "#2C3E50",
        "texto_secundario": "#7F8C8D",
        "bg_input": "#FFFFFF",
        "texto_input": "#2C3E50",
        "bg_display": "#FFFFFF",
        "texto_display": "#2C3E50",
        "bg_botao_numero": "#FFFFFF",
        "texto_botao_numero": "#2C3E50",
        "bg_botao_cinza": "#95A5A6",
        "texto_botao_cinza": "#FFFFFF",
        "bg_botao_laranja": "#E67E22",
        "texto_botao_laranja": "#FFFFFF",
        "bg_botao_primario": "#3498DB",
        "texto_botao_primario": "#FFFFFF",
        "bg_botao_acao": "#2980B9",
        "texto_botao_acao": "#FFFFFF",
        "cor_sucesso": "#27AE60",
        "cor_perigo": "#E74C3C",
        "cor_alerta": "#F39C12"
    }

    @classmethod
    def pegar_paleta(cls, modo: str) -> dict:
        if modo == "DARK":
            return cls.CORES_ESCURO
        return cls.CORES_CLARO