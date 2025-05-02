# server.pyの中身
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
  # WebAPIを取得しに行く。
  url = "https://weather.tsukumijima.net/api/forecast/"
  #400040は福岡県・久留米だけど、東京都・東京の番号に変更してくださいね。
  city_code = "city/130010"
  # 取得したWebAPIのデータをtenki_dataに代入（格納）
  # .json()でJSON形式に変換しています。
  # Pythonのデータ構造（辞書型・dict型）として利用できる。
  tenki_data = requests.get(url+city_code).json()
  title = tenki_data["title"]
  
  return render_template('index.html',
                         title=title,
                         tenki_data=tenki_data)

if __name__ == "__main__":
  app.run(debug=True)
