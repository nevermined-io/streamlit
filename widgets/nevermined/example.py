import time
import streamlit as st
from streamlit_javascript import st_javascript
from streamlit.components.v1 import html

st.markdown('<iframe src="http://localhost:3000/streamlit?did=did:nv:b0fb4abcfd49be732d828f9e58c5aa28f334960cd58efb4c6ef2f66697460745" style="border-radius: 10px; width: 100%;" />', unsafe_allow_html=True)

html("""
<script>
    parent.window.addEventListener('message', (e) => {
        if (e.data.type === 'streamlit:token') {
            parent.window.token = e.data;
        }
    },false);
</script>
""", height=0)

key = 0
while True:
    key += 1
    token = st_javascript('parent.window.token', key=key)
    if token:
        print(token)
        break
    time.sleep(5)
