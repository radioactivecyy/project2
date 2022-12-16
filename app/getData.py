from github import Github
import pandas as pd


def getStars(token, name):

    g = Github(token)

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

    # 获取每个stargazers的时间的数量
    stargazers = [stargazers.count(x) for x in stargazers]
    # 写到csv文件中
    df["stargazers"] = stargazers
    # 合并相同的时间
    df = df.groupby("time").sum()
    df = df.reset_index()
    stargazers = df["stargazers"].tolist()
    # 获取每个stargazers的时间的数量的累加
    stargazers = [sum(stargazers[:i + 1]) for i in range(len(stargazers))]
    # 写到csv文件中
    df["stargazers"] = stargazers
    df.to_csv("stargazers_pandas.csv", index=False)


def getCommit(token, name):
    # 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
    g = Github(token)
    # # 设置headers
    # # 获取仓库
    # repo = g.get_repo("LBruyne/ZJU-SE-CourseMaterial")
    repo = g.get_repo(name)
    # # 获取仓库的commits
    commits = repo.get_commits()
    # # 根据commits的时间进行排序
    commits = sorted(commits, key=lambda x: x.commit.author.date)
    # # 获取每个commit的时间
    commits = [x.commit.author.date for x in commits]
    time = [x.strftime("%Y-%m-%d") for x in commits]
    # # 获取每个commit的时间的数量
    commits = [commits.count(x) for x in commits]
    df = pd.DataFrame(time, columns=["time"])
    df["commits"] = commits
    df = df.groupby("time").sum()
    df = df.reset_index()
    commits = df["commits"].tolist()
    commits = [sum(commits[:i + 1]) for i in range(len(commits))]
    df["commits"] = commits
    df.to_csv("commits_pandas.csv", index=False)


# 获取issue


def getIssue(token, name):
    # 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
    g = Github(token)
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

    # 获取每个issue的时间的数量
    issues = [issues.count(x) for x in issues]
    df['issues'] = issues
    df = df.groupby("time").sum()
    df = df.reset_index()
    issues = df["issues"].tolist()
    # 获取每个issue的时间的数量的累加
    issues = [sum(issues[:i + 1]) for i in range(len(issues))]
    df["issues"] = issues
    # 写到csv文件中
    df.to_csv("issues_pytorch.csv", index=False)


def getCommitPerDay(token, name, filename):
    # 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
    g = Github(token)
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
    # 获取每个commit的时间的数量
    commits = [commits.count(x) for x in commits]
    df = pd.DataFrame(time, columns=["time"])
    df["commits"] = commits
    df = df.groupby("time").sum()
    df = df.reset_index()
    df["commits"] = commits
    df.to_csv(filename, index=False)


def getCommitsInsdel(token, name, filename, filename1):
    # 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
    g = Github(token)
    # 获取仓库
    repo = g.get_repo(name)
    # 获取仓库的commits
    commits = repo.get_commits()
    commits1 = commits

    # 获取每个时间的ins和del
    ins = []
    dels = []

    for commit in commits:
        ins.append(commit.stats.additions)
        dels.append(commit.stats.deletions)
    # 写到csv文件中
    # 获取每个commit的时间
    commits = [x.commit.author.date for x in commits]
    time = [x.strftime("%Y-%m-%d") for x in commits]

    df = pd.DataFrame(time, columns=["time"])

    df = pd.DataFrame(ins, columns=["ins"])
    df['ins'] = ins
    df['dels'] = dels
    df = df.groupby("time").sum()
    df = df.reset_index()
    # 按月份进行分组
    df["time"] = df["time"].apply(lambda x: x[:7])

    df.to_csv(filename, index=False)

    commits = commits1
    commits = sorted(commits, key=lambda x: x.commit.author.date)
    # 获取每个commit的时间
    commits = [x.commit.author.date for x in commits]
    time = [x.strftime("%Y-%m-%d") for x in commits]
    # 获取每个commit的时间的数量
    commits = [commits.count(x) for x in commits]
    df = pd.DataFrame(time, columns=["time"])
    df["commits"] = commits
    df = df.groupby("time").sum()
    df = df.reset_index()
    df["commits"] = commits
    df.to_csv(filename1, index=False)
# 处理stars


def handel_Stars():
    # 合并commits_time和commits
    commits_time = pd.read_csv("pandas_commits_time.csv")
    commits = pd.read_csv("pandas_commits.csv")
    commits = pd.concat([commits_time, commits], axis=1)
    # 合并同一天的commits
    commits = commits.groupby("time").sum()
    commits = commits.reset_index()
    # 写到csv文件中
    commits.to_csv("pandas_commits_test.csv", index=False)
# 获取stars


def analyse_Issue(name, token, filename):
    # issue 按更新时间在时间轴上的分布
    # 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
    g = Github(token)
    # 获取仓库
    repo = g.get_repo(name)
    # 获取仓库的issues
    issues = repo.get_issues()
    # 获取每个issue的开始时间
    issues_start = [x.created_at for x in issues]
    # 获取每个issue的结束
    issues_end = [x.closed_at for x in issues]
    # 获取每个issue的关键词
    issues_key = [x.title for x in issues]
    # 把时间转换成字符串
    issues_start = [x.strftime("%Y-%m-%d") for x in issues_start]
    issues_end = [x.strftime("%Y-%m-%d") for x in issues_end]
    # 写到csv文件中
    # 生成index
    index = [i for i in range(len(issues_start))]
    df = pd.DataFrame(index, columns=["index"])
    df["start"] = issues_start
    df["end"] = issues_end
    df["key"] = issues_key
    df.to_csv(filename, index=False)


if __name__ == "__main__":
    token = "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"

    getCommitsInsdel(token, "pandas-dev/pandas",
                     "commits_insdel_pandas.csv", "commits_PerDay_pandas.csv")
    # getCommitPerDay(token, "pandas-dev/pandas", )
    getCommitsInsdel(token, "pytorch/pytorch",
                     "commits_insdel_pytorch.csv", "commits_PerDay_pytorch.csv")
    # getCommitPerDay(token, "pytorch/pytorch", )
    # handel_Stars()
    # getCommit(token, "pandas-dev/pandas")
