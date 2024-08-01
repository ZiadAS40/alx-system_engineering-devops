#!/usr/bin/python3
"""Returns an information about to-do list for a given employee ID."""
import requests
import sys
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    json_file = "todo_all_employees.json"
    my_dict = ({user.get("id"): [{"task": todo.get("title"),
                                  "completed": todo.get("completed"),
                                  "username": user.get("name")}
                                  for todo in todos] for user in users})

    with open(json_file, mode='w') as file:
        json.dump(my_dict, file)
