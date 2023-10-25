arq = open('teste.txt', 'w')
arq.write('Oi')
arq.close()
arq = open('teste.txt')
x = arq.read()
print(x)

f = open('teste.txt', 'w')
f.write('Olá mundo')
f.close()

f = open('teste.txt')
ler = f.read(3)
print(ler)

resto = f.read()
print(resto)

f = open('teste.txt','r')
linha1 = f.readline()
linha2 = f.readline()
f.close()
print(linha1)
print(linha2)

lista = ['Ola mundo\n', 'Ola Python\n', 'Ola UFC']
f = open('teste.txt')
f.writelines(lista)
f = open('teste.txt', 'r')
cont = f.readline()
print(cont)
f.close()

f = open('teste.txt','a')
f.write('\nOla Python')
f.close()

f = open('teste.txt','r+')
f.write('0123456789abcdef')
f.seek(5)
x = f.read(1)
print(x)