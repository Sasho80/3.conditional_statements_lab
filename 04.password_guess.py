password_guest= input()
password_user = "s3cr3t!P@ssw0rd"

if password_user == password_guest:
    print("Welcome")
else:
    print("Wrong password!")
