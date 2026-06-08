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
            print("Then I type 'git  remote add origin https://github.com/anshul-327/Push_testing.git' to see link the directory and github repository.")
            print("Then I add the files by typing 'git add .'")
            print("Then I save a snapshot of my work by typing 'git commit -m 'Added both the python files to the repository and this is the first commit'")
            print("Finally, I type 'git push -u origin master' (first I used main but there was an error so I run git branch and saw it is master and not main) to upload everything so you can see it!")
        elif reply.lower() == "no":
            secret()
            # if you wnat to know what secret() does, just type no. Btw, it is my first time using a custom function that too imported!!!!
    else:
        print("That is not a vaild response")

        # I also did a second commit so in the explaination there is only first commit
