def classificar_nivel_heroi(xp_heroi):
    if xp_heroi < 1000:
        return "Ferro"
    elif 1001 <= xp_heroi <= 2000:
        return "Bronze"
    elif 2001 <= xp_heroi <= 5000:
        return "Prata"
    elif 5001 <= xp_heroi <= 7000:
        return "Ouro"
    elif 7001 <= xp_heroi <= 8000:
        return "Platina"
    elif 8001 <= xp_heroi <= 9000:
        return "Ascendente"
    elif 9001 <= xp_heroi <= 10000:
        return "Imortal"
    else:
        return "Radiante"

# Uso da função
nome_heroi = "SuperCoder"
xp_heroi = 4500
nivel = classificar_nivel_heroi(xp_heroi)
print(f"O Herói de nome {nome_heroi} está no nível de {nivel}")
