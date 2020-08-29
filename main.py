import authentication
import storage
import settings

settings.init()

menu = 0

while menu != 7:
    print('\nMenu')
    menu = int(input(
        "\t1. Cadastrar Produto\n\t2. Alterar Produto\n\t3. Excluir Produto\n\t4. Listar Estoque de Peça\n\t5. "
        "Comprar Produto\n\t6. Vender Produto\n\t7. Sair\n\nDigite a opção desejada: "))

    if menu == 1:
        storage.create()

    elif menu == 2:
        authentication.authenticate()
        if settings.is_authenticated:
            storage.update()

    elif menu == 3:
        authentication.authenticate()
        if settings.is_authenticated:
            storage.delete()

    elif menu == 4:
        storage.index()

    elif menu == 5:
        storage.buy()

    elif menu == 6:
        storage.sell()

    elif menu == 7:
        authentication.logout()

    else:
        print("\033[31mOPÇÃO INVALIDA!\033[m")