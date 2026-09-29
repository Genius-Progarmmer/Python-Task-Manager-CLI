import os
import sys
from dotenv import load_dotenv

load_dotenv()

max_tasks_value = os.getenv("TODO_MAX_TASKS")
app_name = os.getenv("TODO_APP_NAME")

if max_tasks_value is None:
    sys.stderr.write("ERROR... TODO_MAX_TASKS is missing from .env\n")
    sys.exit(1)

if app_name is None or app_name.strip() == "":
    sys.stderr.write("ERROR... TODO_APP_NAME is missing or empty in .env\n")
    sys.exit(1)

try:
    max_tasks = int(max_tasks_value)
except ValueError:
    sys.stderr.write("ERROR... TODO_MAX_TASKS must be a number\n")
    sys.exit(1)

if max_tasks <= 0:
    sys.stderr.write("ERROR... TODO_MAX_TASKS must be greater than 0\n")
    sys.exit(1)

tasks = []


def commands_work(command_example):

    if len(command_example) < 2:
        print(app_name)
        print("add <something>")
        print("list")
        print("remove <number>")
        print("exit")

        while True:
            user_command = input("give a command to the service: ")
            user_args = user_command.split()

            if len(user_args) == 0:
                sys.stderr.write("ERROR... you need to give a command\n")
                continue

            if user_args[0] == "exit":
                sys.exit()

            elif user_args[0] == "list":
                if len(tasks) == 0:
                    print("Your task list is empty.")
                else:
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task}")

            elif user_args[0] == "add":
                if len(tasks) >= max_tasks:
                    sys.stderr.write(
                        f"ERROR... you had reached your tasks limit. "
                        f"You have {max_tasks} tasks\n"
                    )
                else:
                    if len(user_args) < 2:
                        sys.stderr.write("ERROR... you need to give a task\n")
                        print("add <something>")
                    else:
                        add_example = " ".join(user_args[1:])
                        tasks.append(add_example)

            elif user_args[0] == "remove":
                if len(user_args) < 2:
                    sys.stderr.write("ERROR... you need to give a task number\n")
                    print("remove <number>")
                else:
                    try:
                        task_number = int(user_args[1])
                    except ValueError:
                        sys.stderr.write("ERROR... task number must be a number\n")
                    else:
                        if task_number < 1 or task_number > len(tasks):
                            sys.stderr.write("ERROR... that task number does not exist\n")
                        else:
                            tasks.pop(task_number - 1)

            else:
                sys.stderr.write("ERROR... the command is not recognized\n")
                print("add <something>")
                print("list")
                print("remove <number>")
                print("exit")

    if command_example[1] == "list":
        if len(tasks) == 0:
            print("Your task list is empty.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

    elif command_example[1] == "add":
        if len(tasks) >= max_tasks:
            sys.stderr.write(
                f"ERROR... you had reached your tasks limit. "
                f"You have {max_tasks} tasks\n"
            )
        else:
            if len(command_example) < 3:
                sys.stderr.write("ERROR... you need to give a task\n")
                print("add <something>")
            else:
                add_example = " ".join(command_example[2:])
                tasks.append(add_example)

    elif command_example[1] == "remove":
        if len(command_example) < 3:
            sys.stderr.write("ERROR... you need to give a task number\n")
            print("remove <number>")
        else:
            try:
                task_number = int(command_example[2])
            except ValueError:
                sys.stderr.write("ERROR... task number must be a number\n")
            else:
                if task_number < 1 or task_number > len(tasks):
                    sys.stderr.write("ERROR... that task number does not exist\n")
                else:
                    tasks.pop(task_number - 1)

    elif command_example[1] == "exit":
        sys.exit()

    else:
        sys.stderr.write("ERROR... the command is not recognized\n")
        print("add <something>")
        print("list")
        print("remove <number>")
        print("exit")


commands = sys.argv

commands_work(commands)