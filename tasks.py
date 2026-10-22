"""A tiny task tracker used for Git practice."""

tasks = [
    {"title": "Learn git status", "done": False},
    {"title": "Make my first commit", "done": False},
]


def show_tasks():
    print("MY TASKS")
    print("-" * 24)
    for number, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"{number}. [{mark}] {task['title']}")


if __name__ == "__main__":
    show_tasks()
