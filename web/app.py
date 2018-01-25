from flask import Flask, render_template
import os

app = Flask(__name__)


@app.errorhandler(404)   # 404 error handler
def error_404(e):
    return render_template('404.html'), 404


@app.errorhandler(403)   # 403 error handler
def error_403(e):
    return render_template('403.html'), 403


@app.route('/<string:name>')
def hello(name):
    if name.endswith('.html') or name.endswith('.css'):    # Check if the path ends with .html or .css
        if '//' not in name and '..' not in name and '~' not in name: # Check if the path has '//', '..' or '~'
            filename = './templates/%s' % name
            if os.path.isfile(filename):  # Check if the file exists
                return render_template('/%s' % name)
            else:
                return error_404(404)
        else:
            return error_403(403)
    else:
        return error_403(403)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
