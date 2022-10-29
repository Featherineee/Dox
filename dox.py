from colorama import Fore
import time

print(f"""{Fore.MAGENTA}      
███████╗███████╗░█████╗░████████╗██╗░░██╗███████╗██████╗░██╗███╗░░██╗███████╗
██╔════╝██╔════╝██╔══██╗╚══██╔══╝██║░░██║██╔════╝██╔══██╗██║████╗░██║██╔════╝
█████╗░░█████╗░░███████║░░░██║░░░███████║█████╗░░██████╔╝██║██╔██╗██║█████╗░░
██╔══╝░░██╔══╝░░██╔══██║░░░██║░░░██╔══██║██╔══╝░░██╔══██╗██║██║╚████║██╔══╝░░
██║░░░░░███████╗██║░░██║░░░██║░░░██║░░██║███████╗██║░░██║██║██║░╚███║███████╗
╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝
        """)
print(f'''{Fore.RED}
Made By featherine#3810 
Github : https://github.com/Featherineee
''')
time.sleep(1)

def Dox():
  target = input(f"{Fore.GREEN}[+]{Fore.RESET} Type Username Of Target : ")
  firstName = input(
    f"{Fore.GREEN}[+]{Fore.RESET} Type First Name Of Target : ")
  lastName = input(f"{Fore.GREEN}[+]{Fore.RESET} Type Last Name Of Target : ")
  age = int(input(f"{Fore.GREEN}[+]{Fore.RESET} Type Age Of Target : "))
  if age >= 70:
    print(f"{Fore.RED}[-]{Fore.RESET} You Have Choosed Too Old For Dox :((")
    exit()
  elif age < 9:
    print(f"{Fore.RED}[-]{Fore.RESET} Bro Thats Kid :Dd")
    exit()
  ip = input(f"{Fore.GREEN}[+]{Fore.RESET} Type IP Of Target : ")
  facebook = input(f"{Fore.GREEN}[+]{Fore.RESET} Type Targets Facebook Url : ")
  instagram = input(f"{Fore.GREEN}[+]{Fore.RESET} Type Targets Instagram Url : ")
  dad = input(f"{Fore.GREEN}[+]{Fore.RESET} Type Targets Dads Full Name : ")
  mom = input(f"{Fore.GREEN}[+]{Fore.RESET} Type Targets Moms Full Name : ")
  siblings = input(f"{Fore.GREEN}[+]{Fore.RESET} Type Siblings Full Name : ")
  phoneNumber = input(f"{Fore.GREEN}[+]{Fore.RESET} Type Targets Phone Number : ")
  fucked = input(f'{Fore.GREEN}[+]{Fore.RESET} Fucked By? : ')
  file = open(f'{target}.txt', 'a')
  file.write(f'''
  [+] Username : {target}
  [+] Firstname : {firstName}
  [+] Lastname : {lastName}
  [+] Age : {age}
  [+] Ip : {ip}
  [+] Facebook : {facebook}
  [+] Instagram : {instagram}
  [+] Dad : {dad}
  [+] Mom : {mom}
  [+] Sibling : {siblings}
  [+] Phone Number : {phoneNumber}

  [+] Fucked By : {fucked}
  [+] Dox By : https://github.com/Featherineee
  ''')
  print(f'{Fore.GREEN}[+]{Fore.RESET} Dox Has Been Created, ' + target)
  time.sleep(2)
  exit()


if __name__ == "__main__":
  Dox()
