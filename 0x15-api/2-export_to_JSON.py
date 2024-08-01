#!/usr/bin/python3
"""Returns an information about to-do list for a given employee ID."""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    user_id = "{}".format(sys.argv[1])
    json_file = "{}.json".format(sys.argv[1])
    my_dict = ({user_id: [{"task": t.get("title"),
                           "completed": t.get("completed"),
                           "username": user.get("username")}for t in todos]})

    with open(json_file, mode='w') as file:
        json.dump(my_dict, file)
