# file = open("hello.txt")
# content= file.read()
# print(content)


# Write to file
# file =  open("Hello.txt", "w")
# file.write("Let's become a django developer")
# file.close()

#append to file
# file = open("Hello.txt", "a")
# file.write("\n Let's become a pytbon developer")
# file.write("\n Let's become a AI developer")

# creating a folder
# import os
# try:
#     os.mkdir("my folder")
#     print("Folder created successfully")

# except:
#     print("Folder already exists")

# deleting a folder
import os
try:
    os.rmdir("my folder")
    print("Folder deleted successfully")

except:
    print("Folder does not exist")
