import random
substantivos = ["amor", "lua", "mar", "vento", "céu", "flor"]
adjetivos = ["belo", "radiante", "sereno", "profundo", "etéreo", "calmo"]
verbos = ["dança", "suspira", "brilha", "flui", "encanta", "desperta"]
def gerar_estrofe():
    verso1 = f"{random.choice(substantivos)} {random.choice(verbos)} {random.choice(adjetivos)}"
    verso2 = f"{random.choice(adjetivos)} {random.choice(substantivos)} {random.choice(verbos)}"
    verso3 = f"{random.choice(verbos)} {random.choice(adjetivos)} {random.choice(substantivos)}"
    return f"{verso1}\n{verso2}\n{verso3}\n"
def gerar_poesia(num_estrofes):
    poesia = ""
    for _ in range(num_estrofes):
        poesia += gerar_estrofe() + "\n"
    return poesia
poesia = gerar_poesia(3)
print(poesia)
