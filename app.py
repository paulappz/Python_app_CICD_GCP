from flask import Flask
app = Flask('hello')
@app.route('/')
def hello():
  return "Hello Paul!\n"
if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)
