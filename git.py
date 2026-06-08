from helper import secret

name = input("Enter your name")
print("Hello", name)

reply=""

while reply.lower() != "yes" and reply.lower() != "no":
    reply = input("Do you want to know what I did to share this to you. If yes type 'yes', if no type 'no'.")
    if type(reply) == str:
        if reply.lower() == "yes":
            print("Good")
            print("First, I open the terminal and do into the directory of this file.")
            print("Then I type 'git init' to initialize the repository and like it to the repository in github.")
            print("Then I set my branch to main by typing 'git branch -M main'")
            print("Then I add the files by typing 'git add .'")
            print("Then I save a snapshot of my work by typing 'git commit -m First commit'(because it is first commit).")
            print("Then I link it to the cloud using 'git remote add origin '")
            print("Finally, I type 'git push -u origin main' to upload everything so you can see it!")
        elif reply.lower() == "no":
            secret()
            # if you wnat to know what secret() does, just type no. Btw, it is my first time using a custom function that too imported!!!!
    else:
        print("That is not a vaild response")
