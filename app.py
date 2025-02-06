from flask import Flask

app= Flask(__name__)

@app.route('/')
def hello_word():
    return 'hello word '

if __name__== '__-main__':
    app.run(debug=True)
