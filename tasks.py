"""A tiny task tracker used for Git practice."""

tasks = [
    {"title": "Learn Git locally and on GitHub", "done": False},
    {"title": "Make my first commit", "done": False},
    {"title": "Practice branching", "done": False},
    {"title": "Solve exercise 1", "done": False},
]


def show_tasks():
    print("MY TASKS")
    print("-" * 24)
    for number, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"{number}. [{mark}] {task['title']}")


if __name__ == "__main__":
    show_tasks()
