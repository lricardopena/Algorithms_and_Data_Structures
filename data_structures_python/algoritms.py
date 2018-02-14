def addFunction(list1, list2):
    carryadd = False
    listadded = []
    i,j = 0, 0
    while i < len(list1) or j < len(list2):
        number = 0
        if i < len(list1) and j < len(list2):
            number = list1[i] + list2[j]
            j += 1
            i +=1
        elif i < len(list1):
            number = list1[i]
            i += 1
        elif j < len(list2):
            number = list2[j]
            j +=1

        if carryadd:
            number += 1

        if number >= 10:
            carryadd = True
            number -= 10
        else:
            carryadd = False
        listadded.append(number)

    if carryadd:
        listadded.append(1)
    return listadded



list1 = [9]
list2 = [9,9,9]

addlist = addFunction(list1,list2)
print addlist