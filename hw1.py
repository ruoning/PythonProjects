PATH = "/Users/ruoningli/Desktop/ruoning/test.txt"

lines = 0
age = 0
birth = 0

greatest_age = ""
greatest_birth = ""

with open(PATH) as file_doc:
    for data in file_doc.readlines():
        if data == "\n":
            continue
        lines += 1
        print(data)

        words = data.split(',')
        if words[1] > age:
            age = words[1]
            greatest_age = words[0]

        dates = words[2].split('-')
        if dates[2] > birth:
            birth = dates[2]
            greatest_birth = words[0]

print("Total number of kids is " + str(lines))
print("The kid with greatest age is " + greatest_age)
print("The kid with greatest date of birth is " + greatest_birth)


