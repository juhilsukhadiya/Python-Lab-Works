# # # # i=0
# # # # while(i<=4):
# # # #     j=0
# # # #     while(j<=4):
# # # #         print(i,j)
# # # #         j=j+1
# # # #     i = i+1     

# # # # n=6
# # # # i=0
# # # # while(i<n):
# # # #     j=0
# # # #     while(j<n):
# # # #         print("*", end="")
# # # #         j=j+1
# # # #     print("\n")
# # # #     i = i +1    

# # # i=1
# # # while i<=5:
# # #     j=1
# # #     while j<=i:
# # #         print("*", end="")
# # #         j += 1
# # #     print()
# # #     i += 1    


# # # i    j      condaation (j <= i)  output
# # # 1    1      True                     *
# # # 1    2      False               go to new  line
# # # 2    1      True                    **
# # # 2    3      false                go to new line
# # # 3    1      true                  ***
# # # 3    4      false                  go to new line
# # # 4    1      

# # n=4 
# # i= n

# # while i>=1:
# #     j=1
# #     while j<= n -i:
# #         print("?",end="")
# #     z=1   

# #     while z<=i:
# #         print("*", end="")
# #         z=z+1
# #     print()
# #     i=i-1 /
# # n=5
# # i=n
# # while(i>=1):
# #     j=1
# #     while(j<i):
# #         print("?", end="")
# #         j += 1
# #     z=0
# #     while(z<=n-i):
# #         print("*", end="")
# #         z += 1
# #     print()
# #     i -= 1

# i=5, j= 1->5, z= 0->1    ????*
# i=4, j= 1 ->4 ,z=0->2    ???**
# i=3, j=1->3,z=0->3       ??***
# i=2,j=1->2,z=0->4        ?****
# i=1, j=1,z=0->5          *****


# n = 5
# i = 1

# while i <= n:
#     j = 1

    
#     while j <= n-i:
#         print(" ", end="")
#         j += 1

    
#     j = 1
#     while j <= 2*i-1:
#         print("*", end="")
#         j += 1

#     print()
#     i += 1

i=1,n-i(5-1=4),2*i-1(2*1-1=1)      *
i=2,n-i(5-2=3),2*i-1(2*2-1=3)     ***
i=3,n-i(5-3=2),2*i-1(2*3-1=5)    *****
i=4,n-i(5-4=1),2*i-1(2*4-1=7)   *******
i=5,n-i(5-5=0),2*i-1(2*5-1=9)  ********* 