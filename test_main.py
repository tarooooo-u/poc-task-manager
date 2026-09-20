"""
main.py の動作をチェックするテストコード
pytest を使って実行します
"""

from main import add_task, get_tasks, complete_task


# --- add_task のテスト ---

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


# --- get_tasks のテスト ---

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


# --- complete_task のテスト ---

def test_complete_task_marks_done_true():
    """指定したIDのタスクのdoneがTrueになるか"""
    tasks = []
    add_task(tasks, "タスク1")
    complete_task(tasks, 1)
    assert tasks[0]["done"] is True


def test_complete_task_returns_true_on_success():
    """完了に成功したとき、戻り値がTrueになるか"""
    tasks = []
    add_task(tasks, "タスク1")
    result = complete_task(tasks, 1)
    assert result is True


def test_complete_task_only_affects_target_task():
    """指定したID以外のタスクのdoneが変わらないか"""
    tasks = []
    add_task(tasks, "タスク1")
    add_task(tasks, "タスク2")
    complete_task(tasks, 2)
    assert tasks[0]["done"] is False
    assert tasks[1]["done"] is True


def test_complete_task_invalid_id_returns_false():
    """存在しないIDを指定したとき、戻り値がFalseになるか"""
    tasks = []
    add_task(tasks, "タスク1")
    result = complete_task(tasks, 99)
    assert result is False


def test_complete_task_invalid_id_does_not_crash_data():
    """存在しないIDを指定しても、既存タスクのdoneが変わらないか"""
    tasks = []
    add_task(tasks, "タスク1")
    complete_task(tasks, 99)
    assert tasks[0]["done"] is False


def test_complete_task_zero_id_returns_false():
    """ID 0 (存在しない番号) を指定したとき、Falseになるか"""
    tasks = []
    add_task(tasks, "タスク1")
    result = complete_task(tasks, 0)
    assert result is False


def test_complete_task_negative_id_returns_false():
    """マイナスのIDを指定したとき、Falseになるか"""
    tasks = []
    add_task(tasks, "タスク1")
    result = complete_task(tasks, -1)
    assert result is False