print ("your data:")

def mo (nums:list):
    total = 0
    for i in nums:
        total += i
    return total / len(nums)

def disp (nums:list):
    math_exp = mo(nums)
    total = 0
    for i in nums:
        total += pow(i - math_exp, 2)
    return total / len(nums)

def print_statistical_range (nums:list):
    nums.sort()
    count = 0
    tmp = nums[0]
    for i in nums:
        if (i == tmp):
            count += 1
        else:
            print(str (tmp) + " - " + str (count))
            tmp = i
            count = 1
    print (str (tmp) + " - " + str (count))

def print_interval_range (nums:list, n_inreval:int):
    step = (max(nums) - min (nums)) / n_inreval
    nums.sort()
    count = 0
    tmp = nums[0]
    for i in nums:
        if (i < tmp + step):
            count += 1
        else:
            print(str (tmp) + ".." + str (tmp + step) + " - " + str (count))
            while tmp + step < i:
                tmp += step
            count = 1
    print (str (tmp) + ".." + str(tmp + step) + " - " + str (count))

nums = []

for i in input().split():
    nums.append(float(i))

print(max (nums) - min (nums))

print_statistical_range (nums)

print ("MO = ", mo(nums))

print ("DISP = ", disp(nums))
