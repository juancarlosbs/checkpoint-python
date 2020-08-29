import storage

menu = 0

while menu != 7:
    print('\nMenu')
    menu = int(input(
        "\t1. Cadastrar Produto\n\t2. Alterar Produto\n\t3. Excluir Produto\n\t4. Listar Estoque de Peça\n\t5. "
        "Comprar Produto\n\t6. Vender Produto\n\t7. Sair\n\nDigite a opção desejada: "))

    if menu == 1:
        storage.create()

    elif menu == 2:
        storage.update()

    elif menu == 3:
        storage.delete()

    elif menu == 4:
        storage.index()

    elif menu == 5:
        print('void')

    elif menu == 6:
        print('void')

    elif menu == 7:
        print("Saindo...")
        exit()

    else:
        print("\033[31mOpção inválida!\033[m")