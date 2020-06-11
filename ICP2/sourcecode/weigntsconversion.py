# converting weights into kgs
N = int(input("Enter number of students? "))
lbs = []
for i in range(N):
    lb = float(input("Enter the weight of each student: "))
    lbs.append(lb)
print("Given weights in lbs ", lbs)

# list comprehension

kgs = [x * 0.45359237 for x in lbs]

print("Weights converted int0 kgs: ", kgs)
