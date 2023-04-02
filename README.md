# Wuhan_Pepsi
武汉百事可乐分享仓库
___
本系列教程旨在从大的方面讲解如何运用Python制作一个网站,具体Python细节不做过多深究，特别是Python基础。
## Chapter 0 工欲善其事，必先利其器
这一章主要讲解开发环境的布置，极大的利用Windows拥抱开源Linux系统的优势进行，所以如果打算使用Windows下的PyCharm开发请绕过。

>开发环境： Windows10 19044+ 或Windows 11 + WSL2 + PyCharm Community + fcitx 

开启wsl2g，操作如下：
1. 任务栏搜索控制面板，进入点击卸载程序，点击启用或关闭Windows功能，点击开启适用于Linux的Windows子系统与虚拟机平台后确定重启进入桌面。
2. 任务栏搜索store，进入Windows Store，搜索linux，安装Ubuntu及Windows Terminal
3. 任务栏搜索wt,进入后，输入wsl --update 对wsl进行升级以便支持Linux GUI功能。
4. 启动ubuntu，可以输入ubuntu或下拉列表选择Ubuntu,初始化后输入用户名及密码，支持图形化的Linux子系统部署完毕。

Linux(debian系)基本操作：
- sudo 增加管理员权限，如执行命令仍无效，请sudo su 直接以root身份执行命令。su(switch user简写) 你的用户名切换回来。
- sudo sed -i 's@//.*archive.ubuntu.com@//mirrors.ustc.edu.cn@g' /etc/apt/sources.list 及 sudo sed -i 's/http:/https:/g' /etc/apt/sources.list更换国内源以便下载更新软件。
详情请参考[中国科技大学](https://mirrors.ustc.edu.cn/help/ubuntu.html)
- sudo apt update 与软件仓库进行同步以获取所有软件的最新情况
- sudo apt upgrade 更新所有软件
- sudo apt search 软件名 对名称进行查找搜索，包括查看软件简介以便进一步确定该软件。

Linux通用操作
- touch a 新建文件a
- mkdir project 新建文件夹project
- cd 文件夹名称 进入该目录， cd .. 进入当前目录上一级，cd ../.. 进入当前目录上一级的上一级,cd ~ 进入当前用户的家目录
- cat b 显示文件b内容于终端。
- move 移动文件或文件夹或改名。（取决于路径，同一路径下即重命名）

至此，可以sudo apt install gedit测试下Linux某种类Windows记事本程序运行正常与否。
>开启WSL systemctl

某种系统级命令，可对服务开启重启停止等等，只需新建/etc/wsl.conf文件bi并写入以下内容保存重启wsl即可。

    [boot]
    systemd=true
详情请阅读[微软官方博客](https://devblogs.microsoft.com/commandline/systemd-support-is-now-available-in-wsl/)

wsl --shutdown Windows终端执行后，直接终止Linux子系统进程，再运行对应版本的Linux即可重新开启。

>安装PyCharm Community

在systemctl restart snapd.service后执行下述代码进行安装，这里我们只需要社区免费版即可。

sudo snap install pycharm-community --classic

支持中文：sudo apt install fonts-wqy-microhei

>安装中文输入法

具体请点击参考[这篇文章](https://patrickwu.space/2019/10/28/wsl-fcitx-setup-cn/)进行安装。


## Chapter 1 初来乍到
这一章主要说明如何构建一个网站基本的框架，将采用三个函数分别概括说明，包含基本概念。麻雀虽小，五脏俱全。
我们采用poetry为我们创建网站虚拟的开发环境，以区别于本机主环境，以免照成不可预测的情况。步骤如下：
- 新建项目文件夹，本文为tutorial
- 进入该文件夹后，输入poetry init，分别以interactive shell(问询)的形式问你包名（网站名）、版本号、描述、作者、许可证、Python版本号、主要依赖、开发依赖等项目情况。完后会生成配置文件pyproject.toml.
- 输入poetry install, poetry 会根据之前我们已经配置好的pyproject.toml为我们生成所需的一切。
- 输入poetry shell, 激活当前网站的虚拟环境。

新建文件app.py，这里可以用PyCharm或命令行去创建，以后不再加以说明。

    from apiflask import APIFlask

    app=APIFlask(__name__)

    @app.route('/')
    def index():
    return "Hello, World"

键入以上5行后，在当前网站名称文件夹下输入flask run,就会启动一个运行于本机的网站。打开浏览器访问http://127.0.0.1:5000/后，显示Hello, World。我们已经完成了一个网站的Hello,World程序。
index()函数为视图函数，其上跟着一个装饰器，引号内为访问路径。函数主体非常检查，即返回一个字符串。
假设我们需要构建一个新的篇章，做用户输入输出操作的，目前这个文件，如果各种功能堆叠在一起，夹杂着不同的访问路径和视图函数的逻辑，既不好看也不好维护，这怎么办呢？就有这样一个概念，叫蓝图，可以很好的解决目前这种问题。我们需要构建Python软件包，包区别于一般的文件夹的地方只在于多一个__init__.py文件，文件空与不空都不影响，具体看需求。
在__init__.py文件下我们导入蓝图

    from apiflask import APIBlueprint

    user=APIBlueprint('user',__name__,url_index='/user')

    from . import view

这里实例化一个蓝图对象，跟着三个初始化参数。第一个，蓝图的名称；第二个，蓝图的包名，用__name__；第三个为浏览器地址栏的路由名称，即二级访问地址。

最后我们完成这个已在包名中导入的视图文件（view.py）

    from . import user


    @user.get("/")
    def index():
        return "这是从user蓝图加载的视图函数"

好像也是显示一句话，，没有什么新意。这里我们改成一个文本框和一个提交按钮的表单形式。

    @user.get("/")
    def index():
        return "<form method='post'><input type='text' name='username'/><input type='submit'/></form>"

我们已经看出，这里的视图函数上方的路由装饰器修饰的为get()方法，区别于刚才我们最开始index()的route方法。get()方法只接受客户端发起的get请求。
给用户提供了输入文本框和提交按钮，剩下的就差显示用户输入的内容了。让我们再写入一个视图函数。

    @user.post('/')
    @user.input(Hello,location="form")
    def user(data):
        return f"<h1>你输入了{data['username']}</h1>"

注意这里，我们对用户的输入做出了要求，他需要遵循Hello类的定义来进行检查。这是后端的验证强制检查。内容如下，为新增内容。

    from apiflask.schemas import Schema
    from apiflask.fields import String
    from apiflask.validators import Length

    class Hello(Schema):
    username=String(required=True,validate=Length(1,8))

我们不仅要求对类型，还有是否必须及长度做出约束。这个时候我们试下，不输入内容进行访问，服务器会响应422客户端报错。
有个关键点需要注意，一个是在路由装饰器下方再写一个装饰器进行引用，上下两层装饰器顺序不能颠倒。另一个则是我们后台代码在检查客户端发送速度的时候，如何进行来源的判断，是header还是form亦或是其他？由location,这边第二个位置参数进行判断，默认来源是json。

总结:
本章我们学习了如何用5行代码就启一个http网络服务，并且掌握了在视图函数上方如何按需求对get或post请求分别进行处理并显示内容。最后我们知晓了如何对用户输入的内容加以控制约束。
