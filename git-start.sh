# 启动ssh的密钥的一键脚本
read -p "是否需要生成deploy key，方便直接pull，push以.git的形式? y or n?    " git
if [ $git = "y" ] ; then
    echo "生成形式直接默认即可，生成路径需要自己记录，最好放在当前目录下"
    read -p "请输入你的github邮箱：" email
    ssh-keygen -t rsa -C "$email"
    eval $(ssh-agent -s)
    read -p "请输入你的id_rsa文件存放位置" location
    ssh-add $id_rsa
    cat $id_rsa.pub
    read -p "请将pub文件放到github的deploy keys中，放置成功后，再输入y   " success
    if [ $success = "y" ] ; then
        ssh -T git@github.com
        echo "密钥已生效..................."
    fi
fi
read -p "是否需要让密钥重新生效? y or n?      " replay
if [ $replay = "y" ] ; then
   read -p "请输入密钥地址，回车为当前地址" reLocation
   if [ -z "${reLocation}" ]; then
       reLocation="$(pwd)/id_rsa"
       echo "你的密钥地址在$reLocation"
   fi
   eval $(ssh-agent -s)
   ssh-add $reLocation
   ssh -T git@github.com
   echo "密钥已生效............................."
fi

