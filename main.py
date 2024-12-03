HELP = '''
help - вывести справку о командах
add - добавить ноую задачу
show - печатать все добавленые задачи
exit - выйти из программы
'''

tasks = []

if __name__ == '__main__':
    command = ''
    while command != 'exit':
        command = input('Введите команду')
        if command == 'help':
            print(HELP)
        elif command == 'show':
            print(tasks)
        elif command == 'add':
            date = input('Введите дату')
            item = input('Введите задачу')
            task = [date, item]
            tasks.append(task)
            print('Задача добавлена!')
        elif command == 'exit':
            print('Спасибо за использование! До свидания!')
