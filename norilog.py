import json

from flask import Flask, render_template, request, redirect
from datetime import datetime

application = Flask(__name__)

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

        database.append({
            "start": start,
            "finish": finish,
            "memo": memo,
            "created_at": created_at.strftime("%Y-%m-%d %H:%M")
        })

        json.dump(database, open(DATA_FILE, mode="w", encoding="utf-8"), indent=4, ensure_ascii=False)


def load_data():
    """記録データを返す"""
    try:
        # json モジュールでデータベースファイルを開きます
        database = json.load(open(DATA_FILE, mode="r", encoding="utf-8"))
    except FileNotFoundError:
        database = []
    return database


@application.route('/')
def index():
    """トップページ
    テンプレートを使用してページを表示します
    """
    # 記録されているデータを読み込む
    rides = load_data()
    return render_template('index.html', rides=rides)


@application.route('/save', methods=['POST'])
def save():
    """記録用 URL"""
    # 記録用データを取得する
    start = request.form.get('start')  # 出発
    finish = request.form.get('finish')  # 到着
    memo = request.form.get('memo')  # メモ
    created_at = datetime.now()  # 記録時間（現在時間）を保存します

    save_data(start, finish, memo, created_at)

    # 保存後はトップページにリダイレクトします。
    return redirect('/')


if __name__ == '__main__':
    # IPアドレス0.0.0.0の8000番ポートでアプリケーションを実行します
    application.run('0.0.0.0', 8000, debug=True)
