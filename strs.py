# my_string = 'Hello'
# print(my_string)

# my_string = "Hello"
# print(my_string)
#
my_string = '''Hello'''
print(my_string)
#
# triple quotes string can extend multiple lines
my_string = """Hello, someone please
               help me, I'm stuck in this computer"""
print(my_string)

str = 'programiz'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])


#immutabliity (wtf is that huh)
my_string = 'applesauce or something idk'
my_string[5] = 't'

# oh no mr armani I broke the program
# let's try this instead
del my_string[1]
#look at what you've done


# Python String Operations
str1 = 'Hello'
str2 ='World!'

# using +
print('str1 + str2 = ', str1 + str2)

# using *
print('str1 * 3 =', str1 * 3)

#iteration (we'll get into this soon)
count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')
