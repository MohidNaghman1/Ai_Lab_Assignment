# sen = input("Enter Your Sentence: ")
# x = sen.split(' ')
# print(x[0][0])

def Sort_Text(text1):
    x = text1.split()
    text_length = len(x)
    for i in range(0,text_length+1):
        for j in range(0, text_length - i - 1):
                # Swap if the current character is greater than the next
                if ord(x[j][0]) > ord(x[j+1][0]):
                    x[j], x[j+1] = x[j+1], x[j]

                # print(x[i][0])
                # print(x[i+1][0])
                # print()
    return ' '.join(x)

#     return tex
text1 = "hello I am Mohid Ai no"
print(Sort_Text(text1))






 





