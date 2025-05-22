from task_manager import TaskManager

def menu():
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar como concluída")
    print("4. Remover tarefa")
    print("5. Sair")

if __name__ == "__main__":
    tm = TaskManager()

    while True:
        menu()
        choice = input("Escolha uma opção: ")

        if choice == "1":
            title = input("Digite o título da tarefa: ")
            tm.add_task(title)
        elif choice == "2":
            tm.list_tasks()
        elif choice == "3":
            task_id = int(input("ID da tarefa a concluir: "))
            tm.complete_task(task_id)
        elif choice == "4":
            task_id = int(input("ID da tarefa a remover: "))
            tm.remove_task(task_id)
        elif choice == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
