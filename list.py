if __name__ == '__main__':
    N = int(input())
    answer =[]
    for i in range(N):
        temp = list(input().split())
        if temp[0]=="insert":
            answer.insert(int(temp[1]),int(temp[2]))
        elif temp[0]=="print":
            print(answer)
        elif temp[0]=="remove":
            answer.remove(int(temp[1]))
        elif temp[0]=="append":
            answer.append(int(temp[1]))
        elif temp[0]=="sort":
            answer.sort()
        elif temp[0]=="pop":
             answer.pop()
        elif temp[0]=="reverse":
              answer.reverse() 
            
