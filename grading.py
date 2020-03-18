def find_total (math,english,kiswahili,science,sst):
    total = math+english+kiswahili+science+sst
    return total
#x=find_total(math=50,english=79,kiswahili=80,science=90,sst=68)


def find_average(total):
    average = total/5
    return average

#y=find_average(x)

def find_grade(avg):


    if avg >= 80 and avg <= 100:
        return "A"
    elif avg >= 75 and avg <= 79:
        return "A-"
    elif avg >= 70 and avg <= 74:
        return "B+"
    elif avg >= 65 and avg <= 64:
        return "B"
    elif avg >= 60 and avg <= 69:
        return "B-"
    elif avg >= 55 and avg <= 59:
        return "C+"
    elif avg >= 50 and avg <= 54:
        return "C"
    elif avg >= 45 and avg <= 49:
        return "C-"
    elif avg >= 40 and avg <= 44:
        return "D+"
    elif avg >= 35 and avg <= 39:
        return "D"
    elif avg >= 30 and avg <= 34:
        return "D-"
    elif avg >= 0 and avg <= 29:
        return "E"
    else:
        return ("Invalid")


#grade=find_grade(y)

#print(grade)
#print(x)
#print(y)