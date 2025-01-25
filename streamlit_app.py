 x = 10
 'x: ', x 

import streamlit as st
import streamlit.components.v1 as stc

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

