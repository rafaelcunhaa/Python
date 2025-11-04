palavra = input("Digite uma palavra: ")
palavrax = ""

for j in palavra:
    if j != " ":
     palavrax = palavrax + j

palavrax = palavrax.upper()
reversa = ""


for i in palavrax:
    reversa = i + reversa

if palavrax == reversa:
    print("É um palindromo")
    
else:
    print("Não é palindromo")