# Smile-Detection-with-Python-Flask

## Getting Started

### Folder Structure
```
.
|-- main.py
|-- README.md
|   +-- haar_cascade
|   |   |-- haarcascade_frontalface_default.xml
|   |   |-- haarcascade_smile.xml
|   +-- model
|   |   |   |-- keras_metadata.pb
|   |   |   |-- saved_model.pb
|   |   +-- variables
|   |   |   |-- variables.data
|   |   |   |-- variables.index
```
Ensure you create directory in your directory.

`git clone https://github.com/aminshokripwa/Smile-Detection-with-Python-Flask.git`

## Download the packages used to create this rest API
RMake sure to install python and and upgrade pip to the latest version.

```
python -m pip install --upgrade pip setuptools wheel
```

```
pip install -r requirments.txt
```

## Running the project as developer

`main.py`

## Running the project on server

To run on the server, in the main.py file, change the last line to open server port and connect with your server IP.

`app.run(host='0.0.0.0', port=80)`

## API Endpoints & Usage

To be able to login, you need to use the create new user endpoint to set up a user account.

* POST    `api/v1/face` Send image file by Postman(Smile-Detection-with-Python-Flask.postman_collection.json)

```

    "imagefile": "Image file"

```

*** Output ***

Displays the smile status for the selected photo

```
["message": Not Smiling,"status": true]"

```