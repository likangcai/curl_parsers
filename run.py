# -*- coding: utf-8 -*-
# ----------------------------
# @Author:    影子
# @Software:  PyCharm
# @时间:       2025/5/28 下午12:26
# @项目:       curl_parser
# @FileName:  run.py
# ----------------------------
from parser_curl import parse_curl
from generator import to_python_code
from generator import to_json_code
import argparse


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
    parsed = parse_curl(curl_cmd)

    if args.output == 'python':
        print(to_python_code(parsed))
    elif args.output == 'json':
        print(to_json_code(parsed))


def curl_python_object(command: str):
    """ curl命令转python对象 """
    return parse_curl(command)


def to_json(data: dict) -> str:
    """ curl命令转json对象 """
    return to_json_code(data)


def to_python(data: dict) -> str:
    """ curl命令转python代码 """
    return to_python_code(data)


if __name__ == "__main__":
    cli_run()

 #    curl_commd = """
 #
 # curl -X POST https://api.example.com/submit
 #
 #    """
 #
 #    parsed = parse_curl(curl_commd)
 #    # print(parsed)
 #    print(to_python_code(parsed))
 #    # print(to_json(parsed))

