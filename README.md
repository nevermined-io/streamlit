# Nevermined Streamlit Demo App

## Running locally

```bash
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ streamlit run nevermined-app.py
```

## Integrating the widget in a streamlit app

Start by adding the widget to your app with the _did_ of your webservice (e.g. `did:nv:5a06236a0bb1620c171a17a2e4d82935b1b63274011aeb1d9efcce87e83f0fee`).

```python
st.markdown('<iframe src="https://testing.nevermined.app/streamlit?did=did:nv:5a06236a0bb1620c171a17a2e4d82935b1b63274011aeb1d9efcce87e83f0fee" style="border-radius: 10px; width: 100%;" />', unsafe_allow_html=True)
```

Wait for the user authentication token and proxy url. This should be added at the end of the app not to block other elements from rendering

```python
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
    if token:
        st.session_state["nvm"] = {
            "jwt": token["data"]["jwtToken"]["accessToken"],
            "url": f'{token["data"]["proxyUrl"]}/ask'
        }
        break
    time.sleep(1)
```

Use the returned authentication token and proxy url to make calls to the service. For example:

```python
token = st.session_state["nvm"]["jwt"]
url = st.session_state["nvm"]["url"]

data = {"payload": "payload to post to the service"}
headers = {"Authorization": f"Bearer {token}"}

response = requests.post(url, json=data, headers=headers)
```

## What's the DID?

The _did_ is the unique identifier of any asset existing on Nevermined. You can get the _did_ from the url of the service on the Nevermined App. For example on this url:

```
https://testing.nevermined.app/streamlit?did=did:nv:5a06236a0bb1620c171a17a2e4d82935b1b63274011aeb1d9efcce87e83f0fee
```

The _did_ is the identifier of the webservice starting by `did:nv:`. Meaning in this case the _did_ is `did:nv:5a06236a0bb1620c171a17a2e4d82935b1b63274011aeb1d9efcce87e83f0fee`
