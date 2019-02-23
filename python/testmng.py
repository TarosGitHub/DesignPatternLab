#! /usr/bin/env python

import sys
from unittest import TestLoader
from unittest import TextTestRunner

def main(path):
    loader = TestLoader()
    test = loader.discover(path)
    runner = TextTestRunner()
    runner.run(test)

if __name__ == '__main__':
    #if len(sys.argv) != 2:
    #    print('usage: %s path' % sys.argv[0])
    #    sys.exit(1)

    # 全テスト実行
    # 現在のディレクトリ(PythonLab)フォルダ配下のテストをすべて実行
    # 現在のディレクトリ(PythonLab)を指定しないと、
    # 各テストのモジュールのimport(from ... import ...)でエラーになってしまう。 
    #main(sys.argv[1])
    main(".")
