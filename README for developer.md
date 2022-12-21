# 2022---xxyyz
本项目为2022浙江大学软件需求工程的大作业，队伍为xxyyz队

cyy-10.26-commit:

- 大致把stargazer和issue的company信息存下来了，放在data文件夹的.csv文件中（没错就是java要输出的那个文件格式），使用的时候在mysql中导入文件即可

- issue全部获取了1w多条

- 新建了4个数据库表，字段意思就是字面意思

- 目前传给前端的是直接从数据库里取出的人数较多的company的相关信息（全部信息经过预先sql处理筛出人数较多的company后存入另一个statistic数据库），以字典的形式，前端应该是可以遍历字典并取出的（？）

  | key                     | value                                 |
  | ----------------------- | ------------------------------------- |
  | company的名称 eg.Google | 该公司参与的人数                      |
  | total                   | 所有参与的且github中写明company的人数 |
  | update_time             | 这些数据的更新时间                    |

cyy-10.27-commit:

- 把committer的信息搞下来了，放在data文件夹对应数据库表名的.csv文件中
- committer的公司信息全部搞了，总共5w多条，有公司信息的有2w多条
- 对committer信息按照之前的字段也建了两个表
- 多建了一个total表，更新数据的时候用（虽然但是更新的函数还没写）

cyy-10.29-commit:

- 写了更新的函数，调用该函数将更新上次更新到现在这一时间段内新增的所有commany信息
- stargazer数据的获取依旧是老问题，所以代码里注释掉了，能用的就是更新issue和committer的公司信息，测试过了
- 更新函数仅是对数据库表的更新，如果要获取对应来源的公司信息，还是要再调用对应的函数

cyy-11.3-commit:

- 如pytorch一般新建了7个数据库表，并写了pandas的三种company来源的获取、更新函数，形式和pytorch差不多
- 把从pandas获取到的所有数据放在了data文件夹中，带有pandas_前缀

cyy-12.21-commit:

- 词云图更新了两个函数，pytorch_graph_issues_word_cloud和pandas_graph_issues_word_cloud，信息从数据库中提取，所以需要导入pytorch_issues和pandas_issues两张表。

- 分布更新了两个函数，pytorch_issue_update_time和pandas_issue_update_time，信息直接从csv中提取，可以直接使用。

- urls配置为

- ```python
  path('pytorch_issue_wordcloud', views.pytorch_graph_issues_word_cloud),
  path('pandas_issue_wordcloud',views.pandas_graph_issues_word_cloud),
  path('pytorch_update_time', views.pytorch_issue_update_time),
  path('pandas_update_time', views.pandas_issue_update_time),
  ```