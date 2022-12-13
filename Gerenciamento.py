# Cadastro de prisao
nome = {}
numero_detento = {}
detenção = {}
menu_list = (
    '(1) - Cadastro detendo \n(2) - Detentos Cadastrado,\n(3) - Exclusao de Detento ')
while True:
    print('='*8, 'Delegacia de Gotham', '='*8)
    print(menu_list)
    print('='*37)
    op = (input())
    if op == '1':
        while True:

            print('Cadastro Gotham')
            numero_det = (input('Numero do detento: ').strip())
            nome_det = (input('Nome do detento: ').strip())
            motivo_det = (input('Qual violacao do detento: ').strip())
            numero_detento[numero_det] = numero_det
            nome[numero_det] = nome_det
            detenção[numero_det] = motivo_det
            print(f'O detento {nome_det}, foi cadastrado com sucesso !')
            print('='*37)
            print('(1) - Cadastrar um novo \n(2) - Sair  ')
            op = (input())
            if op == '2':
                break
    elif op == '2':
        print('Detentos Gotham')
        print(nome)
    elif op == '3':
        print(nome)
        print('Qual detento que vc quer apagar do cadastro ? \npelo cadastro')
        op = (input())
        del nome[op]
        print ('Reginstro deletado')

    print('Voltar ao Menu \n(1) Continuar  - (2) Exit ')
    op = (input())
    if op == '2':
        break
