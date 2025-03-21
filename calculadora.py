while True:

    n1 = int(input('um valor: '))
    n2 = int(input('Outro valor: '))


    soma = n1 + n2
    multiplicaccao = n1 * n2
    divisao = n1 / n2 if n2 != 0 else 'erro (divisão por zero)'
    subtracao = n1 - n2

    print('A soma é =',soma,'/','A multiplicacao é =',multiplicaccao,'/','A divisao é = ',divisao,'/','A subtracao é =',subtracao)

    continuar = input('deseja continuar? (s/n):').strip().lower()
    if continuar == 'n':
        print('encerrando o programa...')
        break
