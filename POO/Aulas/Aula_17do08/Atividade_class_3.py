# calculadora:

def menu():
    print('******************************')
    print('(1) Somar')
    print('(2) Subtrair')
    print('(3) Multiplicar')
    print('(4) Dividir')
    print('(5) Limpar memória')
    print('(6) Sair do programa')
    print('******************************')
    return 'Qual opção desejada? '

def calculadora():
    memory = 0
    while True:
        alt = int(input(menu()))
        if alt == 1:
            num1 = memory
            num2 = float(input('Digite um valor para somar: '))
            soma = num1 + num2
            print('O resultado é: ', soma)
            memory = soma

        if alt == 2:
            num1 = memory
            num2 = float(input('Digite o outro valor: '))
            subtracao = num1 - num2
            print('O resultado é: ',subtracao)
            memory = subtracao

        if alt == 6:
            print('Volte sempre!!!')
            break
calculadora()