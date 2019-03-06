# update
echo "更新系统 适用于centos系统"
yum update -y
######################################

# zsh
read -p "是否需要安装一套开发环境,zsh之类的? 若需要记得ctrl+D跳出来zsh界面  y or n?  " zsh
if [ $zsh = "y" ] ; then
    yum install vim zsh git autojump autojump-zsh -y
    sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
    echo "zsh开发环境完成................"
fi
#########################################



# python3
read -p "是否需要安装python3.6环境? y or n?   " python
if [ $python = "y" ] ; then
    wget https://www.moerats.com/usr/shell/Python3/CentOS_Python3.6.sh && sh CentOS_Python3.6.sh
    echo "python3 安装完成................"
fi
##########################################

# lamp
read -p "是否需要安装Lamp环境即Linux、apache、mysql、php等常见插件?如果需要进去也需要ctrl+D退出  y or n?  " lamp
if [ $lamp = "y" ] ; then
    yum -y install wget screen git 
    git clone https://github.com/teddysun/lamp.git
    cd lamp
    chmod 755 *.sh
    screen -S lamp
    ./lamp.sh
    cd ..
    echo "lamp安装完成，返回上一级目录......."
fi
#################################################

# ssr
read -p "是否需要安装ssr？y or n?   " ssr
if [ $ssr = "y" ] ; then
    wget --no-check-certificate -O shadowsocks-all.sh https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks-all.sh
    chmod +x shadowsocks-all.sh
    ./shadowsocks-all.sh 2>&1 | tee shadowsocks-all.log
    echo "安装ssr完成，记得添加链接..........."
fi
###################################################

# backend 需要账号与密码
read -p "是否需要Django后台服务器?这里是直接运行，而数据库密码为admin，名称为iot，若是希望自己来的，则将启动的两行注释掉即可 y or n?       " django
if [ $django = "y" ] ;then
    git clone https://github.com/tyrantqiao/dataPlatform.git
    cd dataPlatform
    source backend/bin/activate
    pip3 install -r requirements.txt
    cd iot
    read -p "后台开启的端口是: " port
    python3 manage.py runserver 0.0.0.0:$port &
    cd ...
    echo "后台启动成功................"
fi
####################################################

# npm node
read -p "是否需要npm，nodejs? y or n     " npm
if [ $npm = "y" ]; then
    yum install nodejs -y
    echo "nodejs安装完成..............................."
fi
###################################################

# frontend
read -p "是否需要ant-design模版的前端架构？ y or n    " front
if [ $front = "y" ]; then
    git clone https://github.com/tyrantqiao/ant_frontend.git
    cd ant_frontend
    npm install
    npm start &
    echo "前端启动成功............."
    cd ..
fi
#######################################################
