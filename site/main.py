from github import Github
from flask import Flask, render_template, request

app = Flask(__name__)
g = Github()


@app.route('/')
def root():
    search = request.args.get('uname')
    if search is None:
        title = ""
        data = None
    else:
        title = f"Commit data for {search}"
        data = get_data(search)
    return render_template('gh.html', data=data, title=title)


def get_data(search):
    data = None
    try:
        user = g.get_user(search)
        repos = user.get_repos()
        data = {}
        for repo in repos:
            commits = repo.get_commits(author=user).totalCount
            data[repo.name] = commits
    except Exception as e:
        print(e)
    return data


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
