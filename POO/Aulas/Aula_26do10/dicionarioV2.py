conts = dict()
nomes = ['maria','joão','maria','gabriel','joão','francisco']
for nome in nomes:
    conts[nome] = conts.get(nome,0) + 1
print(conts)