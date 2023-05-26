def selection_sort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j
                    
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
        print("The array after",i+1,"pass",nums)

    print ("Sorted array")
    print(nums)
temp = int(input("Enter the  numbers elements to be sorted: "))
nums = []
for i in range(temp):
    element = int(input("Enter the element:"))
    nums.append(element)
sorted_nums = selection_sort(nums)