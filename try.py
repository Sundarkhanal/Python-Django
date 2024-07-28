a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

print(a.lower())
print(a.upper())
print(a.count('do'))
print(a.find("do"))
print(a.find("universe"))

#using replace method
print(a.replace("do", "done"))

#concatenation of two strings
greeting = "Hello"
name = "Ram"

message = greeting + ','+name 
message = (f"{greeting}, {name} good morning")
print(message)

print(dir(name))

print(help(message.lower()))