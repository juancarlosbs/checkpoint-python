import settings


def authenticate():
  if settings.is_authenticated is False:
    settings.given_password = input('DIGITE SUA SENHA: ')
    settings.authentication_tries += 1

    if settings.given_password != settings.correct_password:
      if settings.authentication_tries >= settings.max_authentication_tries_allowed:
        print('SEU ACESSO FOI BLOQUEADO! PROCURE O ADMINISTRADOR')
        exit()

      print('SENHA INCORRETA')
      return

    settings.is_authenticated = True


def logout():
  print('SAINDO...')
  exit()
