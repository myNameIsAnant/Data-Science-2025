
"""
What is 7 to the power of 4?
"""


print(7 ** 4)

"""
Split this string:
s = "Hi there Sam!"
into a list.
"""

s = "Hi there Sam!"

result = s.split()

print(result)

"""
Given the variables:
planet = "Earth"
diameter = 12742
Use .format() to print the following string

The diameter of Earth is 12742 kilometers.
"""

planet = "Earth"
diameter = 12742
print("The diameter of {} is {} kilometers.".format(planet, diameter))

"""
Given this nested list, use indexing to grab the word "hello"
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
"""
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

print(lst[3][1][2][0])


"""
Given this nested dictionary grab the word "hello". 
Be prepared, this will be annoying/tricky 
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
"""

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

print(d["k1"][3]["tricky"][3]["target"][3])

"""
What is the main difference between a tuple and a list?
"""


"""
Create a function that grabs the email website domain 
from a string in the form:
user@domain.com
So for example, passing "user@domain.com" would return: domain.com
"""
def extract_website_domain(email):
    return email.split('@')[-1]
email= "user@domain.com"
print(extract_website_domain(email))

"""
Create a basic function that returns True if the 
word 'dog' is contained in the input string. 
Don't worry about edge cases like a punctuation being 
attached to the word dog, but do account for capitalization.
"""

def checkDog(string):
    return 'dog' in string.lower()

print(checkDog("Is there a dog here?"))

"""
Create a function that counts the number of times 
the word "dog" occurs in a string. Again ignore edge cases.
"""

def countDog(string):
    count = 0
    for word in string.lower().split():
        if word == "dog":
            count += 1
    return count
print(countDog("This dog runs faster than the other dog."))

"""
Use lambda expressions and the filter() function to 
filter out words from a list that don't start with the letter 's'. 
For example:
seq = ['soup','dog','salad','cat','great']
"""

seq = ['soup','dog','salad','cat','great']
result = list(filter(lambda x: x[0] == "s",seq))
print(result)

"""
You are driving a little too fast, and a police officer stops you. 
Write a function to return one of 3 possible results: 
"No ticket", "Small ticket", or "Big Ticket". 
If your speed is 60 or less, the result is "No Ticket". 
If speed is between 61 and 80 inclusive, the result is "Small Ticket". 
If speed is 81 or more, the result is "Big Ticket". 
Unless it is your birthday (encoded as a boolean value in the 
parameters of the function) -- on your birthday, your speed can 
be 5 higher in all cases. 
"""

def caughtSpeeding(speed,isbirthday=False):
    if isbirthday: speed -= 5
    if speed <= 60:
        return "No Ticket"
    elif 61 <= speed <= 80:
        return "Small Ticket"
    else:
        return "Big Ticket"
print(caughtSpeeding(81))
