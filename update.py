#!/usr/bin/env python

import os
from urllib import parse

HEADER="""# 
# 백준 & 프로그래머스 문제 풀이 목록
"""

def main():
    content = ""
    content += HEADER
    
    directories = [];
    solveds = [];
    table_header_added = True
    
    for root, dirs, files in os.walk("."):
        dirs.sort()
        if root == '.':
            for dir in ('.git', '.github'):
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        category = os.path.basename(root)
        
        if category == 'images':
            continue
        
        directory = os.path.basename(os.path.dirname(root))
        
        if directory == '.':
            continue
            
        if directory not in directories:
            if directory in ["백준", "프로그래머스"]:
                content += "## 📚 {}\n".format(directory)
            else:
                content += "### 🚀 {}\n".format(directory)
                content += '<details>\n'
                content += '<summary>접기/펼치기</summary>\n'
                if not table_header_added:
                    content += '\n'
                    content += "| 문제번호 | 링크 |\n"
                    content += "| ----- | ----- |\n"
                    table_header_added = False
                    
            directories.append(directory)

        for file in files:
            if category not in solveds:
                content += "|{}|[링크]({})|\n".format(category, parse.quote(os.path.join(root)))#, file)))
                solveds.append(category)
                print("category : " + category)
                
        if directory not in ["백준", "프로그래머스"]:
            content += "</details>\n"
            
    with open("README.md", "w") as fd:
        fd.write(content)
        
if __name__ == "__main__":
    main()
