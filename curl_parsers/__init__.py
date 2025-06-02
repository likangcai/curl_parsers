# -*- coding: utf-8 -*-
# ----------------------------
# @Author:    影子
# @Software:  PyCharm
# @时间:       2025/5/30 上午10:22
# @项目:       curl_parsers
# @FileName:  __init__.py
# ----------------------------
from .parser_curl import _parse_curl
from .generator import _to_python_code, _to_json_code


def parse_curl(command: str) -> dict:
    """将 curl 命令解析为 Python 对象
    Args:
        command (str): 待解析的 curl 命令字符串
    Returns:
        dict: 解析后的请求对象字典
    Raises:
        ValueError: 如果命令为空或仅包含空白字符
    """
    command = command.strip()
    if not command:
        raise ValueError("curl 命令不能为空")
    return _parse_curl(command)


def to_python(command: str) -> str:
    """将 curl 命令解析结果转为 Python 代码
    Args:
        command (str): 待解析的 curl 命令字符串
    Returns:
        str: 生成的 Python 代码字符串
    """
    data = parse_curl(command)
    return _to_python_code(data)


def to_json(command: str) -> str:
    """将 curl 命令解析结果转为 JSON 字符串
    Args:
        command (str): 待解析的 curl 命令字符串
    Returns:
        str: 生成的 JSON 字符串
    """
    data = parse_curl(command)
    return _to_json_code(data)
