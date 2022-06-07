from flask import Flask, render_template

app = Flask(__name__)

#rendering the HTML page which has the button
@app.route('/json')
def json():
  return render_template('json.html')

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
  print ("Hello")
  return ("nothing")

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/cakes')
def cakes():
  return render_template('cakes.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
