from flask import Flask

app = Flask(__name__)

@app.get("/")
def read_root():
    return {"Hello": "World .---."}

app.run(host="0.0.0.0")  ##port=4000