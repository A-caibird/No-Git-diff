import os
from index import read_file, highlight_diff

def main():
    a_txt = 'test_data/a.txt'
    b_txt = 'test_data/b.txt'
    
    a_txt = os.path.abspath(a_txt)
    b_txt = os.path.abspath(b_txt)

    file1_content = read_file(a_txt)
    file2_content = read_file(b_txt)

    highlight_diff(file1_content, file2_content)

if __name__ == '__main__':
    main()
