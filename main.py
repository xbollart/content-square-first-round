import os.path
from os import path
from mower import Mower


def parse_input_file(file_path):
    if not path.exists(file_path):
         print('Input file not found')
         return

    f = open(file_path,'r')

    content = f.readlines()

    if len(content) < 3:
        print('Input file format error: file contains:' + str(len(content)) + ' lines it should at least contains 3 lines ')
        return
    f.close

    # clean data
    for i in range(len(content)):
        content[i] = content[i].strip()

    max_grid = content[0].split(' ')
    if len(max_grid) != 2:
        print('unable to read max grid data')
        return

    i = 1
    id = 1
    mowers = []
    while i + 1 < len(content):
        initial_pos = content[i].split(' ')
        if(len(initial_pos) != 3 ):
            print('unable to read mower'+str(id)+' initial position')
        else:
            moves = list(content[i+1])
            m = Mower(id,initial_pos[0],initial_pos[1],max_grid[0],max_grid[1],initial_pos[2],moves)
            mowers.append(m)
        i += 2
        id += 1

    return mowers

def write_results(file_path,mowers):
    f = open(file_path,'w')

    for mower in mowers:
        f.write(mower.show_my_position())

    f.close

if __name__ == "__main__":

    mowers =  parse_input_file('input.txt')

    if mowers != None and len(mowers) > 0:

        for mower in mowers:
            mower.mow()

        write_results('output.txt',mowers)