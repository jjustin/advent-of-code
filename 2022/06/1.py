from input import input

l = 4
last4chars = ["-"] * l
for (i, char) in enumerate(input):
    if len(set(last4chars)) != l or "-" in last4chars:
        last4chars = last4chars[1:l] + [char]
    else:
        print(i)
        break
