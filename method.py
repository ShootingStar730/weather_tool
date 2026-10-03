import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

def get_todo(todo_id):
    url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        print("APIへの接続に失敗しました")
        return None

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("APIからデータを取得できませんでした")

def get_todos(limit):
    url = f"https://jsonplaceholder.typicode.com/todos"

    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    try:
        params = {"_limit": limit} if limit else None

        response = requests.get(url, params=params, headers=headers)

    except requests.exceptions.RequestException:
        print("APIへの接続に失敗しました")
        return None

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
        return None
    
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

    try:
        response = requests.put(url, json=todo)
    except requests.exceptions.RequestException:
        print("APIへの接続に失敗しました")
        return None

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("TODOの更新に失敗しました")

def delete_todo(todo_id):
    url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
    try:
        response = requests.delete(url)
        print(response.status_code)
        print(response.text)

    except requests.exceptions.RequestException:
        print("APIへの接続に失敗しました")
        return False
    
    if response.status_code == 200:
        return True
    else:
        return False