import time
import streamlit as st
from streamlit_javascript import st_javascript
from streamlit.components.v1 import html

st.markdown('<iframe src="http://localhost:3000/streamlit?did=did:nv:4a72bef4b755094f70f40e17b9edf82ea0efafc466098b61a2a47ee9874d4251" style="border-radius: 10px; width: 100%;" />', unsafe_allow_html=True)

html("""
<script>
    parent.window.addEventListener('message', (e) => {
        if (e.data.type === 'streamlit:token') {
            parent.window.token = e.data.token;
        }
    },false);
</script>
""")

key = 0
while True:
    key += 1
    token = st_javascript('parent.window.token', key=key)
    if token:
        # print(token)
        break
    time.sleep(1)
