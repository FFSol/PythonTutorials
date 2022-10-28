# For loops

# iterate over a sequential structure or basic sequence
# ex: list, chars in string, list of strings, etc

# for <val> in <sequence>:
    # do something

# for      : control loop keyword
# val      : the targeted item in the sequence
# in       : keyword for iterating over vals in sequence (also for checking presence)
# sequence : iterable or sequence to iterate over

for item in [1, 2, 64356, -1]:
    print(item)

for _ in range(10):
    print("just doing something, no need to use an item")


#-- While loops

# while <condition>:
    # do something

# while     : control loop keyword
# condition : conditional expression to evaluate on each pass of while loop


#-- Do While loops

# while True:
    # do something
    # if <condition>:
        # break

i = 1
while True:
    print('doing something')
    if i == 10:
        break
    i += 1
