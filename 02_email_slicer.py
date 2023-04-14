def main():
    print("Welcome to the email slicer")
    print("")

    email_input=input("Input your email address:")
    (username,domain)=email_input.split("@")
    (domain,extension)=domain.split(".")
    print("username:",username,sep="")
    print("Domain:",domain,sep="")
    print("extension:",extension,sep="")
while(True):
    main()