
def create(storage: list):
    _id = int(input('Escreva o codigo do produto: '))
    _description = input('Escreva a descrição do produto: ')
    _quantity = int(input('Escreva a quantidade: '))
    product = {
        'id' : _id,
        'description' : _description,
        'quantity' : _quantity
    } 
    if _id is not None and _description is not None and _quantity is not None :
        storage.append(product)
    return storage

def update(storage: list):
    
