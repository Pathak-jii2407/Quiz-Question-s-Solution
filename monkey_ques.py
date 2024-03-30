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



