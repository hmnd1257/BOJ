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
    dir_li = []
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
        cnt = 0
        
        if directory not in directories:
            if directory in ["백준", "프로그래머스"]:
                content += "## 📚 {}\n".format(directory)
                content += "<details>\n"  # Move the <details> tag before the <summary> tag
                content += "<summary>접기/펼치기</summary>\n"
                content += "\n"
            else:
                content += "### 🚀 {}\n".format(directory)
                content += "| 문제번호 | 링크 |\n"
                content += "| ----- | ----- |\n"
                dir_li.append(directory)
                cnt += 1
            directories.append(directory)

        for file in files:
            if category not in solveds:
                content += "|{}|[링크]({})|\n".format(category, parse.quote(os.path.join(root)))#, file)))
                solveds.append(category)
                print("category : " + category)
        try:
            if len(dir_li) % cnt == 0:
                content += "</details>\n"
        except:
            pass
        
    with open("README.md", "w") as fd:
        fd.write(content)
        
if __name__ == "__main__":
    main()
