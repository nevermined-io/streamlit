# Nevermined Streamlit Components

## Quickstart

* Ensure you have [Python 3.6+](https://www.python.org/downloads/), [Node.js](https://nodejs.org), and [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) installed.
* Clone this repo.
* Create a new Python virtual environment for the template:
```
$ cd widgets
$ python3 -m venv venv  # create venv
$ . venv/bin/activate   # activate venv
$ pip install streamlit # install streamlit
```
* Initialize and run the component template frontend:
```
$ cd widgets/nevermined
$ npm install    # Install npm dependencies
$ npm run start  # Start the Webpack dev server
```
* From a separate terminal, run the template's Streamlit app:
```
$ cd widgets
$ . venv/bin/activate  # activate the venv you created earlier
$ pip install -e . # install template as editable package
$ streamlit run nevermined/example.py  # run the example
```
* Modify the Python code at `widgets/nevermined/__init__.py`.
