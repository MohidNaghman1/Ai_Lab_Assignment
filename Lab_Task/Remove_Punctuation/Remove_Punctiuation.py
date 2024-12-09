def Remove_Punctuation(x):

    list1 = []

    for i in x:
        if i.isalpha():
            list1.append(i)

        
    return("".join(list1))
        

inp = input("Enter Your String: ")

x = Remove_Punctuation(inp)
print(x)