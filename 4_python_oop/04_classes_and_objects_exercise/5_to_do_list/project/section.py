from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        # try:
        #     task = next(filter(lambda t: t.name == task_name, self.tasks))
        # except StopIteration:
        #     return f"Could not find task with the name {task_name}"
        #
        # task.completed = True
        #
        # return f"Completed task {task_name}"

        for current_task in self.tasks:
            if current_task.name == task_name:
                current_task.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed_tasks = 0

        for current_task in self.tasks:
            if current_task.completed:
                self.tasks.remove(current_task)
                removed_tasks += 1

        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"

        for task in self.tasks:
            result += f"{task.details()}\n"

        return result
