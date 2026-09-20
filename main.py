"""
シンプルなCLIタスク管理ツール

使い方:
    python main.py add "タスク名"   タスクを追加する
    python main.py list             タスク一覧を表示する
    python main.py done <ID>        指定したIDのタスクを完了にする
"""

import argparse
import json
import os

TASKS_FILE = "tasks.json"


def add_task(tasks, task_name):
    """
    タスクをリストに追加する関数

    Parameters:
        tasks (list): タスクを格納するリスト
        task_name (str): 追加したいタスクの名前

    Returns:
        list: タスクが追加された後のリスト
    """
    task = {"name": task_name, "done": False}
    tasks.append(task)
    return tasks


def get_tasks(tasks):
    """
    タスク一覧を取得する関数

    Parameters:
        tasks (list): タスクを格納するリスト

    Returns:
        list: タスクのリスト
    """
    return tasks


def complete_task(tasks, task_id):
    """
    指定したIDのタスクを完了状態にする関数

    Parameters:
        tasks (list): タスクを格納するリスト
        task_id (int): 完了にしたいタスクの番号（1始まり。list表示の番号と対応）

    Returns:
        bool: 完了状態への更新に成功したら True、
              該当するIDが存在しなければ False
    """
    index = task_id - 1  # リストは0始まりなので、表示上の番号(1始まり)から1引く

    if index < 0 or index >= len(tasks):
        return False

    tasks[index]["done"] = True
    return True


def print_tasks(tasks):
    """
    タスク一覧を見やすく表示する関数
    完了しているタスクは [x]、未完了のタスクは [ ] で表示する
    """
    if not tasks:
        print("タスクはまだありません。")
        return

    for i, task in enumerate(get_tasks(tasks), start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{i}. {status} {task['name']}")


def load_tasks(filepath=TASKS_FILE):
    """
    JSONファイルからタスク一覧を読み込む関数。
    ファイルがまだ無い場合は空のリストを返す。
    """
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks, filepath=TASKS_FILE):
    """
    タスク一覧をJSONファイルに保存する関数
    """
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def main():
    parser = argparse.ArgumentParser(description="シンプルなCLIタスク管理ツール")
    subparsers = parser.add_subparsers(dest="command")

    # add コマンドの定義
    add_parser = subparsers.add_parser("add", help="タスクを追加する")
    add_parser.add_argument("task_name", help="追加するタスクの名前")

    # list コマンドの定義
    subparsers.add_parser("list", help="タスク一覧を表示する")

    # done コマンドの定義
    done_parser = subparsers.add_parser("done", help="指定したIDのタスクを完了にする")
    done_parser.add_argument("task_id", type=int, help="完了にするタスクの番号（listの番号）")

    args = parser.parse_args()

    # 保存されているタスクを読み込む
    tasks = load_tasks()

    if args.command == "add":
        add_task(tasks, args.task_name)
        save_tasks(tasks)
        print(f"タスクを追加しました: {args.task_name}")
        print()
        print("=== タスク一覧 ===")
        print_tasks(tasks)

    elif args.command == "list":
        print("=== タスク一覧 ===")
        print_tasks(tasks)

    elif args.command == "done":
        success = complete_task(tasks, args.task_id)
        if success:
            save_tasks(tasks)
            print(f"タスク {args.task_id} を完了にしました。")
            print()
            print("=== タスク一覧 ===")
            print_tasks(tasks)
        else:
            print(f"エラー: ID {args.task_id} のタスクが見つかりません。")

    else:
        # コマンドが指定されなかった場合はヘルプを表示
        parser.print_help()


if __name__ == "__main__":
    main()