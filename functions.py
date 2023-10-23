FILEPATH = "todos.txt"
def get_todos(filename=FILEPATH):
    with open(filename, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todo, filename=FILEPATH):
    with open(filename, "w") as file:
        file.writelines(todo)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())