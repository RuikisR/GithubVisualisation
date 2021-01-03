from github import Github
from flask import Flask, render_template, request

app = Flask(__name__)
g = Github()


@app.route('/')
def root():
    search = request.args.get('uname')
    if search is None:
        title = "Yeet"
    else:
        title = f"Data for {search}"
    data = ""
    return render_template('gh.html', data=data, title=title)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
