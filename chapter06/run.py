from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def example():
    return 'example'

if __name__ == "__main__":
	app.run()