class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        if task in self.tasks:
            print(f"{task} уже записана\n")
        else:
            self.tasks[task] = False

    def complete_task(self, task):
        if task not in self.tasks:
            print(f"{task} не существует\n")
        else:
            self.tasks[task] = True

    def remove_task(self, task):
        if task not in self.tasks:
            print(f"{task} не существует\n")
        else:
            del self.tasks[task]

    def list_tasks(self):
        if not self.tasks:
            print("Список задач пуст\n")
            return

        print("Список задач:")
        for task in self.tasks:
            if self.tasks[task]:
                print('[Выполнено]' + task)
            else:
                print('[В процессе]' + task)
        print("")


task_list = ToDoList()

task_list.list_tasks()

task_list.add_task("Задача1")
task_list.add_task("Задача2")
task_list.add_task("Задача3")
task_list.add_task("Задача3")

task_list.list_tasks()

task_list.complete_task("Задача1")
task_list.complete_task("Task1")

task_list.remove_task("Задача2")
task_list.remove_task("Task2")

task_list.list_tasks()
