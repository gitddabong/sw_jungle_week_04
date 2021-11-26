#-*- coding:utf-8 -*-
import os 
def generate_folders(problems_str):
    '''generate_folder.py파일이 있는 위치에 백준코딩 문제 폴더 생성 함수 
    
    Args: 
        problems_str (str): whitespace로 구분된 백준 문제 번호 스트링
    Returns:
        None
    '''
    problems_list = problems_str.split()
    path_root = os.getcwd()
    for num in problems_list:
        os.mkdir(os.path.join(path_root, num))


if __name__ == '__main__':
    problems_str = '''9084
9251
12865
11049
11053
2098
2253
11047
1541
1931
1946
1700
9249
'''
    generate_folders(problems_str)
