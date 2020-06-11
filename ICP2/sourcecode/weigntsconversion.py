# converting weights into kgs
N = int(input("Enter number of students? "))
lbs = []    # defining the list
for i in range(N):
    lb = float(input("Enter the weight of each student: "))
    lbs.append(lb)      # appending the values to  a list
print("Given weights in lbs ", lbs)

# using list comprehension to convert lbs to kgs
kgs = [x * 0.45359237 for x in lbs]
print("Weights converted into kgs: ", kgs)
