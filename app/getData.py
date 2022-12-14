from github import Github
import pandas as pd


def getStars(name):
    # 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
    g = Github("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")

    # 获取仓库
    # repo = g.get_repo("LBruyne/ZJU-SE-CourseMaterial")
    repo = g.get_repo(name)
    # 获取仓库的stargazers
    stargazers = repo.get_stargazers_with_dates()
    # 根据stargazers的时间进行排序
    stargazers = sorted(stargazers, key=lambda x: x.starred_at)

    # 获取每个stargazers的时间
    stargazers = [x.starred_at for x in stargazers]
    time = [x.strftime("%Y-%m-%d") for x in stargazers]
    # 写到csv文件中
    df = pd.DataFrame(time, columns=["time"])
    df.to_csv("time.csv", index=False)
    # 获取每个stargazers的时间的数量
    stargazers = [stargazers.count(x) for x in stargazers]

    # 获取每个stargazers的时间的数量的累加
    stargazers = [sum(stargazers[:i + 1]) for i in range(len(stargazers))]
    # 写到csv文件中
    df = pd.DataFrame(stargazers, columns=["stargazers"])
    df.to_csv("stargazers.csv", index=False)


def getCommit(name):
    # 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
    g = Github("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")
    # 设置headers

    # 获取仓库
    # repo = g.get_repo("LBruyne/ZJU-SE-CourseMaterial")

    repo = g.get_repo(name)
    # 获取仓库的commits
    commits = repo.get_commits()
    # 根据commits的时间进行排序
    commits = sorted(commits, key=lambda x: x.commit.author.date)
    # 获取每个commit的时间
    commits = [x.commit.author.date for x in commits]
    time = [x.strftime("%Y-%m-%d") for x in commits]
    # 写到csv文件中
    df = pd.DataFrame(time, columns=["time"])
    df.to_csv("commits_time.csv", index=False)
    # 获取每个commit的时间的数量
    commits = [commits.count(x) for x in commits]
    # 获取每个commit的时间的数量的累加
    commits = [sum(commits[:i + 1]) for i in range(len(commits))]
    # 写到csv文件中
    df = pd.DataFrame(commits, columns=["commits"])
    df.to_csv("commits.csv", index=False)
# 获取issue


def getIssue(name):
    # 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
    g = Github("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")
    # 获取仓库
    # repo = g.get_repo("LBruyne/ZJU-SE-CourseMaterial")
    repo = g.get_repo(name)
    # 获取仓库的issues
    issues = repo.get_issues()
    # 根据issues的时间进行排序
    issues = sorted(issues, key=lambda x: x.created_at)
    # 获取每个issue的时间
    issues = [x.created_at for x in issues]
    time = [x.strftime("%Y-%m-%d") for x in issues]
    # 写到csv文件中
    df = pd.DataFrame(time, columns=["time"])
    df.to_csv("issues_time.csv", index=False)
    # 获取每个issue的时间的数量
    issues = [issues.count(x) for x in issues]
    # 获取每个issue的时间的数量的累加
    issues = [sum(issues[:i + 1]) for i in range(len(issues))]
    # 写到csv文件中
    df = pd.DataFrame(issues, columns=["issues"])
    df.to_csv("issues.csv", index=False)


def getCommitsInsdel(name):
    # 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
    g = Github("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")
    # 获取仓库
    repo = g.get_repo(name)
    # 获取仓库的commits
    commits = repo.get_commits()
    # 获取ins和del
    ins = []
    dels = []
    for commit in commits:
        files = commit.files
        for file in files:
            ins.append(file.additions)
            dels.append(file.deletions)

    print(ins)
    print(dels)


def getCommitsInsdel(name):
    # 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
    g = Github("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")
    # 获取仓库
    repo = g.get_repo(name)
    # 获取仓库的commits
    commits = repo.get_commits()
    # 获取每个时间的ins和del
    ins = []
    dels = []

    for commit in commits:
        ins.append(commit.stats.additions)
        dels.append(commit.stats.deletions)
    # 写到csv文件中
    # 获取每个commit的时间
    commits = [x.commit.author.date for x in commits]
    print(ins)
    print(dels)
    time = [x.strftime("%Y-%m-%d") for x in commits]

    df = pd.DataFrame(time, columns=["time"])
    df.to_csv("commits_insdel_time.csv", index=False)
    df = pd.DataFrame(ins, columns=["ins"])
    df.to_csv("commits_ins.csv", index=False)
    df = pd.DataFrame(dels, columns=["dels"])
    df.to_csv("commits_dels.csv", index=False)


if __name__ == "__main__":
    getStars("pytorch/pytorch")
