import sys
#import argparse

#ログを抽出する
argvs = sys.argv

ld = open(argvs[1], 'r')
lines = ld.readlines()
ld.close()

f = open(argvs[2], 'w')
for line in lines:
    if line.find(argvs[3]) >= 0:
        f.write(line[:-1])
        f.write('\n')

#コマンドライン引数の説明
#parser = argparse.ArgumentParser(description='特定の文字列のある行を抽出、1番目の引数で読み込むファイルを指定、2番目の引数で書き込むファイルを指定、3番目の引数で検索する文字列を指定する')
#parser.add_argument('r', required=True)
#parser.add_argument('-v', action='version', version='%(prog)s 0.1')
#args = parser.parse_args()
#print(args)
