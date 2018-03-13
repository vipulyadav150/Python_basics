s = ('Physics' , 'Chemistry' , 'Mathematics')


n = int(input("Enter the number of students : \n"))
data = {}
for i in range (0 , n):
    name = input("Enter the  name of student %d :\n" %(i+1))
    marks = []
    g = 1
    for x in s :
        while True:
            try:
                marks.append(int(input("Enter  marks for %s : \n" %(x))))
                break
            except ValueError:
                print("Make sure you enter a number!Try again")
                continue

    data[name] = marks
    total = 0

for k,v in data.items():
    total = sum(v)
    if total < 120:
        print("%s failed!\n" %(k))
    else :
        print("%s Passed!\n" %(k))

