# assert False, "Dang!"
# assert True, "Boing"

# while True:
#     answer = input("What is 5 +5 ? ")
#     if "10" in answer:
#         break

# exec("print(2)")

# Lambda:
# s = lambda y: y**y
# e = s(4)
# print(e)

# def sss(y):
#     print(y**y)

# sss(4)

# print("Hello there \a everyone")
# print("Hello there \b everyone")
# print("Hello there \f everyone")
# print("Hello there \n everyone")
# print("Hello there \r everyone")
# print("Hello there \t everyone")
# print("Hello there \v everyone")
# print("Hello there \a everyone")

# my_dict = {'sword_1': "long_sword", 'sword_2': "dagger", 'wand': "simple_wood", 'wand_power': 15}
# print(my_dict)
# print(my_dict["sword_1"])

# x = b"hello"

# print(x)

# my_list = [1, 2, "hello", [3, 4, 5]]
# print(my_list[1])

import pandas as pd

# https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/

# # Initialize data in lists:
# my_data = {'Name': ["Dominik", "Sebastian", "Johannes", "Irene", "Achim", "Nicolas"], 'Age': [36, 27, 29, 45, 56, 24], 'Titel': ["Head of JRG", "PhD-Candidate", "PhD-Candidate", "Professor", "President", "Hiwi"]}

# # create dataframe
# df = pd.DataFrame(my_data)

# # prnt the output
# print(df, "\n\n")

# print(df.iloc[0][0])
# print("\n")
# print(df.iloc[2][2])
# print(df["Age"])
# print(df.iloc[0][2])
# print(df.iloc[[0]])
# print(df.iloc[[0, 1]])
# print(df.iloc[1,2])
#print(df.iloc[:,:])


print("Hello %s, how old are you? Ah, you are %s" % (12, 25)) 
name = "jojojoojo"
age = 1383811
print(f"Hello, {name}, how old are ye? Ah ye art {age}")