import json
import os

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, title):
        task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'done': False
        }
        self.tasks.append(task)
        self.save_tasks()
        print("Tarefa adicionada!")

    def list_tasks(self):
        if not self.tasks:
            print("Nenhuma tarefa encontrada.")
            return
        for task in self.tasks:
            status = "✅" if task['done'] else "❌"
            print(f"{task['id']}. [{status}] {task['title']}")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['done'] = True
                self.save_tasks()
                print("Tarefa concluída!")
                return
        print("Tarefa não encontrada.")

    def remove_task(self, task_id):
        new_tasks = [task for task in self.tasks if task['id'] != task_id]
        if len(new_tasks) == len(self.tasks):
            print("Tarefa não encontrada.")
        else:
            self.tasks = new_tasks
            self.save_tasks()
            print("Tarefa removida!")
