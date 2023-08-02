import statistics
print("Find the mean of two numbers")

fnum = int(input("first num: "))
snum = int(input("second num:"))
stat =  statistics.mean([fnum, snum])
print(f"your answer is: {stat}")
