while True:
    username = input("USERNAME: ")
    while username == "":
        username = input("PLEASE PUT A USERNAME: ")
        continue
    password = input("PASSWORD: ")
    while password == "":
        password = input("PLEASE PUT A PASSWORD: ")
        continue

    if username == "bryan" and password == "louis":
        print("ACCESS GRANTED.")
        break
    else: 
        print("ACCESS DENIED, TRY AGAIN")
        continue

