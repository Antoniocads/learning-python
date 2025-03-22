#Estudando listas - Part 1

pessoas = ['Lucas','Suzane','Marcos','João','Putão']
#              0       1        2       3       4

print(f'''A: Quem você conhece? 
B: Conheço estas pessoas:
{pessoas[1]}, {pessoas[3]} e {pessoas[2]}''')

print('')

pessoas[1] = "Douglas"

print(f'''A: Quem vai ir conosco? 
B: Talvez você não conheça, mas as pessoas que estão confirmados são:
{pessoas[1]}, {pessoas[3]} e {pessoas[2]}''')

print('')

#Expandindo o estudo para funções da lista

numeros = [1,2,3,4,5,6,7,8,9,10]
objetos = ['colher','faca','tesoura','borracha']

print('Juntando as duas listas:')
numeros.extend(objetos)
print(numeros)

print('')

print('Adicionando valor garfo no final da lista de objetos:')
objetos.append('garfo')

print(objetos)

print('')

print('Inserindo valor garfo no terceira posição da lista de objetos:')
objetos.insert(3,'garfo')

print(objetos)

print('')

print('Removendo objeto faca da lista de objetos:')
objetos.remove('faca')

print(objetos)

print('')

print('Removendo objeto que está na posição de referencia número 3 == borracha:')
objetos.pop(3)

print(objetos)

print('')

print('Checando se o objeto garfo existe:')

print(objetos.index('garfo'))

print('')

objetos.append('garfo')
print('Checando quantos garfos existem na lista:')

print(objetos)
print(objetos.count('garfo'))

print('')

print('Organizando lista:')

print(f'Antes de organizar a lista: {objetos}')

objetos.sort()
print(f'Depois de organizar a lista: {objetos}')

print('')