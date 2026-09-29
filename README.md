# CLI To-Do App

A simple command-line To-Do application built with Python.

## Features

* Add tasks from the command line
* Store tasks in a list
* Set the maximum number of tasks using a `.env` file
* Set the app name using a `.env` file
* Save and load tasks using JSON
* Use command-line arguments to control the app

## Requirements

* Python 3
* python-dotenv

Install the required package with:

```bash
pip install python-dotenv
```

## Usage

Run the program from the terminal and provide a command.

Example:

```bash
python todo.py add "Finish Python project"
```

The app will add the task to your To-Do list.

Tasks can be saved to a JSON file so they are still available when the program is started again.

## Configuration

The app uses a `.env` file for configuration.

Example:

```env
TODO_MAX_TASKS=100
TODO_APP_NAME=My To-Do List
```

`TODO_MAX_TASKS` controls the maximum number of tasks that can be stored.

`TODO_APP_NAME` sets the name displayed by the application.

## Example Output

```text
My To-Do List

Task added: Finish Python project

Tasks:
1. Finish Python project
```

## Technologies

* Python
* JSON
* python-dotenv
* Command-line arguments
