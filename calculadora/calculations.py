# -*- coding: utf-8 -*-

def calcular_consumo(potencia_w, horas_por_dia, dias_por_mes, preco_kwh=0.75):
    if potencia_w < 0 or horas_por_dia < 0 or dias_por_mes < 0:
        raise ValueError("Os valores não podem ser negativos!")
    if horas_por_dia > 24:
        raise ValueError("Não pode usar mais de 24 horas por dia!")
    if dias_por_mes > 31:
        raise ValueError("Um mês não tem mais que 31 dias!")
    
    consumo = (potencia_w * horas_por_dia * dias_por_mes) / 1000.0
    custo_mensal = consumo * preco_kwh
    custo_diario = custo_mensal / dias_por_mes if dias_por_mes > 0 else 0
    
    return {
        "kwh_mes": round(consumo, 2),
        "custo_mensal": round(custo_mensal, 2),
        "custo_diario": round(custo_diario, 2)
    }


def calcular_media(lista_valores):
    if not lista_valores:
        raise ValueError("Nenhum valor foi informado!")
    
    numeros = []
    for v in lista_valores:
        numeros.append(float(str(v).replace(",", ".")))
    
    media = sum(numeros) / len(numeros)
    return round(media, 2)


def calcular_imc(peso, altura):
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso e altura devem ser maiores que zero!")
    
    if altura > 3.0:
        altura = altura / 100.0
    
    imc = peso / (altura ** 2)
    imc = round(imc, 2)
    
    if imc < 18.5:
        classificacao = "Abaixo do peso"
        cor = "alerta"
    elif imc < 25:
        classificacao = "Peso ideal"
        cor = "sucesso"
    elif imc < 30:
        classificacao = "Sobrepeso"
        cor = "alerta"
    elif imc < 35:
        classificacao = "Obesidade Grau I"
        cor = "perigo"
    elif imc < 40:
        classificacao = "Obesidade Grau II"
        cor = "perigo"
    else:
        classificacao = "Obesidade Grau III (Mórbida)"
        cor = "perigo"
    
    return imc, classificacao, cor