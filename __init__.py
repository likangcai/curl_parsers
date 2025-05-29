# !/usr/bin/env/python3
# -*- coding: utf-8 -*-
# ------------------------------
# @Author  : 影子
# @Time    : 2025/5/29 21:22
# @File    : __init__.py
# @Software: PyCharm
# @Description: 
# ------------------------------
"""将curl命令解析成python代码或json数据"""
from .generator import *
from .parser_curl import parse_curl


def python_object(command: str) -> dict:
    """ curl命令转python对象 """
    return parse_curl(command)


def to_json(data: dict) -> str:
    """ curl命令转json对象 """
    return to_json_code(data)


def to_python(data: dict) -> str:
    """ curl命令转python代码 """
    return to_python_code(data)
