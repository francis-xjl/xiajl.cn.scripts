#!/usr/bin/env python
# encoding: utf-8
"""
@author: francis
@contact: francis.xjl@qq.com
@file: download_backup.py
@time: 2018/5/15 9:58
@desc:
"""

import requests
import time

BACK_UP_ROOT = "F:/xiajl.cn_backups/"
BACK_UP_SITE = "http://[username]:[password]@backup.xiajl.cn/"

def backup_db():
    """
    备份数据库文件
    :return:
    """
    filename = BACK_UP_ROOT + "db_" + str(time.strftime("%Y%m%d%H%M%S")) + ".gz"
    r = requests.get(BACK_UP_SITE + '/solo.latest.gz', stream=True)
    with open(filename, 'wb') as fd:
        for chunk in r.iter_content():
            fd.write(chunk)
    pass


def backup_file():
    """
    备份图片文件
    :return:
    """
    filename = BACK_UP_ROOT + "file_" + str(time.strftime("%Y%m%d%H%M%S")) + ".tar.gz"
    r = requests.get(BACK_UP_SITE + '/xiajl.cn.tar.gz', stream=True)
    with open(filename, 'wb') as fd:
        for chunk in r.iter_content():
            fd.write(chunk)
    pass

if __name__ == "__main__":
    backup_db()
    backup_file()