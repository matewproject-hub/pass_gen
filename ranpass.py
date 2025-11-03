import random
import string
#import pyperclip
def generate_password(length):
    if length < 5:
        return "Password is too short"
    uc=string.ascii_uppercase
    lc=string.ascii_lowercase
    dig=string.digits
    sp=string.punctuation
    password=[random.choice(uc),random.choice(lc),
              random.choice(dig),random.choice(sp)]
    all_characters=uc+lc+dig+sp
    for _ in range(length-4):
        password.append(random.choice(all_characters))
    random.shuffle(password)
    return ''.join(password)
if __name__=="__main__":
    length=int(input("Enter your desired length\n"))
    print("Your desired password is:", generate_password(length))
    #pyperclip.copy(password)
    #print("Password copied to your clipboard")
