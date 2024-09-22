from flask import Flask
from flask import Flask, render_template

app=Flask(__name__)


@app.route('/')
def home():
  return "<p>een tekst naar keuze</p>"

if __name__ == '__main__':
 app.run(port=5000,debug=True)
