def fileapi(pathstr_of_file=None):
    f1 = open(pathstr_of_file)
    lines_list = list()
    lines = f1.readlines()
    totl_lines = len(lines)
    print(lines)
    for i in range(0,totl_lines):
        line = lines[i]
        if line.find('*') != -1:
            print(line)
            lines_list.append(line)
    f1.close()
    print(lines_list)
def fileapi2(pathstr_of_file=None):
    with open(pathstr_of_file,"r") as f:
        print(f.read(1))
        print(f.read(1))
        llist = list(f)
        ltuple = tuple(f)
        lset = set(f)
        print("lset is :" , lset)
        print("llist is :", llist)
        print("ltuple is :", ltuple)
        # for line in f:
        #     print(line,end="")
def fileapi3(pathstr_of_file=None):
    with open(pathstr_of_file,"r") as f:
        print(f.readline())
        print(f.readline())
        l = f.readline()
        while l:
            print(l)
            l = f.readline()


if __name__ == '__main__':
    # fileapi('f1.txt')
    # fileapi2('f1.txt')
    fileapi3('f1.txt')