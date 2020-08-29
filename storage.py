import settings
import functools


def create():
    id = int(input('ESCREVA O CÓDIGO DO PRODUTO: '))

    found_item = list(filter(lambda _product: _product['id'] == id, settings.storage))
    if len(found_item) > 0:
        print('CÓDIGO JÁ EXISTENTE.')
        return

    description = input('ESCREVA A DESCRIÇÃO DO PRODUTO: ')
    quantity = int(input('ESCREVA A QUANTIDADE: '))

    if quantity <= 0:
        print('A QUANTIDADE DE COMPRA PRECISA SER MAIOR QUE 0.')
        return

    product = {
        'id' : id,
        'description' : description,
        'quantity' : quantity
    }

    if id is not None and description is not None and quantity is not None:
        settings.storage.append(product)

    print('PRODUTO CADASTRADO COM SUCESSO.')

    return settings.storage


def update():
    id = int(input('DIGITE O CÓDIGO DO PRODUTO QUE DESEJA ALTERAR: '))

    found_item = list(filter(lambda _product: _product['id'] == id, settings.storage))
    if len(found_item) == 0:
        print('PRODUTO NÃO CADASTRADO.')
        return

    print(f"DESCRIÇÃO: {found_item[0]['description']}")
    print(f"QUANTIDADE EM ESTOQUE: {found_item[0]['quantity']}")
    
    description = input('DIGITE A NOVA DESCRIÇÃO DO PRODUTO (PRESSIONE ENTER PARA MANTER O VALOR ATUAL): ')
    quantity = int(input('DIGITE A NOVA QUANTIDADE DO PRODUTO (PRESSIONE ENTER PARA MANTER O VALOR ATUAL): '))

    if quantity <= 0:
        print('A QUANTIDADE DE COMPRA PRECISA SER MAIOR QUE 0.')
        return

    item_index = settings.storage.index(found_item[0])
    
    if description != '':
        settings.storage[item_index]['description'] = description
        
    if quantity != '':
        settings.storage[item_index]['quantity'] = quantity

    print(f'PRODUTO#{id} ATUALIZADO COM SUCESSO!')

    return settings.storage


def delete():  
    id = int(input('DIGITE O CÓDIGO DO PRODUTO QUE DESEJA ALTERAR: '))

    found_item = list(filter(lambda _product: _product['id'] == id, settings.storage))
    if len(found_item) == 0:
        print('PRODUTO NÃO EXCLUÍDO')
        return
    
    confirm_delete = input('DESEJA EXCLUIR O PRODUTO?')
    if confirm_delete == 'sim':    
        print('PRODUTO EXCLUIDO COM SUCESSO')
        settings.storage.remove(found_item[0])
    else:
        print('PRODUTO NÃO EXCLUÍDO')

    return settings.storage


def index():
    print("CÓDIGO\tDESCRIÇÃO\tQUANTIDADE EM ESTOQUE:")
    print(6 * '-', '', 14 * '-', '', 22 * '-')
    for product in sorted(settings.storage, key=lambda x: x['id'], reverse=False):
        print(f" {product['id']}     {product['description'].ljust(20)} {product['quantity']}")
    
    amount_of_products = len(settings.storage)
    amount_of_products_in_storage = functools.reduce((lambda x, y: x + y['quantity']), settings.storage, 0)
    amount_of_products_bellow_minimum_limit = len(list(filter(lambda x: x['quantity'] < 100, settings.storage)))

    print(f'Total de produtos cadastrados: {amount_of_products}')
    print(f'Quantidade de itens em estoque: {amount_of_products_in_storage}')
    print(f'Produtos com estoque abaixo do mínimo permitido (100 unidades): {amount_of_products_bellow_minimum_limit}')

    return settings.storage


def buy():
    id = int(input('DIGITE O CÓDIGO DO PRODUTO QUE DESEJA COMPRAR: '))

    found_item = list(filter(lambda _product: _product['id'] == id, settings.storage))
    if len(found_item) == 0:
        print('PRODUTO NÃO CADASTRADO.')
        return

    print(f"DESCRIÇÃO: {found_item[0]['description']}")
    print(f"QUANTIDADE EM ESTOQUE: {found_item[0]['quantity']}")

    quantity_to_buy = int(input('DIGITE A QUANTIDADE DE COMPRA DO PRODUTO: '))
    if quantity_to_buy <= 0:
        print('A QUANTIDADE DE COMPRA PRECISA SER MAIOR QUE 0.')
        return

    item_index = settings.storage.index(found_item[0])
    settings.storage[item_index]['quantity'] += quantity_to_buy

    print(f"{quantity_to_buy} PRODUTOS ({found_item[0]['description']}) ADICIONADOS COM SUCESSO!")

    return settings.storage

        
def sell():
    id = int(input('DIGITE O CÓDIGO DO PRODUTO QUE DESEJA VENDER: '))

    found_item = list(filter(lambda _product: _product['id'] == id, settings.storage))
    if len(found_item) == 0:
        print('PRODUTO NÃO CADASTRADO.')
        return

    print(f"DESCRIÇÃO: {found_item[0]['description']}")
    print(f"QUANTIDADE EM ESTOQUE: {found_item[0]['quantity']}")

    quantity_to_sell = int(input('DIGITE A QUANTIDADE QUE DESEJA VENDER: '))
    if quantity_to_sell <= 0:
        print('A QUANTIDADE DE VENDAPRA PRECISA SER MAIOR QUE 0.')
        return

    item_index = settings.storage.index(found_item[0])

    total_item = settings.storage[item_index]['quantity'] - quantity_to_sell

    if total_item >= 0:
        settings.storage[item_index]['quantity'] -= quantity_to_sell
        print(f"{quantity_to_sell} PRODUTOS ({found_item[0]['description']}) VENDIDOS COM SUCESSO.")
        return settings.storage

    print('NÃO TEMOS PRODUTOS SUFICIENTES.')
    return
