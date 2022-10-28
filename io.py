a = 5.3405893
print('The value of a is', a)

# but Mr Armani, what if I'm a pretentious little function user?
boob = 10
print('The value of a is {} and boob is {}'.format(a,boob))

# variables are hard, so you aren't required to define them in advance tho
print('Some value is {} and something else is {}'.format("this", "that"))

# you can make your life harder too, and use annoying printing methods like this
print('The value of a is %3.2f' %a)

# fstrings, an elegant function for a more civilized age
color = 'tan'
height = 12
print(f'The {color} dog jumped {height} feet in the air')


# can you guess what the keyword is for user input is?
# if you said 'Input', you're WRONG.....it's 'input' (case matters)
question = "What is your name? " # keep in mind, I added a space to the end
name = input(question)
print(name)

# for when you want to evaluate some expression, command, or string
res = eval('1 + 1')
print(res)


# Reading Files (stolen from Google doc)

# Echo the contents of a text file
f = open('foo.txt', 'rt', encoding='utf-8')
for line in f:              ## iterates over the lines of the file
    print(line, end='')     ## end='' so print does not add an end-of-line char
                            ## since 'line' already includes the end-of-line.
f.close()

# or we can take all the lines at once
f = open('foo.txt', 'rt', encoding='utf-8')
entire_file = f.readlines()

f.close()


# Writing to Files
f = open('foo.txt', 'rt', encoding='utf-8')

f.write('poop')                 ## using the write() function
print('BEEG YOSHI', file=f)     ## using the print() function

f.close()                       ## remember to close your files, it's like leaving your fly unzipped
