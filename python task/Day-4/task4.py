test_dtr_lst = ("    ** user_945 % user_745 | | user_654 user_80  t   est123@gmail.com         ")

# print(test_dtr_lst)
test_dtr_lst1 = test_dtr_lst.strip().split()
print(test_dtr_lst1)
test_dtr_lst2 = test_dtr_lst.split()

# print(test_dtr_lst2)
# print(test_dtr_lst)

test_dtr_str1 = test_dtr_lst1.pop(0)
test_dtr_str1 = test_dtr_lst1.pop(1)
test_dtr_str1 = test_dtr_lst1.pop(2)
test_dtr_str1 = test_dtr_lst1.pop(2)
test_dtr_str1 = test_dtr_lst1.pop(-1)
test_dtr_str1 = test_dtr_lst1.pop(-1)
print(test_dtr_lst1)
# print(test_dtr_lst[1])
# print(test_dtr_lst[3])
# print(test_dtr_lst[6])
# print(test_dtr_lst[7])

st = test_dtr_lst2[8]
st += test_dtr_lst2[9]
# st = st.join("")

print(st)