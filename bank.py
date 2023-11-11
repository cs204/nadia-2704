TextS = input("Приветствие: ")
if TextS.lower().startswith("здравствуйте"):
   print("$0")
elif TextS.lower().startswith("з"):
   print("$20")
else:
   print("$100")