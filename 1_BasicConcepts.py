#this is how you make comments

#output are made like this. Like java you can use \n and \t. To add a number after the text use ,
print("This is an output.\nOperation examples: ", 1+1, 1*5, 6-3, 6/2, 4**2, 10//3, 10%3, "\n")

#with """ you can write the text with indentetion on different level
print("""this 
is a 
multiline
text""")

#concatenation of strings is done like this
print("\nthis is a " + "concatenation")

#you can repeat strings
print("\nsend help"*3)

#variables are assigned like this, and...
pin = "1234" #this is a string
pon = 1234   #this is an int

#input is taken like this, and always return a string, you can write the output inside the input()
username = input("Choose your username: ")
print("Nice username, " + username)

#you can convert with int(), str(), float(), to get an int in input for example
age = int(input("\nHow old are you? "))
print("\nAhahah u r ", age)



#LISTS
#list are written like this and can contain different types and also other lists, to make for example a matrix
nums = ["spam", "eggs", "melon", "spam"]
print("The list contains: ", nums)

#using in you can search for something inside a list or check if a string is a substring
if "spam" in "spamming":
    print("\nyesh")
else:
    print("\nnope")
#using not in you can check the opposite

#append adds stuff at the end of a list
nums.append("salty")

#to obtain the lenght of a list
print("\nThe list is long ", len(nums))

#insert let you add stuff in a specified position and shift everything to the right
nums.insert(2, "pb&j")

#index return the first index of the element searched
nums.index("melon") 

#we also have...
max(nums) #return max element
min(nums) #return min element
nums.count("spam") #return how many time something occur
nums.remove("spam") #remove the element
nums.reverse() #reverse items in list



#WHILE
i = 0
while i<=5:
    print(i)
    i += 1
    if i == 4:
        break #'continue' and 'break' behaves like in java

print("Finished!")

#FOR 
#essenzialmente funziona come un for each
words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word)

count = 0
words = "This is a string"
for x in words:
    count += 1

print("The string contains " + str(count) + " lecter")

#RANGE
#return a sequence of numbers, by default start from 0 and increments by 1 until the specified number
numbers = list(range(10)) #list containing numbers up to 10
range(0, 20) #return range from 0 to 19
range(5, 20, 2) #from 5 to 20 but an interval of 2
range(20, 5, -2) #order reversed

#can be used to repeat code a certain number of time
for i in range(5):
    print("Hellooo")