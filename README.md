# AutoTicketForPoly

#### 介绍
保利票务自动抢票脚本

#### 软件架构
基于python3
selenium
chromedriver


#### 安装教程

1.  选择git clone 或者直接下载压缩文件到本地
2.  下载python3.7  https://blog.csdn.net/weixin_40844416/article/details/80889165
3.  python3.7安装好之后，打开cmd终端输入pip install selenium，等待安装完毕
![输入图片说明](https://images.gitee.com/uploads/images/2021/0802/095017_ae037ff4_9510992.png "屏幕截图.png")
4.  如果没有chrome，下载chrome。chrome的版本信息在浏览器的“帮助”菜单中能找到
5.  下载chrome **对应版本** 的chromedriver，网址：https://npm.taobao.org/mirrors/chromedriver/
6.  生成一个chrome浏览器的快捷方式到此文件夹
![输入图片说明](https://images.gitee.com/uploads/images/2021/0801/120050_3dc87c05_9510992.png "屏幕截图.png")
7.  右键chrome快捷方式，选择“属性”，设置“目标”  
举例：**"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="E:\Data\02_Code\07_Ticket_Order\Automatic_ticket_purchase-master\AutomationProfile"** 
这个地方填写的是debug模式启动chrome命令，这样才能让webdriver通过port口获取浏览器页面，需要在本文件夹下面创建一个AutomationProfile，来存放临时文件

命令的格式是  chrome原文件的路径  --remote-debugging-port=9222 --user-data-dir="临时文件存放路径"

然后设置起始位置为本文件夹

举例：E:\Data\02_Code\07_Ticket_Order\Automatic_ticket_purchase-master  这里设置了chrome的root路径
![输入图片说明](https://images.gitee.com/uploads/images/2021/0801/120309_0ec25c66_9510992.png "屏幕截图.png")

这两步是为了让webdriver可以获取到当前的浏览器页面，这个页面是登陆之后的页面，所以不存在登陆的验证问题


#### 使用说明

1.  进入文件夹，打开chrome快捷方式
2.  用txt文本软件打开ticket_order.py编辑以下两行
![输入图片说明](https://images.gitee.com/uploads/images/2021/0802/095822_8bb45f2e_9510992.png "屏幕截图.png")
    关闭ticket_order.py
3.  打开cmd终端，使用命令 python ticket_order.py，开始运行
![输入图片说明](https://images.gitee.com/uploads/images/2021/0802/095943_222b7343_9510992.png "屏幕截图.png")
 **注意保持浏览器页面在屏幕前面** （眼睛能看到的地方，这个软件有些鼠标自动点击的地方需要浏览器在最前面）
![输入图片说明](https://images.gitee.com/uploads/images/2021/0802/100116_e03c24a1_9510992.png "屏幕截图.png")

4.  等待打印出来 “抢票成功，请尽快支付” 时表示抢票成功

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
