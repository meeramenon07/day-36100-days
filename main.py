nameList = []
def printList():
  print()
  for fullName in nameList:
    print(fullName)
  print()
while True:
  firstName = input("your first name:  ").strip().capitalize()
  lastName = input("your last name:  ").strip().capitalize()
  fullName = f"{firstName} {lastName}"
  if fullName not in nameList:
    nameList.append(fullName)
  else:
    print("Duplicates are not allowed!")
  printList()


  




  