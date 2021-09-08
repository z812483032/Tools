# -*- encoding:utf-8 -*-

import re
import win32clipboard as w
import win32con


def get_text():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_UNICODETEXT)
    w.CloseClipboard()
    return d.encode('GBK').decode('GBK')

def set_text(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

def format_conversion():
    pattern = "^(.*?): (.*)$"
    string = get_text()
    result = ''
    for line in string.splitlines():
        result += re.sub(pattern, '\'\\1\': \'\\2\',', line) + '\n'
    set_text(result)

if __name__ == '__main__':
    format_conversion()
