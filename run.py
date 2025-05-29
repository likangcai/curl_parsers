# -*- coding: utf-8 -*-
# ----------------------------
# @Author:    影子
# @Software:  PyCharm
# @时间:       2025/5/28 下午2:26
# @项目:       curl_parser
# @FileName:  run.py
# ----------------------------
from parser_curl import parse_curl
from generator import to_python_code
from generator import to_json_code
import argparse


def cli_run():
    """命令行解析"""
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
    # cli_run()

    curl_commd = """
   
   curl 'https://smp-sit.crb.cn/gw/platform/org-change-record/org-find-page' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: zh-Hans' \
  -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkQ1RkU1NzgwQjFFRURFMTgxQ0UzRDUyMDYwMjU4OUYxNDA1NTlFRTYiLCJ4NXQiOiIxZjVYZ0xIdTNoZ2M0OVVnWUNXSjhVQlZudVkiLCJ0eXAiOiJhdCtqd3QifQ.eyJzdWIiOiIxNjE3YWY0MS0yODk3LTQwY2UtOWI3Zi0xY2QyMTMyZGVhZDMiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJ6aGFuZ2NoaTEiLCJlbWFpbCI6InpoYW5nY2hpMUBleGFtcGxlLmNvbSIsInJvbGUiOlsiWjAxMS01MDAwMDYwOSIsIlowWFQtNTAwMDIwODMiLCJaMFhULTUwMDAyMTg1IiwiWjBYVC01MDIzODQ4NiJdLCJnaXZlbl9uYW1lIjoi5byg5bybIiwicGhvbmVfbnVtYmVyX3ZlcmlmaWVkIjoiRmFsc2UiLCJlbWFpbF92ZXJpZmllZCI6IkZhbHNlIiwidW5pcXVlX25hbWUiOiJ6aGFuZ2NoaTEiLCJVc2VyQlAiOiIwMDEwMDQwMTQ0IiwiQ29kZSI6Ik1Ea3pNVE5oWWpOak1tRTBORFkxWTJJM1pqbGhNekU1TVRJNFlUSXdOR1U9IiwiTG9naW5Tb3VyY2UiOiJwYXNzd29yZG5ldyIsIlVuaXF1ZW5lc3MiOiI5Yzk0ZTg1My04OWYyLTRmZDktOGY1My02MWY1MDFiYzhiOTAiLCJvaV9wcnN0IjoiYmFzaWMtd2ViIiwiY2xpZW50X2lkIjoiYmFzaWMtd2ViIiwib2lfdGtuX2lkIjoiNmFiM2M3ZjQtNTc0NC1mMTY5LWRmNDktM2ExYTJiZWQ3NmY1IiwiYXVkIjpbIkJhc2VTZXJ2aWNlIiwiUHJvdG9jb2xTZXJ2aWNlIiwiRGlzdHJpYnV0b3JTZXJ2aWNlIiwiRGVtb1NlcnZpY2UiLCJNYWluRGF0YVNlcnZpY2UiLCJXb3JrRmxvd1NlcnZpY2UiLCJDYWxjdWxhdGVTZXJ2aWNlIiwiVmVyaWZpY2F0aW9uU2VydmljZSIsIk1vbnRobHlLbm90U2VydmljZSIsIk1lc3NhZ2VTZXJ2aWNlIiwiRGlzcGF0Y2hNZXNzYWdlU2VydmljZSIsIkxvZ1NlcnZpY2UiLCJEaXNwYXRjaExvZ1NlcnZpY2UiLCJSZXBvcnRTZXJ2aWNlIiwiTWFya2V0aW5nU2VydmljZSIsIkdhdGV3YXlTZXJ2aWNlIiwiTW9udGhseU1hcmtldGluZ1BsYW5TZXJ2aWNlIl0sInNjb3BlIjoiQmFzZVNlcnZpY2UiLCJqdGkiOiJmMDgzMjI1NC00YTVmLTRiZWEtODliYy03N2FkOWNhYjkyMDIiLCJleHAiOjE3NDg1MDE3NDMsImlzcyI6Imh0dHA6Ly90cG0uY3JiLmNuLyIsImlhdCI6MTc0ODQ4Mzc0M30.ayFSiX7EsmhQQWn3-JLJLbcqgQVfsYKqKuj79B-OjkjN3M_nGV_NQE5dBcHA-j-k2dcrGa_OHFLavc1CXIOdy5g2PGV7DRdP_OKk5uA4SurakMe2TmqRy6kCbsDBMtMm5mJnxyunjOhxtK2bd5fsngtJLeGzYoJVwIQLGvfvGEYjrDfxE0pBcszh0x_PjJVI_pjeOhmNE0mNDL__2HS02CvAqgLLyqD89rXXiT_BTBHQeZvqWSuJLK6xNaj84FOv0azVCDTFS_j6ULDz0oSYaBjFs8mLhU13TCNRSN2eeq-aseSjN8wY9dfFVcQ0-k93E6BTEdLkQudp0Wg01OFyOw' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://tpm-sit.crb.cn' \
  -H 'Referer: https://tpm-sit.crb.cn/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36' \
  -H 'centerCode: 50002185' \
  -H 'centerName: %E8%BE%BD%E5%AE%81%E8%90%A5%E9%94%80%E4%B8%AD%E5%BF%83' \
  -H 'divisionCode: 50002184' \
  -H 'divisionName: %E8%BE%BD%E5%AE%81%E5%8C%BA%E5%9F%9F%E5%85%AC%E5%8F%B8' \
  -H 'headquartersCode: 50000609' \
  -H 'headquartersName: %E9%9B%AA%E8%8A%B1%E6%80%BB%E9%83%A8' \
  -H 'lastOrgCode: 50002185' \
  -H 'lastOrgName: %E8%BE%BD%E5%AE%81%E8%90%A5%E9%94%80%E4%B8%AD%E5%BF%83' \
  -H 'roleCode: Z0XT' \
  -H 'sec-ch-ua: "Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw '{"filter":{"onlyArchive":false,"operateType":"03","recordTempId":"1f6f9528f7f87a9c1fcdd74b60ff3f9c","identity":"01"},"pageNum":1,"pageSize":15}'
    
    
    """

    parsed = parse_curl(curl_commd)
    # print(parsed)
    print(to_python_code(parsed))
    # print(to_json(parsed))
