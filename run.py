# -*- coding: utf-8 -*-
# ----------------------------
# @Author:    影子
# @Software:  PyCharm
# @时间:       2025/5/28 下午12:26
# @项目:       curl_parser
# @FileName:  run.py
# ----------------------------
import argparse

from generator import to_python_code
from generator import to_json_code
from parser_curl import parse_curl


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

    curl_cmd = args.curl_command
    try:
        parsed = parse_curl(curl_cmd)
    except Exception as e:
        print(f"解析 curl 命令失败: {e}")
        return

    if args.output == 'python':
        print(to_python_code(parsed))
    elif args.output == 'json':
        print(to_json_code(parsed))


class Uncurl:
    """
    解码curl命令
    """

    def __init__(self, command: str):
        if not isinstance(command, str) or not command.strip():
            raise ValueError("curl命令不能为空")
        try:
            self._data = parse_curl(command)
        except Exception as e:
            raise ValueError(f"无效的 curl 命令: {e}")

    @property
    def data(self) -> dict:
        """
        获取解析后的 curl 数据
        :return: 解析结果字典
        """
        return self._data

    def to_python(self) -> str:
        """
        将curl命令解析结果转为python代码
        :return: python代码
        """
        return to_python_code(self._data)

    def to_json(self) -> str:
        """
        将curl命令解析结果转为JSON字符串
        :return: JSON字符串
        """
        return to_json_code(self._data)


if __name__ == "__main__":
    # cli_run()

    curl_command = """
     curl -X POST https://api.example.com/submit
    """

    parsed = Uncurl(curl_command)
    print(parsed.to_python())
    print(parsed.to_json())
    print(parsed.data)
