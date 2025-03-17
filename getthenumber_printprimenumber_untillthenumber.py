def count_prime(num):
    for i in range(2,num):
        for j in range(2,i):
            if i%j==0:
                break     
        else:
            print(i,end=" ")

user_num=int(input("Enter the number : "))
count_prime(num=user_num)