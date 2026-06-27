# 编写一个程序，使用 map() 和 filter() 生成一个列表，该列表的元素是 [1,2,3,4,5,6,7,8,9,10] 中奇数的平方。

my_list = [1,2,3,4,5,6,7,8,9,10]

result1 = filter(lambda x: x % 2 != 0, my_list)

expect_list1 = list(result1)

result2 = map(lambda x: x ** 2, expect_list1)

expect_list2 = list(result2)

print(expect_list2)




