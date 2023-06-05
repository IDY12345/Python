
input_string = input('Enter elements of a list separated by space ')
print("\n")
user_list = input_string.split()


# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])


print("Sum = ", sum(user_list))
print("Max = ",max(user_list))
print("Min = ",min(user_list))
print("Total Numbers = ",len(user_list))
print("Avg = ", sum(user_list)/(len(user_list)))