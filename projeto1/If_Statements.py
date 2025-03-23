# #Trabalhando com IFs
#
# acordei_antes_das_9 = ''
#
# print("Eu acordei.")
#
# if acordei_antes_das_9 == True:
#     print("Fiz o meu café da manhã e fui correr.")
# elif acordei_antes_das_9 == False:
#     print ("Não tomei meu café da manhã e fui correr.")
# else:
#     print("Não fui correr e fui fazer o almoço.")
#

acordei = False
fome = False

if acordei and fome:
    print("Eu acordei antes das 9 e irei fazer o meu cafe da manha.")
elif acordei and not(fome):
    print("Eu acordei antes das 9, nao estou com fome e irei correr.")
elif not(acordei) and fome:
    print("Eu acordei depois das 9 e estou com fome. Irei fazer o almoco.")
else:
    print("Eu acordei depois das 9 e nao estou com fome. Irei estudar!")

var="James Bond"
print(var[2::-1])