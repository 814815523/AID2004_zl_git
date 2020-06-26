



for r in list(n):
    for c in range(len(list1)-1,-1,-1):
        if r == list1[c] :
            del list1[c]
            break

print(n-set(list1))

'''


'''
小明家必须要过一座桥。小明过桥最快要１秒，小明的弟弟最快要３秒，
小明的爸爸最快要６秒，小明的妈妈最快要８秒，小明的爷爷最快要１２秒。
每次此桥最多可过两人，而过桥的速度依过桥最慢者而定。
过桥时候是黑夜，所以必须有手电筒，小明家只有一个手电筒，
而且手电筒的电池只剩30秒就将耗尽。小明一家该如何过桥，请写出详细过程。
'''

list_time = [1,3,6,8,12]

def get_total_time(list_target):
    new_target = sorted(list_target)
    print(new_target)
    length = len(new_target)
    if 0<length < 3:
        return new_target[-1]

    elif length==3:
        total_time =  new_target[0] + new_target[1] + new_target[2]
        return  total_time

    elif length>3:
        number = length -2
        if number%2==0:
            total_time = (2*new_target[1]+new_target[0]) * (number // 2)+new_target[1]
            for i in range(length-1,1,-2):
                total_time +=new_target[i]
                return total_time
        else:
            total_time =  (2*new_target[1]+new_target[0]) *((number-1)//2)+new_target[0]+new_target[1]+new_target[2]
            for i in range(length-1,1,-2):
                total_time += new_target[i]
                return total_time

result = get_total_time(list_time)
print(result)



