#dictionaries words/definitions 
#dictionary in pyton is key and value 
words = {"apple":"bright red or green fruit", "orange":"a citrus fruit or a color."}
print(words["apple"])
print(words["orange"])
contacts = {} 
contacts["Mom"] = ["212-333-4444","mom@moms.net"]
print(contacts)
print(contacts["Mom"][1]) #mom's email 
contacts["Dad"] = ["609-788-9999","poppa@pops.com"]

print(contacts["Dad"][0])

contacts.update({"Sam":["212-333-0101","sam@gmail.com"]}) #add another entry 

contacts["Sally"] = ["718-989-9898","sals@yahoo.com"]

#NO order to the dictionary 
#print(contacts[-1]) does NOT work  
#print(contacts[0]) does NOT work 

print(contacts.keys()) 
contact_names = list(contacts.keys()) #convert all the keys into a list 
print(contact_names[0])

family = {}
family[0] = "Grandpa"
family[1] = "Mom"
print(family[0])
print(family)

contacts = {} #create dictionary 
contacts["Bob Saget"] = { "phone": "212-333-4444","email":"bob@bobs.com"}
contacts["Mom"] = {"email": "mom@yahoo.com","phone":"646-246-1234"}

print(contacts["Bob Saget"]["phone"])
print(contacts["Mom"]["email"])

contacts.pop("Bob Saget")
print(contacts)

contacts["Mom"]["email"] = "newmomemail@apple.com"

print(contacts)

def mult(a,b,c):
  return a*b*c

print(mult(3,4,5))

vals = {"a": 10, "b" : 1, "c": 3}


print(mult(**vals)) #210
