# curl_parser

#### 介绍
curl命令转python代码，支持json格式数据转换


#### 安装教程

1.  pip install curl_parser
2.  或者下载源码，解压后运行run.py文件


#### 使用说明

1.  终端命令行输入：
    python run.py 'curl -X POST https://api.example.com/submit' --output python     # 输出python代码
    python run.py 'curl -X POST https://api.example.com/submit' --output json       # 输出json格式数据
2.  调用函数：
    curl_commd = """ curl -X POST https://api.example.com/submit """
    print(to_python_code(parsed))     # 输出python代码
    print(to_json(parsed))            # 输出json格式数据
    print(parse_curl(curl_commd))     # 解析curl命令并返回字典数据



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
