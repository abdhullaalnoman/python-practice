# a = int(input("Enter number 1")) 
# b = int(input("Enter number 2")) 
# c = int(input("Enter number 3")) 
# d = int(input("Enter number 4")) 
# if(a>b and a>c and a>d):
#     print(f"${a} is bigger.")
# elif(b>a and b>c and b>d):
#     print(f"${b} is bigger.")
# elif(c>a and c>b and c>d):
#     print(f"${c} is bigger.")
# else:
#     print(f"${d} is bigger.")



# a = int(input("Enter mark 1")) 
# b = int(input("Enter mark 2")) 
# c = int(input("Enter mark 3"))  
# mark = ((a+b+c)/300)*100
# if(mark>=40 and a>=40 and b>=40 and c>=40):
#     print("You Are Passed.your Percentage is :",mark)
# else:
#     print("You are Failed.your Percentage is :",mark)


# a = "Make a lot of money"
# b = "buy now"
# c = "subscribe this"
# d = "click this"

# mesg = input("Enter a message")

# if((a in mesg) or (b in mesg) or (c in mesg) or (d in mesg)):
#     print("The Message is a spam.")
# else:
#     print("The Message is not a spam.")


# username = "nomandfhfgdfg"
# if(len(username)>10):
#     print("This Username Contain more than 10 word")
# else:
#     print("This Username not Contain more than 10 word")

# names = ["Noman", "sumu", "Nipa", "sohag"]
# name = input("Enter the name")
# if(name in names):
#     print("yes,Name is here")
# else:
#     print("not,Name is not here")

# mark = int(input("Enter your mark"))
# if(mark>=90 and mark<=100):
#     print("Ex")
# elif(mark>=80 and mark<90):
#     print("A")
# elif(mark>=70 and mark<80):
#     print("B")
# elif(mark>=60 and mark<70):
#     print("C")
# elif(mark>=50 and mark<60):
#     print("D")
# elif(mark<50):
#     print("F")
# else:
#     print("Enter a valid mark")

post  = input("Enter a Post: ")    

if("Noman".lower() in post.lower()):
    print("Noman in the post")
else:
    print("Noman not in the post")
