"""
シンプルなCLIタスク管理ツール
"""


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


def print_tasks(tasks):
    """
    タスク一覧を見やすく表示する関数
    """
    if not tasks:
        print("タスクはまだありません。")
        return

    for i, task in enumerate(get_tasks(tasks), start=1):
        status = "✅" if task["done"] else "⬜"
        print(f"{i}. {status} {task['name']}")


if __name__ == "__main__":
    # 動作確認用の簡単なサンプル実行
    tasks = []
    add_task(tasks, "牛乳を買う")
    add_task(tasks, "レポートを書く")

    print("=== タスク一覧 ===")
    print_tasks(tasks)
