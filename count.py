s=input("Enter your text: ")

alpha=0
dig=0
sp=0

for i in s:
    if i.isalpha():
        alpha= alpha +1
    elif i.isdecimal():
        dig = dig + 1
    else:
        sp= sp + 1

print(f"The total count of Alphabet is {alpha}, digit {dig}, Special character {sp}")
