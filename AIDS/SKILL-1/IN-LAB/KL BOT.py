import random
print("Hello , I am advisor chat bot.")
name = input(" May I know your name? ")
print("Thank you! " + name)
print("I am here to explore you that core courses required for the specialization's offered in KL University.")
branch = input("You belonged to CSE yes (or) no ")
if 'yes' in branch:
    print("Oh ! that's a great choice ")
    print(" 1.AI\n", "2.DS\n", "3.CYS\n", "4.CLOUD COMPUTING")
    print("These are the top specializations in the present era.")
specialization = input("Enter your Interested specialization ")
if "AI" in specialization:
    print("These are the core courses present in this specialization\n", "1.AIDS\n", "2.PYTHON FULL STACK DEVELOPMENT\n", "3.PQRTS\n", "4.OOP'S FULL STACK")
elif "DS" in specialization:
    print("These are the core courses present in this specialization\n", "1.DBMS\n", "2.DIA\n", "3.PQRTS\n")
elif "CYS" in specialization:
    print("These are the core courses present in this specialization\n", "1.CEH\n", "2.COBIT\n", "3.CND\n", "4.CISSP\n",)
elif "CLOUD COMPUTING" in specialization:
    print("These are the core courses present in this specialization\n", "1.DBMS\n", "2.DIA\n", "3.PQRTS\n")
print("wish you a GOOD LUCK !")