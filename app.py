todos = []
while True:
    user_action = input("Type Add, Show , Edit or Exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo :")
            todos[number] = new_todo
        case 'exit':
            break

print("Bye!")