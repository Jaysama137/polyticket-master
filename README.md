# Polyticket-master

**声明：本项目为课程作业，仅作教学科研之用，不干涉现实世界中的实际购票！如有复制或篡改本项目者用于现实世界中抢票，本人强烈道德谴责，并概不负责！**


## 引用的代码

本项目使用了来自[AndrewMore](https://gitee.com/andrewmore)在Gitee的项目[AutoTicketForPoly](https://gitee.com/andrewmore/auto-ticket-for-poly)的代码。在此感谢AndrewMore的工作和贡献。

## 安装与使用说明

请参见[AndrewMore](https://gitee.com/andrewmore)在Gitee的项目[AutoTicketForPoly](https://gitee.com/andrewmore/auto-ticket-for-poly)中的说明。

如果链接失效，可查看本项目中的备份文档：backup/AutoTicketForPoly_README_backup.md

## 本项目的改动

由于售票网站的网页元素变动，本项目的工作流程与[AutoTicketForPoly](https://gitee.com/andrewmore/auto-ticket-for-poly)略有不同：

* 进入购票界面，检测是否开售，选择时段，开始选座
* 进入选座界面，并自动全屏，由使用者**手动**选择座位（目前仅支持选择**一个**座位）。检测到座位选择后，会点击提交按钮
* 进入支付页面，会填写使用者预留的个人信息（姓名和手机号），自动选择第一个支付方式，自动同意购票协议，并点击支付按钮

以上便是本项目工作流程

**再次声明：本项目为课程作业，仅作教学科研之用，不干涉现实世界中的实际购票！如有复制或篡改本项目者用于现实世界中抢票，本人强烈道德谴责，并概不负责！**
