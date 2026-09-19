# CLI タスク管理ツール
Pythonで作られた、シンプルなコマンドラインのタスク管理ツールです。

## できること
- タスクの追加（`add_task`）
- タスク一覧の取得（`get_tasks`）

## ファイル構成

```
.
├── main.py          # タスク管理の基本コード
├── test_main.py     # pytest用のテストコード
├── .gitignore        # Gitで管理しないファイルの指定
└── README.md         # このファイル
```

## セットアップ方法

### 1. 仮想環境の作成・有効化

```bash
python -m venv venv
```

Mac / Linux の場合:
```bash
source venv/bin/activate
```

Windows の場合:
```bash
venv\Scripts\activate
```

### 2. 必要なパッケージのインストール

```bash
pip install pytest
```

### 3. 動作確認

```bash
python main.py
```

### 4. テストの実行

```bash
pytest
```

## 今後の拡張アイデア

- タスクの削除機能
- タスクを完了にする機能
- タスクをファイルに保存して次回起動時も読み込む機能
- コマンドライン引数（`argparse`）でCLI操作をもっと便利にする
