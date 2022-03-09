# catching exceptions, the try catch except finally pattern
# some errors include KeyError, IndexError,FileNotFound error and many other more
# we should catch these exceptions so that we don't fail catastrophically
# try: something that might cause an exception
# except: do this if there was an exception
# else: do this if there we no exceptions (errors)
# finally: do this no matter what

# in the except block, we should specify the error we are looking for or else all the other errors in the try block will be ignored

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["non_existing_key"])
    print(a_dictionary["key"])
except FileNotFoundError:
    # we create the file
    file = open("a_file.txt", "w")
    file.write("Something written to the file")
except KeyError as error_message:
    print(error_message)
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("The code in this 'finally' block must be run no matter what.")

    # raise KeyError("This is an error that I made up.") #raising our own exceptions

# height = float(input("height: "))
# weight = float(input("weight: "))
# bmi = weight / height ** 2

# if height > 3:
#     raise ValueError("The height you entered is invalid.")

fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")

make_pie(0)


facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        current = post['Likes']
    except KeyError:
        pass
    else:
        total_likes = total_likes + current


print(total_likes)
