from flask import Flask

app = Flask(__name__)

@app.route('/')
def example():
    return 'example'

@app.route('/foo')
def example_foo():
    return 'foo'

@app.route('/bar')
def another_example():
    return '<b>bold text</b> - normal text'

@app.route('/foo/abc')
def example_again():
    return 'abc'

if __name__ == "__main__":
	app.run()