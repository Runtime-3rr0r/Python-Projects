while True:
    ans = input("Enter number: ")
    try: 
        if int(ans)>90:print("Number is greater than 90");break
        else:print("Number is less than 90");break
    except ValueError:print("Invalid number")