from evaluator import find_reasons
from colorama import init, Fore, Style
init(autoreset=True)

if __name__ == "__main__":

    while True:
        print("\n***Welcome to MPIN Checker***\n")
        print("This tool is designed to check the validity of a given MPIN.")
        
        print("\n***Please follow these rules when entering the dates***\n")
        print("\n\t1.Enter the respective dates seperated by spaces (or any other character like '-' or '_' or '/')")
        print("\n\t2.Each date should be in the format DD/MM/YYYY or MM/DD/YYYY or YYYY/MM/DD")

        if input("\n\nDo you want to continue? (Y/N): ").lower() == "n":
            exit()

        print("\nPlease provide the following details: \n")
        mpin = input("Enter the MPIN: ")
        dob_self = input("Enter Date of Birth of Self: ")
        dob_spouse = input("Enter Date of Birth of Spouse: ")
        anniversary = input("Enter Anniversary Date: ")

        reasons = find_reasons(mpin, dob_self, dob_spouse, anniversary)

        if "INVALID_DATE" in reasons:
            print("Reasons Found: \n", reasons)
            print("Invalid Date Entered... \n Please Try Again...")
        
        elif len(reasons) == 0:
            print(Fore.GREEN+"Your MPIN is considered STRONG")
            print("Reasons Found: \n", reasons)

        elif len(reasons) <=2:
            print(Fore.YELLOW+"Your MPIN is considered WEAK ")
            print("Reasons Found: \n", reasons)

        else:
            print(Fore.RED+"Your MPIN is considered so WEAK ")
            print("Reasons Found: \n", reasons)

        Style.RESET_ALL

        if input("\n\nDo you want to continue with another MPIN? (Y/N): \n\n").lower() == "n":
            break