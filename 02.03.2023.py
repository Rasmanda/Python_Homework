# 1 task. Write a function to find the max of 3 numbers(NOT FINISHED, IT IS NOT WORKING)
def max_of_two(a, b):
    if a > b:
        return a
    def max_of_three(a, b, c):
        return max_of_two( a, max_of_two( b, c))
    print(max_of_three(2, 4, 6))

# 2 task.reverse a string (how to separate? keeps on breaking the word it self if i try to separata taske 2 and task 3)
word = input("input word: ")
for x in range(len(word)-1, -1, -1):
    print(word[x], end="")


# 3 task.
def sum_numbers(*numbers: float) -> float:
    """sum numbers """
    return sum(numbers)
print(sum_numbers(1.16, 2, 3, 4, 5))



