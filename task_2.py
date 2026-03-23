
curriculum=[]

for week in range(1,17):
    if week % 4==0:
        curriculum.append("контроль")
    else:
        curriculum.append(4)

    print('учебный план на семестр:')
    print(curriculum)

   