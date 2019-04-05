# this app randomly generate passwords according to chosen option
# password can be generated letters only, numbers only or numbers + letters shape
# the app also provides user with the option to generate passwords only from symbols chosen by the user


import random
import string


class Generator:

    def __init__(self, num, count):
        self.set_num_count(num, count)

    def set_num_count(self, num, count):
        if (num <= 0) or (count <= 0):
            raise ValueError("None of the numbers can not be 0 or negative !")
        self.num = num
        self.count = count

    def gener_number(self):
        passw_count = []
        i = 1
        while i <= self.count:
            var = "".join(random.choices(string.digits, k=self.num))
            passw_count.append(var)
            i = i + 1
        return passw_count

    def gener_letters(self):
        passw_count = []
        i = 1
        while i <= self.count:
            var = "".join(random.choices(string.ascii_letters, k=self.num))
            passw_count.append(var)
            i = i + 1
        return passw_count

    def gener_letters_numbers(self):
        passw_count = []
        i = 1
        while i <= self.count:
            var = "".join(random.choices(
                string.ascii_letters+string.digits, k=self.num))
            passw_count.append(var)
            i = i + 1
        return passw_count

    def gener_custom(self, symbols):
        passw_count = []
        i = 1
        while i <= self.count:
            var = "".join(random.choices(symbols, k=self.num))
            passw_count.append(var)
            i = i + 1
        return passw_count


while True:
    try:
        print("Welcome in the random passwords generator \nInput number 1 to calculate password cotaining just numbers\nInput number 2 to calculate password cotaining just letters\nInput number 3 to calculate password cotaining numbers and letters\nInput number 4 to calculate password cotaining customized amount of symbols")
        choice = int(input("Input the choice:"))

        if choice == 1:
            num = int(
                input("Input the number of symbols the passwords should contain:"))
            count = int(input("Input how many passwords should be generated:"))
            var_init = Generator(num, count)
            results = var_init.gener_number()
            for item in results:
                print(item)
            printout = input(
                "Do you want to export the result into txt file ? (y/n) ")
            if printout == "y":
                f = open("passwords.txt", "w")
                for item in results:
                    f.write(item)
                    f.write("\n")
                f.close()
                print("The result has been exported in passwords.txt file !")
            else:
                print("The result was not exported !")

            repeat = input("Do you want to repeat ? (y/n)")

        elif choice == 2:
            num = int(
                input("Input the number of symbols the passwords should contain:"))
            count = int(input("Input how many passwords should be generated:"))
            var_init = Generator(num, count)
            results = var_init.gener_letters()
            for item in results:
                print(item)
            printout = input(
                "Do you want to export the result into txt file ? (y/n) ")
            if printout == "y":
                f = open("passwords.txt", "w")
                for item in results:
                    f.write(item)
                    f.write("\n")
                f.close()
                print("The result has been exported in passwords.txt file !")
            else:
                print("The result was not exported !")

            repeat = input("Do you want to repeat ? (y/n)")

        elif choice == 3:
            num = int(
                input("Input the number of symbols the passwords should contain:"))
            count = int(input("Input how many passwords should be generated:"))
            var_init = Generator(num, count)
            results = var_init.gener_letters_numbers()
            for item in results:
                print(item)
            printout = input(
                "Do you want to export the result into txt file ? (y/n) ")
            if printout == "y":
                f = open("passwords.txt", "w")
                for item in results:
                    f.write(item)
                    f.write("\n")
                f.close()
                print("The result has been exported in passwords.txt file !")
            else:
                print("The result was not exported !")

            repeat = input("Do you want to repeat ? (y/n)")

        elif choice == 4:
            symbols = input(
                "Input the symbols that the passwords should contain: ")
            symbols = symbols.replace(" ", "")
            num = len(symbols)
            count = int(
                input("Input how many passwords should be generated: "))
            var_init = Generator(num, count)
            results = var_init.gener_custom(symbols)
            for item in results:
                print(item)
            printout = input(
                "Do you want to export the result into txt file ? (y/n) ")
            if printout == "y":
                f = open("passwords.txt", "w")
                for item in results:
                    f.write(item)
                    f.write("\n")
                f.close()
                print("The result has been exported in passwords.txt file !")
            else:
                print("The result was not exported !")

            repeat = input("Do you want to repeat ? (y/n)")

    except:
        pass

    else:
        if repeat.lower() != "y":
            print("You have finished the app !")
            break
