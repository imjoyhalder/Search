
new_list = []
def search(list):
    if len(list) <=1:
        return list
    else: 
        new_list = list[0]
        left = []
        right = []
        for i in range(1,len(list)):
            if list[i]<new_list:
                left.append(list[i])
            else:
                right.append(list[i])
        return search(left) + [new_list] +search(right)
    

list = [5,2,1,7,3,5]
print(search(list))