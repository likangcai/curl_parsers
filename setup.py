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
    name="curl-parsers",
    version="0.1.3",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "curl-parse = curl_parsers.run:cli_run"
        ]
    },
    install_requires=[
    ],
)
