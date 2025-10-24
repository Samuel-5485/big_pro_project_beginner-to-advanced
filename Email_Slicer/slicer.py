#Collect email from the user
#split the email using the @. the first part as the user name, the second part is gonna be saved as domain
#split domain using ...
#hellosamicoder.com

def main():
    print("Hey, welcome to the email slicer!")
    print("")

    email_input = input("input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extenstion) = domain.split(".")

    print("UserName: ", username)
    print("Domain: ", domain)
    print("Extension: ", extenstion)
while True:
    main()
