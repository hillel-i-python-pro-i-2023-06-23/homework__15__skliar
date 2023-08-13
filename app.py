from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():  # put application's code here
    return (
        "Hello World! || \n http://127.0.0.1:5000/hello-query?name=pep&number=1 "
        "|| \n http://127.0.0.1:5000/hello/pep/12"
    )


@app.route("/hello/<string:name>/<int:number>")
def hello(name, number):
    return f"Hello {name}! Your number is {number}."


@app.route("/hello-query")
def hello_query():
    name = request.args.get("name", "Guest")
    number = request.args.get("number", 0, type=int)
    return f"Hello {name}! Your number is {number}."


if __name__ == "__main__":
    app.run()
