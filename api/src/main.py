from github import Github


def main():
    g = Github()
    user = g.get_user("RuikisR")
    for repo in user.get_repos():
        print(repo.name)


if __name__ == '__main__':
    main()
