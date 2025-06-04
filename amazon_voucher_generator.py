import random
reed1 = []
reed2 = []
reed3 = []
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',0,1,2,3,4,5,6,7,8,9]
while len(reed1) != 4:
    code = random.choice(alpha)
    reed1.append(code)
generated_code1 = "".join(map(str, reed1))


while len(reed2) != 6:
    code = random.choice(alpha)
    reed2.append(code)
generated_code2 = "".join(map(str, reed2))


while len(reed3) != 4:
    code = random.choice(alpha)
    reed3.append(code)
generated_code3 = "".join(map(str, reed3))

print(f"{generated_code1}-{generated_code2}-{generated_code3}")