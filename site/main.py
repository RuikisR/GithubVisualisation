#from github import Github
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def root():
    return render_template('gh.html')


'''
def main():
    g = Github()
    user = g.get_user("RuikisR")
    for repo in user.get_repos():
        print(repo.name)

'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')