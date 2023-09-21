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
            num2 = float(input('Digite um valor para subtrair: '))
            subtracao = num1 - num2
            print('O resultado é: ',subtracao)
            memory = subtracao

        if alt == 3:
          num1 = memory
          num2 = float(input('Digite um valor para multiplicar: '))
          mult = num1 * num2
          print('O resultado é:', mult)
          memory = mult

        if alt == 4:
          num1 = memory
          num2 = float(input('Digite um valor para dividir: '))
          if num2 == 0:
            nnum2 = float(input('Digite um valor diferente de zero: '))
            num2 = nnum2

          div = num1 / num2
          print('O resultado é: ', div)
          memory = div

        if alt == 5:
          memory = 0
          print('A memória foi resetada: ', memory)

        if alt == 6:
            print('Volte sempre!!!')
            break


calculadora()