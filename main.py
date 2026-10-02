import requests
import argparse


def get_todo(todo_id):
    url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"

    try:
        response = requests.get("https://jsonplaceholder.typicode.com/todos")
    except requests.exceptions.RequestException:
        print("APIへの接続に失敗しました")

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("APIからデータを取得できませんでした")

parser = argparse.ArgumentParser()
# parser.add_argument("id", type=int)

subparsers = parser.add_subparsers()

get_parser = subparsers.add_parser("get")
get_parser.add_argument("id", type=int)
get_parser.set_defaults(command="get")

list_parser = subparsers.add_parser("list")
list_parser.set_defaults(command="list")

args = parser.parse_args()

print(args)

# data = get_todo(args.id)



