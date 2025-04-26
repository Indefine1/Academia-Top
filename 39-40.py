# Задания 1
# class Сhat():
#
#     def __init__(self,name):
#
#         self.user_name = name
#
#     def hello(self):
#         print('Привет!')
#
#     def how(self):
#         print(f'{self.user_name},как дела?')
#
#     def bye(self):
#         print(f'{self.user_name},пока')
#
#
#
# user = input('Введите свое имя ')
# welcom = Сhat(user)
#
# welcom.hello()
# welcom.how()
# ans = input()
# welcom.bye()

# Задания 2
class Tasks():
    def __init__(self):
        self.tasks = []
    def add_task(self,task):
        self.tasks.append({'task': task, 'status':'Не выполнено'})

    def show_task(self):
        for i,task in enumerate(self.tasks,start=1):
            print(f"{i}:{task['task']} - {task['status']}")
    def complete_task(self,number):
        self.tasks[number]['status'] = 'Выполнено'


user_task = Tasks()
while True:

    add = input('Выберите действия:\n1.Добавить дело.\n2.Показать дело.\n3.Выполнить задачу\n')
    if add == '1':
        ans = input('Добавьте дело:')
        user_task.add_task(ans)
        print('Дело добавлено')
    elif add == '2':
        user_task.show_task()
    elif add == '3':
        user_task.show_task()
        num = int(input(f'Какую задачу хотите выполнить?'))
        user_task.complete_task(num - 1)
    else:
        print('Не правильное действие ')




