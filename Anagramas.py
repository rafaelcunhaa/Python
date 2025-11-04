while True:
    
    try:
        palavra = input("Digite uma palavra: ").lower()
        palavra_verificar = input("Digite outra palavra: ").lower()
        palavra = palavra.replace(' ','') # tirar os espaces entre as palavras caso ouver 
        palavra_verificar = palavra_verificar.replace(' ','') # tirar os espaces entre as palavras caso ouver 
        
        
        
        for i in palavra:
            if i in palavra_verificar:
                palavra_verificar = palavra_verificar.replace(i ,"",1)
                palavra = palavra.replace(i ,"",1)
        
        if palavra == palavra_verificar:
            print("Não são anagramas")
        else:
            print("Anagramas")
        break
    
    except Exception as e:
        print("Erro: " , e)
        