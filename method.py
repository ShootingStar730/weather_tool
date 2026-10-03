import requests

def get_todo(todo_id):
    url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        print("APIへの接続に失敗しました")

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("APIからデータを取得できませんでした")

def get_todos():
    url = f"https://jsonplaceholder.typicode.com/todos"
    
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        print("APIへの接続に失敗しました")

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("APIからデータを取得できませんでした")

def add_todo(title):
    url = f"https://jsonplaceholder.typicode.com/todos"

    todo = {
        "id": 5,
        "title": title,
        "completed": False,
        "userId": 1
    }

    try:
        response = requests.post(url, json=todo)
    except requests.exceptions.RequestException:
        print("APIへの接続に失敗しました")
    
    if response.status_code == 201:
        data = response.json()
        return data
    else:
        print("TODOの追加に失敗しました")

def complete_todo(todo_id):
    url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"

    todo = {
        "completed": True
    }

    response = requests.put(url, json=todo)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("TODOの更新に失敗しました")

def delete_todo(todo_id):
    url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"

    response = requests.delete(url)

    if response.status_code == 204:
        return True
    else:
        return False