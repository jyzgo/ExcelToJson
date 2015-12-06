#-*- coding: utf-8 -*-
import codecs
import os
import shutil
import re
import chardet
def convert_encoding(filename, target_encoding):
    # Backup the origin file.
    shutil.copyfile(filename, filename + '.bak')
 
    # convert file from the source encoding to target encoding
    content = codecs.open(filename, 'r').read()
    source_encoding = chardet.detect(content)['encoding']
    print source_encoding, filename
    content = content.decode(source_encoding) #.encode(source_encoding)
    codecs.open(filename, 'w', encoding=target_encoding).write(content)
 
def main():
    for root, dirs, files in os.walk(os.getcwd()):
        for f in files:
            if f.lower().endswith('.java'):
                filename = os.path.join(root, f)
                try:
                    convert_encoding(filename, 'utf-8')
                except Exception, e:
                    print filename
 
def process_bak_files(action='restore'):
    for root, dirs, files in os.walk(os.getcwd()):
        for f in files:
            if f.lower().endswith('.java.bak'):
                source = os.path.join(root, f)
                target = os.path.join(root, re.sub('\.java\.bak$', '.java', f, flags=re.IGNORECASE))
                try:
                    if action == 'restore':
                        shutil.move(source, target)
                    elif action == 'clear':
                        os.remove(source)
                except Exception, e:
                    print source
 
if __name__ == '__main__':
    # process_bak_files(action='clear')
    main()
