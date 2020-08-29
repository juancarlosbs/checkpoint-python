storage = [
    {
        'id' : 123,
        'description' : 'descricao1',
        'quantity' : 12
    },
    {
        'id' : 124,
        'description' : 'descricao2',
        'quantity' : 66
    }
]


def create():
    _id = int(input('Escreva o código do produto (precisa ser um número): '))
    _description = input('Escreva a descrição do produto (precisa ser um texto): ')
    _quantity = int(input('Escreva a quantidade (precisa ser um número): '))

    product = {
        'id' : _id,
        'description' : _description,
        'quantity' : _quantity
    } 

    if _id is not None and _description is not None and _quantity is not None:
        storage.append(product)

    print('Produto cadastrado com sucesso.')
    return storage


def update():
    _id = int(input('Digite o código do produto que deseja alterar: '))

    found_item = list(filter(lambda _product: _product['id'] == _id, storage))
    if len(found_item) == 0:
        print('Produto não encontrado.')
        return
    
    _description = input('Digite a nova descrição do produto (Pressione enter para manter o valor atual): ')
    _quantity = input('Digite a nova quantidade do produto (Pressione enter para manter o valor atual): ')

    item_index = storage.index(found_item[0])
    
    if _description != '':
        storage[item_index]['description'] = _description
        
    if _quantity != '':
        storage[item_index]['quantity'] = int(_quantity)

    print(f'Produto#{_id} atualizado com sucesso!')
    return storage

def delete():  
    _id = int(input('Digite o código do produto que deseja deletar: '))

    found_item = list(filter(lambda _product: _product['id'] == _id, storage))
    if len(found_item) == 0:
        print('Produto não encontrado.')
        return

    storage.remove(found_item[0])

    print(f'Produto#{_id} deletado com sucesso!')
    return storage

def index():
    print("CÓDIGO\tDESCRIÇÃO\tQUANTIDADE EM ESTOQUE:")
    print(6 * '-', '', 14 * '-', '', 22 * '-')
    for product in storage:
        print(f" {product['id']}     {product['description'].ljust(20)} {product['quantity']}")


        