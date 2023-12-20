from github import Github


def pull_request(repo_name):
    g = Github(
        "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"
    )
    user = g.get_user()
    repo = g.get_repo("contek-io/{}".format(repo_name))
    title = "PR test"
    body = "ignore"
    head = f"{user.login}:update"  # 替换成你的用户名和分支名称
    base = "update"  # 替换成目标分支名称
    pull_request = repo.create_pull(title=title, body=body, head=head, base=base)


pull_request("configs_instrument_info")
