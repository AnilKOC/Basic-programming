import os
cwd=os.getcwd()
while True:
    command= input(cwd+" [+]")
    if command == "cd":
        parameter=input("[+] Enter the path :")
        cwd=parameter
        os.chdir(parameter)
    elif command == "list":
        for i in os.listdir():
            print(i)
        '''
        for subdir, dirs, files in os.walk('./.'):
            for file in files:
                print (file)
        '''
    elif command == "getcwd":
        print(cwd)
    elif command == "create-folder":
        parameter = input("[+] Enter the folder name :")
        try:
            os.mkdir(parameter)
            print("[<>] Directory ", parameter, " created.")
        except FileExistsError:
            print("[!!]Directory ", parameter, " already exists.")
    elif command =="change-name-folder":
        parameter = input("[+] Enter the folder name :")
        parameter2 = input("[+] Enter the new name :")
        os.rename(parameter,parameter2)
    elif command =="delete":
        parameter = input("[+] Enter name :")
        parameter = cwd+"\\"+parameter+"\\"
        os.remove(parameter)
    elif command == "text":
        parameter = input("[+] Enter text name :")
        text_file = open(parameter+".txt","w")
        parameter2 = input("[<>] Enter your text :")
        text_file.write(parameter2)
    else:
        print("[-] This command does'nt exist.")
