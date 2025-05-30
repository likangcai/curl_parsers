# -*- coding: utf-8 -*-
# ----------------------------
# @Author:    影子
# @Software:  PyCharm
# @时间:       2025/5/30 上午9:56
# @项目:       curl_parsers
# @FileName:  setup.py
# ----------------------------
"""项目打包配置文件"""
from setuptools import setup, find_packages

setup(
    name="curl_parsers",          # 包名（pip install curl_parsers）
    version="0.1.3",              # 版本号
    author="影子",                # 作者名
    author_email="yxdszlkc@163.com",  # 作者邮箱
    description="Convert curl commands to Python requests code or JSON.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://gitee.com/yxdsz/curl_parsers",  # 项目主页
    packages=find_packages(),     # 自动发现包
    install_requires=[],          # 依赖（如果有）
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={                # 可选：定义命令行入口（如果需要直接运行）
        "console_scripts": [
            "uncurl=curl_parsers.cli:cli_run",
        ],
    },
)
