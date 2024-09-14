import os, subprocess

inp = input("Введите хост: ")
print(subprocess.check_call(["whois", inp]))