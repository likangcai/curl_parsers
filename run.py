# -*- coding: utf-8 -*-
# ----------------------------
# @Author:    影子
# @Software:  PyCharm
# @时间:       2025/5/28 下午12:26
# @项目:       curl_parsers
# @FileName:  run.py
# ----------------------------
import argparse

from generator import _to_python_code
from generator import _to_json_code
from parser_curl import _parse_curl


def cli_run():
    """
    命令行解析
    eg：python run.py 'curl -X POST https://api.example.com/submit' --output python
        python run.py 'curl -X POST https://api.example.com/submit' --output json
    """
    parser = argparse.ArgumentParser(description='Convert curl command to Python requests code or JSON.')
    parser.add_argument('curl_command', type=str, help='The curl command string to be converted.')
    parser.add_argument('--output', choices=['python', 'json'], default='python',
                        help='Output format (default: python)')

    args = parser.parse_args()

    curl_cmd = args.curl_command.strip()
    try:
        parsed = _parse_curl(curl_cmd)
    except ValueError as e:
        print(f"解析 curl 命令失败: {e}")
        return

    if args.output == 'python':
        print(_to_python_code(parsed))
    elif args.output == 'json':
        print(_to_json_code(parsed))


def curl_parser(command: str) -> dict:
    """
    将curl命令解析为python对象
    :param command: curl命令
    :return: 解析结果
    """
    if not command.strip():
        raise ValueError("Invalid curl command")
    try:
        return _parse_curl(command.strip())
    except Exception as e:
        raise ValueError(f"Failed to parse curl command: {e}") from e


def to_python(command: str) -> str:
    """
    将curl命令解析结果转为python代码
    :return: python代码
    """
    data = curl_parser(command)
    return _to_python_code(data)


def to_json(command: str) -> str:
    """
    将curl命令解析结果转为JSON字符串
    :return: JSON字符串
    """
    data = curl_parser(command)
    return _to_json_code(data)


if __name__ == "__main__":
    cli_run()

    # # 示例测试
    # curl_command = """
    #  curl -X POST https://api.example.com/submit
    # """
    #
    # parsed = curl_parser(curl_command)
    # print(to_python(curl_command))
    # print(to_json(curl_command))
    # print(parsed)
