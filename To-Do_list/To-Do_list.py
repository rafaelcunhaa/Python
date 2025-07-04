tarefa = []
identificacao = 1

######################
##### ADD TAREFA #####
######################

def adicionar_tarefa():
    novo_titulo = input("Digite o titulo da tarefa:")
    nova_descricao = input("Digite a descrição da tarefa:")

    with open("tarefas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write( f"{identificacao} - {novo_titulo} - {nova_descricao} \n")



######################
##### VER TAREFA #####
######################

def ler_tarefa():
    with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
        tarefa = arquivo.readlines()

    for linha in tarefa:
        print(linha.strip())


######################
### DELETAR TAREFA ###
######################

def deletar_tarefa():
    opcao = input("Qual tarefa queres deletar (use o número da linha, começando de 0):")
    with open("tarefas.txt", "w", encoding="utf-8") as arquivo:
        arquivo.writelines(tarefa)
        print("Tarefa deletada com sucesso.")

    try:
        indice = int(opcao)
        if 0 <= indice < len(tarefa):
            del tarefa[indice]
        else:
            print("Índice inválido. Nenhuma tarefa foi deletada.")
            return
    except ValueError:
        print("Por favor, digite um número válido.")
        return


######################
## ATUALIZAR TAREFA ##
######################

def atualizar_tarefa():
    try:
        opcao = int(input("Digite o número da tarefa que deseja atualizar: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        return

    with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
        tarefas = arquivo.readlines()

    if opcao < 0 or opcao >= len(tarefas):
        print("Número de tarefa inválido.")
        return

    novo_titulo = input("Digite o novo título da tarefa: ")
    nova_descricao = input("Digite a nova descrição da tarefa: ")

    partes = tarefas[opcao].strip().split(" - ")
    if len(partes) >= 1:
        identificador = partes[0]
    else:
        identificador = str(opcao)

    tarefas[opcao] = f"{identificador} - {novo_titulo} - {nova_descricao} \n"

    with open("tarefas.txt", "w", encoding="utf-8") as arquivo:
        arquivo.writelines(tarefas)
    print("Tarefa atualizada com sucesso.")





def main():
    global identificacao
    print("Olá, bem vindo ao gerenciador de tarefas \n")
    escolha = -1
    while escolha != 0:
        try:
            escolha = int(input("Escolha uma das opções: \n" \
            "[1] Adicionar Tarefa \n" \
            "[2] Deletar Tarefa \n" \
            "[3] Atualizar Tarefa \n" \
            "[4] Ver tarefas \n" \
            "[0] Sair \n" \
            "\n" \
            "Escolha:"))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if escolha == 1:
            adicionar_tarefa()
            identificacao += 1

        elif escolha == 2:
            deletar_tarefa()

        elif escolha == 3:
            atualizar_tarefa()

        elif escolha == 4:
            ler_tarefa()    

        elif escolha == 0:
            break

        else:
            print("Opção invalida")        
    

if __name__ == "__main__":
    main()
