email = input("enter your email address:----")
print(email)
j, k, a = 0, 0, 0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-3] == ".") ^ (email[-4] == "."):
                for i in email:
                    if i == i.isspace():
                        j = 1
                    elif i.isalpha():
                        if i == i.upper():
                            k = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        a = 1
                if j == 1 or k == 1 or a == 1:
                    print("wrong email address (5)")
                else:
                    print("right email")
            else:
                print("wrong email address (4)")
        else:
            print("wrong email address (3)")
    else:
        print("wrong email address (2)")
else:
    print("wrong email address (1)")
