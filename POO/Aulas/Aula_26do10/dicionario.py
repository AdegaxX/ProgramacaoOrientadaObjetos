conts = dict()
nomes = ['maria','joão','maria','gabriel','joão','francisco']
for nome in nomes:
    if nome not in conts:
        conts[nome] = 1
    else:
        conts[nome] = conts[nome] + 1
print(conts)

