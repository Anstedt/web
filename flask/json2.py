from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/')
def json2():
    return render_template('json2.html')

@app.route('/SomeFunction')
def SomeFunction():
    print('Printed From SomeFunction')
    return "Nothing"

@app.route('/YrFunction')
def YrFunction():
    print('Printed From YourFunction')
    return "Nothing"

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
