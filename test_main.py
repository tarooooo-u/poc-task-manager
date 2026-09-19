"""
main.py の動作をチェックするテストコード
pytest を使って実行します
"""

from main import add_task, get_tasks


def test_add_task_adds_one_item():
    """タスクを1つ追加したとき、リストの長さが1になるか"""
    tasks = []
    add_task(tasks, "洗濯する")
    assert len(tasks) == 1


def test_add_task_stores_correct_name():
    """追加したタスクの名前が正しく保存されているか"""
    tasks = []
    add_task(tasks, "洗濯する")
    assert tasks[0]["name"] == "洗濯する"


def test_add_task_default_done_is_false():
    """新しいタスクは完了(done)がFalseの状態で追加されるか"""
    tasks = []
    add_task(tasks, "洗濯する")
    assert tasks[0]["done"] is False


def test_add_task_multiple_items():
    """複数のタスクを追加したとき、正しい数になるか"""
    tasks = []
    add_task(tasks, "タスク1")
    add_task(tasks, "タスク2")
    assert len(tasks) == 2


def test_get_tasks_empty_list():
    """タスクが1つもないとき、空のリストが返るか"""
    tasks = []
    assert get_tasks(tasks) == []


def test_get_tasks_returns_same_list():
    """get_tasksが渡したリストと同じ内容を返すか"""
    tasks = []
    add_task(tasks, "サンプルタスク")
    result = get_tasks(tasks)
    assert result == tasks
