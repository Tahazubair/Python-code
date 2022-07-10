Secret_Word = "Leader"
Guess = ""
Count = 0
limit = 3
Out_of_tries =  False
while Guess != Secret_Word and not(Out_of_tries):
    if Count < limit:
        Guess = input("Enter the word : ")
        Count += 1
    else:
        Out_of_tries = True
if Out_of_tries:
    print("You Lose!")
else:
    print("You Win!")