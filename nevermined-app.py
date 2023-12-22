import time
import streamlit as st
from streamlit_javascript import st_javascript
from streamlit.components.v1 import html
import requests

def ask_elvis(prompt, url, token):
    data = {
        "queries": [
            {
                "query": prompt,
                "top_k": 3
            }
        ]
    }
    headers = {
        "Authorization": f"Bearer {token}"
    }

    print(url, data, headers)
    response = requests.post(url, json=data, headers=headers)
    print(response.status_code, response.text)
    if response.ok:
        return response.text
    else:
        return "There was a problem with the prompt"


st.markdown('<iframe src="https://goerli.nevermined.one/streamlit?did=did:nv:257a5999aa3bc96510a931184dc8afaa42dbb8f4e61ac47a03bbb546edd1b860" style="border-radius: 10px; width: 100%;" />', unsafe_allow_html=True)

if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("ai"):
        if "nvm" in st.session_state:
            jwt = st.session_state["nvm"]["jwt"]
            url = st.session_state["nvm"]["url"]
            response = ask_elvis(prompt, url, jwt)
            
            st.markdown(response)
        else:
            st.markdown("Please login or subscribe first!")

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
while "nvm" not in st.session_state:
    key += 1
    token = st_javascript('parent.window.token', key=key)
    print(token)
    if token:
        print(token)
        st.session_state["nvm"] = {
            "jwt": token["data"]["jwtToken"]["accessToken"],
            "url": f'{token["data"]["proxyUrl"]}/ask'
        }
        break
    time.sleep(1)