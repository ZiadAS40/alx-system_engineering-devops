#!/usr/bin/python3
"""Returns an information about to-do list for a given employee ID."""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    csv_file = "{}.csv".format(sys.argv[1])
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow(("{}".format(sys.argv[1]), "{}"
                            .format(user.get("name")), "{}"
                            .format(True if todo.get("completed")
                            else False), "{}".format(todo.get("title"))))
