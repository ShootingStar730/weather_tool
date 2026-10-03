import argparse
import requests

from method import get_todo
from method import get_todos
from method import add_todo
from method import complete_todo
from method import delete_todo

parser = argparse.ArgumentParser()
# parser.add_argument("id", type=int)

subparsers = parser.add_subparsers()

get_parser = subparsers.add_parser("get")
get_parser.add_argument("id", type=int)
get_parser.set_defaults(command="get")

list_parser = subparsers.add_parser("list")
list_parser.add_argument("--limit", type=int)
list_parser.set_defaults(command="list")

add_parser = subparsers.add_parser("add")
add_parser.add_argument("title")
add_parser.set_defaults(command="add")

done_parser = subparsers.add_parser("done")
done_parser.add_argument("id", type=int)
done_parser.set_defaults(command="done")

delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("id", type=int)
delete_parser.set_defaults(command="delete")

args = parser.parse_args()

if args.command == "get":
    data = get_todo(args.id)

    print(data["title"])
elif args.command == "list":
    data = get_todos(args.limit)

    for todo in data:
        print(f"{todo["id"]}: {todo["title"]}")
elif args.command == "add":
    data = add_todo(args.title)

    print(f"{data["id"]}: {data["title"]}")
elif args.command == "done":
    data  = complete_todo(args.id)

    print(F"{data["id"]}: 完了しました")
elif args.command == "delete":
    res = delete_todo(args.id)

    if res:
        print(f"{args.id}: 削除しました")
    else:
        print("TODOの削除に失敗しました")

# print(args)

# data = get_todo(args.id)



