from grading import find_total,find_average,find_grade

math=int(input("enter scores for Math "))
eng=int(input("enter scores for English "))
kisw=int(input("enter scores for Kiswahili "))
sci=int(input("enter scores for Science "))
sst=int(input("enter scores for SST "))

total=find_total(math,eng,kisw,sci,sst)

print(total)

average=find_average(total)

grade=find_grade(average)

print(average)
print(grade)