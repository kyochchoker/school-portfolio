age = int(input("What is your age?"))
                
if age >= 18:
    citizen = input("Are you a Citizen? (Y or N)")
    if citizen == "Y": 
      print ("You can vote!")
    else:
        print ("You are not a Citzen, You cannot vote.")
        
else:
    print ("You are not eligible to vote.")
