'''total monkeys is 100 and total dorrs are 100 .
initially all doors ae closed . as 1st monkey come
then he opens all the doors and when 2nd monkey comes then
he open only that door which are in the table of 2 as the
same way 3rdmoney opens the door olnly comes in 3 table and so on .
at last after visiting 100th monkey how many doors are open and closed'''



doors=100
open_doors=[0]*doors

# print(open_doors)

for monkey in range(1,doors+1):
    for door in range(monkey,doors+1,monkey):
        open_doors[door-1]=1-open_doors[door-1]
        
        # print(f"monkey {monkey}  doors : {door}")
        # print(open_doors)




print("open doors",open_doors.count(1))
print("closed doors",open_doors.count(0))



