days = ['monday','tuesday','sunday']

for day in days:
    if days.index(day) == 1 or days.index(day)==2:
        print('Toi khong di lam vao ' +day)
    else:
        print('toi di lam vao ' +day) 

