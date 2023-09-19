if __name__ == '__main__':
    n = int(input())
    my_list = []
    for _ in range(n):
        choice = list(input().split())
        if (choice[0] == 'insert'):
            my_list.insert(int(choice[1]), int(choice[2]))
        elif (choice[0] == 'print'):
            print(my_list)
        elif (choice[0] == 'remove'):
            my_list.remove(int(choice[1]))
        elif (choice[0] == 'append'):
            my_list.append(int(choice[1]))
        elif (choice[0] == 'sort'):
            my_list.sort()
        elif (choice[0] == 'pop'):
            my_list.pop()
        else:
            my_list.reverse()
        