import os
import sys

def get_all_md_files(base_path, file_list):
    path_arr = os.listdir(base_path)
    for e in path_arr:
        sub_path = base_path + '/' + e 
        if os.path.isdir(sub_path):
            get_all_md_files(sub_path, file_list)
        elif sub_path.endswith('.md'):
            file_list.append(sub_path)

def insert_text_before_string(file_path, target_string, insert_text):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    find_seq_count = 0
    with open(file_path, 'w') as f:
        for i in range(len(lines)):
            if target_string in lines[i] and find_seq_count < 2:
                find_seq_count += 1
                if find_seq_count == 2:
                    f.write(insert_text + '\n')
            f.write(lines[i])

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        base_path = sys.argv[1]
        target_name = sys.argv[2]
    else:
        print("python add_permalink.py [base_path] [target_name]")
        print("python add_permalink.py c:\dlr\programming-old programming")
        exit

    #print(base_path, target_name)

    file_list = []
    get_all_md_files(base_path, file_list)

    for file in file_list:
        print(file)

        target_content = 'permalink: /' + target_name + file[len(base_path):-3]+'.html'
        insert_text_before_string(file, '---', target_content)
