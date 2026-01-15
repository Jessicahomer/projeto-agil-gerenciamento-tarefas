# projeto-agil-gerenciamento-tarefas
tasks = []

def create_task(title, priority):
    task = {
        "title": title,
        "priority": priority
    }
    tasks.append(task)
    return task

def list_tasks():
    return tasks

def update_task(index, new_title):
    tasks[index]["title"] = new_title

def delete_task(index):
    tasks.pop(index)

if __name__ == "__main__":
    create_task("Estudar Engenharia de Software", "Alta")
    print(list_tasks())
