# Define two lists: one for names and one for corresponding scores.
name = ['Abraham','Jesus','beto']
scores = [['40.0','30.4','100.3'],['90.0','70.5','50.5'],['100.0','110.0','70.8']]
# Use zip() to combine the two lists into a dictionary where names are keys and scores are values.
students = dict(zip(name,scores))

print(f'\n-----------Start the List-----------\n')



# Define a function to calculate grades.
def calculate_grades():
    # Loop through each student (key-value pair) in the dictionary.
    for key, value in students.items():
        k = students.get(key)
        # Convert the list of score strings to a list of floats.
        kfloat = [float( scores) for scores in k]
        # Calculate the average of the scores.
        average = sum(kfloat) / len(kfloat)

        print(f'The list of scores is: {kfloat}')
        print(f'The average for {key} is: {average:.2f}\n\n')

# Call the function to perform the calculations.
calculate_grades()

       