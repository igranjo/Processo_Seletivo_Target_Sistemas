obj_inversao = str(input("Qual string deseja inverter? "))
tamanho = 0
for i in obj_inversao: # Utilizei essa metodologia para evitar utilizar a função len() para descobrir o tamanho da string.
    tamanho = tamanho + 1
obj_invertido = ""
while tamanho != 0:
    obj_invertido = obj_invertido + obj_inversao[tamanho-1] # Aqui realizo a inversão percorrendo a string de trás para frente e concatenando a uma string vazia.
    tamanho = tamanho - 1
print(obj_invertido)
print(obj_inversao[::-1])