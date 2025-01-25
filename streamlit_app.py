
import streamlit as st
import streamlit.components.v1 as stc
from streamlit_drawable_canvas import st_canvas
#　モジュールの読み込み
from PIL import Image

# Streamlit app タイトル
st.title("Drawable Canvas Demo")
img=Image.Open('aaa.jpg')
st.Image(img)
#img = Image.open('aaa.png')
#st.image(img, caption='サンプル',use_column_width=True)

# キャンバスの設定
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # 塗りつぶしの色
    stroke_width=2,  # 線の太さ
    stroke_color="#000000",  # 線の色
    background_color="#FFF",  # 背景色
    background_image=None,  # 背景画像（なし）
    #background_image=img,  # 背景画像
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
 src="https://udify.app/chatbot/jGTwlTKwnlbTFs0M"
 style="width: 100%; height: 100%; min-height: 700px"
 frameborder="0"
 allow="microphone">
</iframe>
"""
# HTMLをStreamlitアプリに埋め込む
stc.html(html_code, height=800)
# Case 2の場合
st.write("## Case 2.")
# HTMLとJavaScriptを埋め込む
html_code = """
<img id="myImage" src="aaa.jpg" alt="Target Image" style="display: none;">
<canvas id="myCanvas"></canvas>
<script>
  const img = document.getElementById('myImage');
  const canvas = document.getElementById('myCanvas');
  const ctx = canvas.getContext('2d');

  img.onload = () => {
    canvas.width = img.width * 2;
    canvas.height = img.height * 2;
    ctx.scale(2, 2);
    ctx.drawImage(img, 0, 0);

    // テキストの位置とサイズ (手動で指定)
    const x = 123;
    const y = 135;
    const w = 98;
    const h = 21;

    // 赤い枠を描画する
    ctx.strokeStyle = 'red';
    ctx.lineWidth = 2;
    ctx.strokeRect(x, y, w, h);
  };
</script>
"""

stc.html(html_code, height=700)
