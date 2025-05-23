def get_todos(filepath):
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

while True:
    user_action = input("Type add,show,edit,complete or exit : ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

            todo = user_action [4:]

            todos = get_todos('exm5.txt')
            todos.append(todo + '\n')

            with open('exm5.txt','w') as file:
                file.writelines(todos)

    elif user_action.startswith("show"):

        todos = get_todos('exm5.txt')

        for index,item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number-1

            todos = get_todos('exm5.txt')
            new_todo = input("Enter the new todo : ")
            todos[number] = new_todo + '\n'

            with open('exm5.txt','w') as file:
                file.writelines(todos)
        except ValueError:
            print("The command is not valid")

            continue

    elif user_action.startswith("complete"):

        try:
            number = int(user_action[9:])
            todos = get_todos('exm5.txt')
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('exm5.txt','w') as file :
                file.writelines(todos)
                message = f"todo {todo_to_remove} was completely removed "
                print(message)
        except IndexError:
            print("There is no item with that Number .")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("command is not valid")

print("bye!!!!")