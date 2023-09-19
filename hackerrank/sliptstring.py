def split_and_join(line):
    line = line.split()
    s = ''
    for i in range(len(line)):
        s += line[i]
        if (i < len(line) - 1):
            s += '-'
    return s
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)