from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<login>')
def redirect(login):
    return render_template('redirect.html')

@app.route('/static/css/<path:path>')
def send_css(path):
    print(path)
    return send_from_directory('templates/css/', path)

@app.route('/static/js/<path:path>')
def send_js(path):
    return send_from_directory('templates/js/', path)

if __name__ == '__main__':
    app.run(host = "0.0.0.0")
