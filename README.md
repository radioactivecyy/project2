## Readme——xxyyz

### 项目用途

旨在帮助开发者和代码分析者对Pytorch项⽬进⾏项⽬分析、⽐较，以更好地从更多维度了解Pytorch项目的各个方面。

### 后端安装及运行

#### 安装（以windows 11 x64 为例）：

- 安装`Python`

  - 进入https://www.python.org/downloads/ 选择`Python 3.10.4`，并选择`Windows installer(64-bit)`，下载压缩包。

  ![download_python](./assets/download_python.png)

  - 解压缩并保持默认选项一直选择下一步直至安装完成。
  - 验证安装——终端输入`python --version`，显示`Python`版本。

  ![python_version](./assets/python_version.png)

- 安装`Django`

  - 终端输入`python -m pip install django==3.2`。
  - 验证安装——终端输入`python`,再输入`import django`,最后输入`django.get_version()`，显示`Django`版本。

  ![django_version](./assets/django_version.png)

- 配置`Mysql`

  - 安装`Mysql`（在此不作赘述）。
  - 在`Mysql`中用`create database xxyyz`创建数据库（`xxyyz`任意填写）。
  - 修改项目中的`./djangoproject/setting.py`，填入自己的数据库名和密码。

  ![Mysql_config](./assets/Mysql_config.png)

- 运行后端

  - 数据库建立与同步

    - 在项目根目录运行终端，输入`python manage.py runserver`。

    ![makemig](./assets/makemig.png)

    - 继续输入`python manage.py migrate`

    ![mig](./assets/mig.png)

  - 在项目根目录运行终端，输入`python manage.py runserver`,出现如下图所示内容，即成功运行。

![run](./assets/run.png)