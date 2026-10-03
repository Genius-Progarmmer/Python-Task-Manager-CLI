# My To-Do List

A simple command-line To-Do List application built with Python. It allows you to add, view, and remove tasks while automatically saving them to a JSON file so your tasks remain available after restarting the program.

## Features

* Add tasks
* List all saved tasks
* Remove tasks by number
* Automatically save tasks to `memory.json`
* Load saved tasks when the program starts
* Set a maximum number of tasks
* Set a custom app name
* Handle invalid commands and inputs
* Handle missing or invalid configuration
* Handle missing or invalid task data

## Requirements

* Python
* `python-dotenv`

## Setup

1. Install the required package:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file based on `.env.example`.

3. Set the maximum number of tasks and the app name in `.env`.

Example:

```env
TODO_MAX_TASKS=100
TODO_APP_NAME=My To-Do List
```

4. Run the program:

```bash
python todo.py
```

## Commands

```text
add <something>
list
remove <number>
exit
```

You can also run commands directly when starting the program:

```bash
python todo.py add Finish homework
python todo.py list
python todo.py remove 1
python todo.py exit
```

## Example Output

```text
My To-Do List
add <something>
list
remove <number>
exit

give a command to the service: add Finish Python project
give a command to the service: add Read a book
give a command to the service: list

1. Finish Python project
2. Read a book

give a command to the service: remove 1
give a command to the service: list

1. Read a book
```

Tasks are stored in `memory.json` and automatically loaded when the program starts again.

## Files

```text
todo.py
.env
.env.example
.gitignore
requirements.txt
memory.json
```

`.env` contains the app configuration, while `memory.json` stores the saved tasks.
