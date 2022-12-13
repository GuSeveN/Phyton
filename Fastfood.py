nome_cpf = {}
endereco = {}
restaurante = {}
menulist = ['Restaurantes', 'Pedidos', 'Confimarcao de entrega']
restaurantes = ['Macdonalds', 'Pizzahut', 'China in Box', 'BrejaOn']


def menu():
    for n, m in enumerate(menulist):
        print('({}) {}'.format(n, m))


def rest():
    for n, m in enumerate(restaurantes):
        print('({}) {}'.format(n, m))


while True:
    print('*'*5, 'IFODD', '*'*5)
    menu()
    op = (input())
    if op == '0':
        rest()
    elif op == '1':
        rest()
        resta = (input('Qual restaurante ? ').strip())
        pedido = (input('Digite seu pedido: ').strip())
        cliente = (input('Digite seu nome e cpf: ').strip())
        end = (input('Digite seu end de entrega: ').strip())
        nome_cpf[cliente] = cliente
        restaurante[cliente] = resta
        endereco[cliente] = end
        print('Sr(a) {}, seu {} foi concluido'.format(cliente, pedido))
    elif op == '2':
        rest()
        print(restaurante)
        print('Seu pedido chegou ?\n sim \n nao')
        op = (input())
        if op == 'sim':
            del restaurante
            del nome_cpf
            del endereco

    print('Voltar ao Menu \n(1) Continuar  - (2) Exit ')
    op = (input())
    if op == '2':

        break
