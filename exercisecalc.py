name = ['Abraham','Jesus','beto']
scores = [['40.0','30.4','100.3'],['90.0','70.5','50.5'],['100.0','110.0','70.8']]
students = dict(zip(name,scores))

print(f'\n-----------Start the List-----------\n')



def calculate_grades():
    for key, value in students.items():
        k = students.get(key)
        kfloat = [float( scores) for scores in k]
        average = sum(kfloat) / len(kfloat)

        print(f'The list of scores is: {kfloat}')
        print(f'The average for {key} is: {average:.2f}\n\n')

calculate_grades()

       