lin = int(input(""))
col = int(input(""))
ent_char = input("")
result=""
char = ""
flag = False

for x in range(0,lin):
    if flag !=True:
        for y in range(0,col):
            result +="*"
            char+=ent_char
            flag = True
    print(result)

for y in range(0,lin):
    print(char)
