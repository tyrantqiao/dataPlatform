# dataPlatform 数据平台
以Django为后台负责数据库处理部分

## 前端使用阿里的ant-design
https://github.com/tyrantqiao/dataPlatform

- 实现前后端分离
- 实现数据节点管理
- 实现数据展示以及采集
- 权限模块
- 一键安装脚本设计

## 调试界面

Django后端接口调试界面http://ip:port/docs/

## 安装界面【详细的可以下载安装说明docs进行查询】

安装说明（这里用的是脚本安装模式，对应的是centos系统，如果是ubuntu系统则不能这样子操作，就得自行安装其中必须安装的配件）

Centos系统的脚本安装方式：

1. 登录服务器（输入服务器的账号和密码）
2. 选择文件夹作为工作目录（比如这里选择了/home/qiao）


3. 下载install.sh脚本作为下载的脚本，执行
wget https://raw.githubusercontent.com/tyrantqiao/dataPlatform/master/install.sh

4. 赋予脚本权限并执行脚本
Chmod +x install.sh
./install.sh


5. 根据提示下载所需要的东西，这里需要的有以下内容，其他东西请自行选择
  5.1 系统更新选择y更新系统（若是嫌慢可以不更新系统，但是最好更新一下系统，为了稳定性起见）
  5.2 Docker安装选择y进行安装
  5.3 Ssh安装
    需要就装，不需要就选择n
  5.4vim安装

  同理需要就装
  5.5python3环境

  需要装的！
  【如果是ubuntu系统，可能需要执行sudo apt-get install build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev libssl-dev
  补充一些必备的依赖】
  5.6Mysql

  不用docker-compose起的服务需要注意安装，用docker-compose就不需要了
  5.7Ssr

  同理需要就装
  5.8django后台
   需要装
  5.9前端和nodejs
  都需要安装
6. 启动项目
docker-compose up -d

等待安装完成即可开始尝试，安装需要一段时间。

不用安装脚本安装方法：
  1. 这里安装的前提是将之前的所需要的依赖全部安装完成需要的有python3、pip3、docker、docker-compose、nodejs
  2. 克隆前端和后端框架
  选择一个文件夹,cd /home   mkdir test   cd  test
  3. Git clone https://github.com/tyrantqiao/ant_frontend.git
  4. Git clone https://github.com/tyrantqiao/dataPlatform.git
  5. 把启动脚本拉出来 sudo mv dataPlatform/docker-compose.yml ./
  6. Sudo docker-compose up -d

需要注意的
  1. dataPlatform/iot/iot/settings.py这里可以修改连接数据库的host，如果是docker-compose服务的mysql，名字就为mysql（默认就是mysql）若不是，则更改为自己的mysql服务ip
  2. Ant-frontend/config/config.js这里可以修改后台服务的ip以及端口，默认是193.112.44.251:9002（这是docker服务设置的端口号），如果不是请自行修改为正确的
