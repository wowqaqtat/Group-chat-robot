# 群发机器人🤖

群发机器人是一款基于 Python 编写的应用程序，旨在为企业微信的管理人员、社群运营者和微商提供一个快捷、高效的群发工具。该机器人可以在企业微信群中进行群发文本、图片，并支持 Markdown 格式，让你的信息更加丰富、生动。（在终端某个群组添加机器人之后，创建者可以在机器人详情页看的该机器人特有的webhook地址。开发者可以向地址发起HTTP POST 请求，即可实现给该群组发送消息。）

## 功能特色

- 支持文本和图片的群发，让你的信息快速传达。
- 支持 Markdown 格式，让你的信息更加丰富、生动。
- 采用企业微信接口，安全可靠，保证你的信息安全。
- 简单易用，只需几步就可轻松实现群发功能。

## 截图

<img src="https://raw.githubusercontent.com/wowqaqtat/Group-chat-robot/main/doc/11.png" height="200px"> <img src="https://raw.githubusercontent.com/wowqaqtat/Group-chat-robot/main/doc/12.png" height="200px"> <img src="https://raw.githubusercontent.com/wowqaqtat/Group-chat-robot/main/doc/13.png" height="200px">

## 快速开始

0. 前置条件：在企业微信中创建内部群，并保存群机器人的webhook地址。
1. 克隆或下载本项目至本地，并安装  Python 相关依赖。
2. 登录企业微信，创建一个内部群，保存webhook地址备用。
3. 将程序中“企业微信机器人webhook地址”改成你自己的。
4. 运行 `群发机器人.py`，即可进行群发操作。
5. 可以通过 `pyinstaller -F 群发机器人.py` 将程序打包，导出为exe文件。

## 使用须知

1. 群发机器人仅用于合法、合理的通讯和活动，请勿滥用。
2. 本程序无法在普通微信群中使用！！本程序只能在企业微信群使用，提高内部管理效率。
3. 一定要保护好机器人的webhook地址，避免泄漏！否则坏人就可以用你的机器人来发垃圾消息了。

## 联系我们

- 本程序基于 [MIT](https://opensource.org/licenses/MIT) 许可证开源。
- 本程序不定时更新，如果大家在使用的过程中，发现任何bug或有不错的想法，欢迎提出交流。
- 源代码：[https://github.com/wowqaqtat/Group-chat-robot](https://github.com/wowqaqtat/Group-chat-robot)
- 视频讲解：bilibili
- 邮箱：[help@haodukeji.cn](mailto:help@haodukeji.cn)
