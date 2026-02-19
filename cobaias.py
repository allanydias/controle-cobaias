#-----------------------------------------------  criação -------------------
# Projeto feito antes do estudo de funções, foco em lógica e estrutura

print('SISTEMA DE EXPERIMENTOS')
print()

print('Menu. Digite: ')

menu = ['0. sair', '1. Cadastro de cobaias ', '2. Relatório parcial', '3. Relatório Final']

X = -1

soma_final_total = 0
soma_final_coelhos = 0 
soma_final_ratos = 0
soma_final_sapos = 0

#----  menu -----------------------------------------------------
while X != 0:
    
    print()
    for i in range(4):
        print(menu[i])

    print()
    X = int(input())
    print()

    while 0 > X or X > 3:
        print('Tente novamente: ')
        print()

        for i in range(0,4):
            print(menu[i])

        print()
        X = int(input())
        print()

    soma_parcial_total = 0
    soma_parcial_coelhos = 0 
    soma_parcial_ratos = 0
    soma_parcial_sapos = 0

    # ----- cadastro -------------------------------------------
    if X == 1:
        N = int(input('Quantos casos você vai querer cadastrar? '))

        while N <= 0:
            print()
            print('OPS! Não pode ser um número igual ou menor a 0.')
            N = int(input('Digite novamente quantos casos você vai querer cadastar: '))
            print()
        print('Digite: C. coelhos, R. ratos, S. sapos')
        print()
        for i in range(N):

            print()
            tipo_cobaias = input('Tipo de cobaia: ')
            tipo_cobaias = tipo_cobaias.upper()

            while tipo_cobaias not in ('C', 'R', 'S'):
                print()
                print('Não foi possivel encontrar esse tipo de cobaia nos resgistros do laboratório, tente novamente.')
                print()
                tipo_cobaias = input('Tipo de cobaia: ')
                tipo_cobaias = tipo_cobaias.upper()
                print()
            
                                 

            while quantidade_cobaias <= 0:
                print('Digite novamente. ', end='')
                quantidade_cobaias = int(input('Quantidade de cobaias: '))
                print()

            soma_parcial_total += quantidade_cobaias

            if tipo_cobaias == 'C':
                soma_parcial_coelhos += quantidade_cobaias
            elif tipo_cobaias == 'R':
                soma_parcial_ratos += quantidade_cobaias
            else:
                soma_parcial_sapos += quantidade_cobaias

        soma_final_total += soma_parcial_total
        soma_final_coelhos += soma_parcial_coelhos
        soma_final_ratos += soma_parcial_ratos
        soma_final_sapos += soma_parcial_sapos
        

     #---- relatório parcial, número 2 ---------------------
    elif X == 2:
       if soma_parcial_total != 0:

            print()
            print('RELATÓRIO PARCIAL:')
            print()
            print(f'Total de cobaias: {soma_parcial_total}')
            print()
            print(f'Total de COELHOS: {soma_parcial_coelhos}')
            print(f'Total de RATOS: {soma_parcial_ratos}')
            print(f'Total de SAPOS: {soma_parcial_sapos}')
            print()
       else:
           print("Sem cadastro no momento.")


        #---- relatório final, número 3 ---------------------
    elif X == 3:

        if soma_final_total != 0:
            percentual_coelhos = soma_final_coelhos * 100 / soma_final_total
            percentual_ratos = soma_final_ratos * 100 / soma_final_total
            percentual_sapos = soma_final_sapos * 100 / soma_final_total

                    
        print()

        print()
        print('RELATÓRIO FINAL:')
        print()
        print(f'Total de cobaias: {soma_final_total}')
        print()
        print(f'Total de COELHOS: {soma_final_coelhos}')
        print(f'Total de RATOS: {soma_final_ratos}')
        print(f'Total de SAPOS: {soma_final_sapos}')
        print()

        if soma_final_total == 0:
            print()
            print('Soma total = 0')
            print()
        else: 
            print()
            print(f'Percentual de coelhos: {percentual_coelhos:.2f}')
            print(f'Percentual de ratos: {percentual_ratos:.2f}')
            print(f'Percentual de sapos: {percentual_sapos:.2f}')
            print()


    





