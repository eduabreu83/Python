try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except(ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que vc digitou...!')
except ZeroDivisionError:
    print('Não é possivel dividir um numero po ZERO...')
except KeyboardInterrupt:
    print('O infeliz quis parar e não informou os dados...')
except Exception as erro:
    print(f'Deu merda... {erro.__class__}:(')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('volte sempre! Muito Obrigado!')
