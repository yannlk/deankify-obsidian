import os

dir_list = ['Zettelkasten', 'One-Time', 'Archive', 'Reading Notes']


def deankify_file(filename):
    print(filename)
    with open(filename, 'r') as y:
        lines = y.readlines()

    for line in lines:
        if '<!--ID:' in line:
            lines.remove(line)

    with open('newvault/' + filename, 'x') as x:
        x.writelines(lines)


for directory in dir_list:
    for file in os.listdir(directory):
        if file.split('.')[1] == 'md':
            deankify_file(directory + '/' + file)
