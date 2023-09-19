if __name__ == '__main__':
    class_room = []
    arrange = set()
    
    for _ in range(int(input())):
        student = []
        name = input()
        score = float(input())
        arrange.add(score)
        student.append(name)
        student.append(score)
        class_room.append(student)
        
    class_room.sort(key = lambda x : (x[1], x[0]))
    arrange1 = sorted(arrange)
    
    for i in range(len(class_room)):
        if class_room[i][1] == arrange1[1]:
            print(class_room[i][0])