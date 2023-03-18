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