
import streamlit as st
import streamlit.components.v1 as stc
# from streamlit_drawable_canvas import st_canvas
# from streamlit_cropper import st_cropper

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

st.image('aaa.jpg')

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
