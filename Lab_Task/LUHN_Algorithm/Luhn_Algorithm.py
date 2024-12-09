
def Check_card(card_number):
    List = list(card_number)
    # fetch the last element
    pop_Item = List[-1]
    # pop the last element
    List = List[0:-1]
    # print(List)
    # reverse the list
    R_List = List[::-1]
    # print(R_List)
    # Loop on the lenght of R_list 
    for i in range(len(R_List)):
        # check the index is even
        if i % 2 == 0:
            # multiply by 2 if even
            R_List[i] = R_List[i] * 2
                
        else:
            # if not even
            R_List[i] = R_List[i]
        #  after multiply if value is greater then 9 then subtract 9 
        if R_List[i] > 9:
                R_List[i] = R_List[i] - 9
    # print(sum(R_List)+pop_Item)
    # check the sum of the list and the last element is divisible by 10
    sum1 = sum(R_List)+pop_Item
    if sum1 %10 == 0:
        print("Valid Card Number")
    else:
        print("Invalid Card number")

x = [5,8,9,3,8,0,4,1,1,5,4,5,7,2,8,9]
Check_card(x)