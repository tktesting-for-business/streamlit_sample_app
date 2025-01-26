
import streamlit as st
import streamlit.components.v1 as stc
from streamlit_drawable_canvas import st_canvas
#　モジュールの読み込み
from PIL import Image

import requests
from typing import Dict

# Streamlit app タイトル
st.title("Drawable Canvas Demo")


# キャンバスの設定
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # 塗りつぶしの色
    stroke_width=2,  # 線の太さ
    stroke_color="#000000",  # 線の色
    background_color="#FFF",  # 背景色
    background_image=None,  # 背景画像（なし）
    # background_image=img,  # 背景画像
    update_streamlit=True,  # Streamlitをリアルタイムで更新
    height=150,  # キャンバスの高さ
    drawing_mode="rect",  # 描画モード（矩形）
    key="canvas",  # キャンバスのキー
)

# 描画結果の表示
if canvas_result.json_data is not None:
    st.json(canvas_result.json_data)


st.title("Embedding Dify app in Streamlit")
# Case 1の場合
st.write("## Case 1.")
# iFrameのHTMLコード
html_code = """
<iframe
 src="https://udify.app/chatbot/H91lTD4M0KqfMpYk"
 style="width: 100%; height: 100%; min-height: 700px"
 frameborder="0"
 allow="microphone">
</iframe>
"""
# HTMLをStreamlitアプリに埋め込む
stc.html(html_code, height=800)

# Test Case
st.write("## Case 天気予報")
API_KEY = 'app-esamNSyt3DcelD4o6yM9uH4U'  # 取得したAPIキーに置き換えてください

# Dify APIのベースURL
BASE_URL = 'https://api.dify.ai/v1/workflows/run'

def get_dify_response(query: str) -> str:
    """
    Dify APIにリクエストを送信し、応答を取得する関数
    :param query: ユーザーの質問
    :return: APIからの応答テキスト
    """
    headers = {
        'Authorization': f"Bearer {API_KEY}",
        'Content-Type': 'application/json'
    }
    
    data = {
        "inputs": {"inTest": query},
        "response_mode": "blocking",
        "user": "taka3chijp@gmail.com"
    }
    
    response = requests.post(BASE_URL, headers=headers, json=data)
    response.raise_for_status()

    return response.json()['data']['outputs']['output']


if __name__ == "__main__":
    try:
        # テキストボックス
        query = st.text_input("天気を知りたい場所を入力してください")
        if query:
            answer = get_dify_response(query)
            st.write(answer)
        else:
            st.write("地域が入力されていません")
        
    except requests.RequestException as e:
        st.write(f"エラーが発生しました: {e}")

