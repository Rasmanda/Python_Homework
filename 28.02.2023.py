# numbers from 0 to 100 that are divisible y 7
y = 1
while y <= 100:
    y += 1
    if y % 7 == 0:
        print(y)

# reverse a word. it should be done using input function
word = input("input word: ")
for x in range(len(word)-1, -1, -1):
    print(word[x], end="")
