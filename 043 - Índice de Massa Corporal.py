#dev uma logica q leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo
# abaixo de 18,5 abaixo do peso
# entre 18,5 a 25 peso ideal
# 25 até 30 sobrepeso
# 30 a 40 obeso
# maior q 40 obeso morbido
peso = float(input('Digite se peso em KG: '))
altura = float(input('Digite sua altura em (m):'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é de {:.1f} e vc esta ABAIXO do seu pedo ideal'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é de {:.1f} e vc esta com o pedo IDEAL'.format(imc))
elif imc > 25 and imc <=30:
    print('Seu IMC é de {:.1f} e vc esta com SOBREPESO'.format(imc))
elif 30 < imc <=40:
    print('Seu IMC é de {:.1f} e vc esta OBESO'.format(imc))
else:
    print('Seu IMC é de {:.1f} e vc esta com OBESIDADE MORBIDA'.format(imc))

