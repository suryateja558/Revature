import re

x= "the train in the spain"
y=re.search("^the .*spain$",x)
if y:
    print("yes")
else:
    print("no")
    #regular expression

x= "the train in the spain"
d=re.findall("ai",x)
print(d)

pattern=r"\d+"
text="there are 123 apples"
match=re.search(pattern,text)


