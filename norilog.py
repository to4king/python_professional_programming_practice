import json

DATA_FILE = 'norilog.json'


def save_data(start, finish, memo, created_at):
    """記録データを保存します
    :param start: 乗った駅
    :type start: str
    :param finish: 降りた駅
    :type finish: str
    :param memo: 乗り降りのメモ
    :type memo: str
    :param created_at: ノリノリの日付
    :type created_at: datetime.datetime
    :return None
    """
    with open(DATA_FILE, mode="r", encoding="utf-8") as f:
        try:
            # json モジュールでデータベースファイルを開きます
            database = json.load(f)
        except FileNotFoundError:
            database = []

        database = {
            "start": start,
            "finish": finish,
            "memo": memo,
            "created_at": created_at.strftime("%Y-%m-%d %H:%M")
        }

        json.dump(database, open(DATA_FILE, mode="w", encoding="utf-8"), indent=4, ensure_ascii=False)


def load_data():
    """記録データを返す"""
    with open(DATA_FILE, mode="r", encoding="utf-8") as f:
        try:
            # json モジュールでデータベースファイルを開きます
            database = json.load(f)
        except FileNotFoundError:
            database = []
        return database

