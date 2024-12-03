HELP = '''
help - вывести справку о командах
add - добавить ноую задачу
show - печатать все добавленые задачи
exit - выйти из программы
'''
today = []
tomorrow = []
other = []
tasks = []

if __name__ == '__main__':
    command = ''
    while command != 'exit':
        command = input('Введите команду')
        if command == 'help':
            print(HELP)
        elif command == 'show':
            # print(tasks)
            print(today, tomorrow, other)
        elif command == 'add':
            item = input('Введите задачу')
            date = input('Введите дату')
            # task = [date, item]
            if date == 'Сегодня':
                today.append(item)
            elif date == 'Завтра':
                tomorrow.append(item)
            else:
                other.append(item)
            # tasks.append(task)
            print('Задача добавлена!')
        elif command == 'exit':
            print('Спасибо за использование! До свидания!')
