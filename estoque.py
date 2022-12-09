# Sistema de estoque.
cod_produto = {}
descricao = {}
estoque = {}
preco = {}


def prod():
    print('='*30)
    for total, total2 in enumerate(descricao.items()):
        print('({}) {}'.format(total, total2))
    print('='*30)


menu_list = ['Cadastro de produto.', 'Preço.',
             'Estoque.', 'Produtos Cadastrado', 'Pre-Venda.']
while True:
    print('='*30)
    print('      VENDAS - GuS ELETRO')
    print('='*30)
    for i, menu in enumerate(menu_list):
        print('({}) {}'.format(i, menu))
    print('='*30)
    op = (input('Digite: ').strip())
    if op == '0':
        print('='*6, 'Tela De Cadastro', '='*6)
        Cod_cadastro = int((input('Digite para cadastro: ').strip()))
        Descricao = (input('Digite descrição do produto: ').strip())
        Preco = float((input('Digite o preço: ').strip()))
        Estoque = int((input('Digite o estoque: ').strip()))
        cod_produto[Cod_cadastro] = Cod_cadastro
        descricao[Cod_cadastro] = Descricao
        preco[Cod_cadastro] = Preco
        estoque[Cod_cadastro] = Estoque
        print('Produto cadastrado,cod {}, {},preço: R$ {}, estoque: {} unid'.format(
            Cod_cadastro, Descricao, Preco, Estoque))
    elif op == '1':
        pesquisa = input('Pesquisar por (1) cod ?').strip()
        if pesquisa == '1':
            pesquisa_cod_pre = int(
                (input('Digite o cod do produto: ').strip()))
            cod1 = cod_produto.get(pesquisa_cod_pre)
            desc = descricao.get(pesquisa_cod_pre)
            prec = preco.get(pesquisa_cod_pre)
            print('O codigo pesquisado é {}, o produto é {}, preco R$:{}'.format(
                cod1, desc, prec))
    elif op == '2':
        pesquisa = input('Pequisar por (1) cod ?').strip()
        if pesquisa == '1':
            pesquisa_cod_est = int(input('Digite o cod do produto: ').strip())
            cod1 = cod_produto.get(pesquisa_cod_est)
            desc = descricao.get(pesquisa_cod_est)
            est = estoque.get(pesquisa_cod_est)
            print('O codigo pesquisado é {}, o produto é {}, estoque até o  momento {} unid'.format(
                cod1, desc, est))
        # elif DUVIDA !
    elif op == '3':
        prod()
        print('='*30)
    elif op == '4':
        print('DADOS DO CLIENTE')
        print('='*30)
        nome_cliente = (str(input('Nome do cliente: ').strip()))
        print('='*30)
        cpf_cliente = (float(input('Cpf do cliente: ').strip()))
        print('='*30)
        print('CONFIRMACAO DOS DADOS')
        confirmacao_cliente = str(
            input('Nome: {} \nCpf: {}\n {}\n(0) - Confirmar\n(1) - Alterar\nDigitar: '.format(nome_cliente, cpf_cliente, '='*30)).strip())
        print('='*30)
        if confirmacao_cliente == '0':
            print('PRODUTO - VENDA')
            print('='*30)
            busc_prod = int(input('Digite cod do produto : ').strip())
            unidades = int(input('Quantas unidades ? ').strip())
            print('='*30)
            cod1 = cod_produto.get(busc_prod)
            desc = descricao.get(busc_prod)
            prec = preco.get(busc_prod)
            est = estoque.get(busc_prod)
            print('CONFIRMACAO DA VENDA')
            print('='*30)
            print(
                f'Cliente {nome_cliente} \nProduto {desc} \nvalor de R${prec} \nquantidade(s): {unidades}')
            confirmacao_cliente = str(
                input('(0) - Confirmar\n(1) - Alterar\nDigitar: ').strip())
            print('='*30)
            if confirmacao_cliente == '0':
                print('FORMA DE PAGAMENTO')
                print('='*30)
                modo_paga = input(
                    '(0) - Avista \n(1) - Cartao \nDigitar: ').strip()
                print('='*30)
                if modo_paga == '0':
                    print('AVISTA - DESCONTO DE 5%')
                    print('='*30)
                    total_unide = prec*unidades
                    avista = total_unide-(total_unide * 0.05)
                    pagamento = input(
                        f'Cliente {nome_cliente}, produto {desc},quantidade(s) : {unidades} a avista vai ficar: R$ {avista} \n(0) - Confirmar \n(1) - alterar \nDigite : ')
                    print('='*30)
                    if pagamento == '0':
                        alt_est = estoque.pop(busc_prod)
                        alt_est2 = estoque[busc_prod] = alt_est - unidades
                elif modo_paga == '1':
                    print('CARTAO - 5x SEM JUROS - 6x Á 10x tx : 1.99%')
                    print('='*30)
                    cartao = int(
                        input('Digite quantidade de parcelas: ').strip())
                    if cartao <= 5:
                        total_unide = prec*unidades
                        s_juros = total_unide/cartao
                        print('='*30)
                        print(
                            f'O Produto {desc},quantidade(s): {unidades} vai ficar em {cartao}x de R$: {s_juros}, TOTAL = {total_unide}')
                        pagamento = input(
                            '(0) - Confirmar \n(1) - alterar \nDigite : ').strip()
                        print('='*30)
                        if pagamento == '0':
                            alt_est = estoque.pop(busc_prod)
                            alt_est2 = estoque[busc_prod] = alt_est - unidades
                    else:
                        total_unide = prec*unidades
                        juros = ((total_unide*0.0199) *
                                 cartao+total_unide)/cartao
                        juros2 = juros*cartao
                        print(
                            f'O produto {desc},quantidade(s) : {unidades}, vai ficar {cartao}x parcelas de R$: {juros}, TOTAL = {juros2}')
                        pagamento = str(
                            input('(0) - Confirmar\n(1) - Alterar\nDigitar: ').strip())
                        if pagamento == '0':
                            alt_est = estoque.pop(busc_prod)
                            alt_est2 = estoque[busc_prod] = alt_est - unidades
            print('Pre-venda, realizada com $UCE$$O !! ')
    print("")
    print("0 para CONTINUAR | 1 para SAIR")
    if int(input()) == 1:
        break
