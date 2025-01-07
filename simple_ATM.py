
def check_pass(passwd):
    with open("pass.txt", "r+") as pass1:
        get_pass = pass1.read()
    if len(passwd) < 6:
        print("Must be 6 Characters, Try Again")
        return False
    elif passwd != get_pass:
        print("Invalid password, please try again")
        return False
    else:
        return True

def change_pass(new_pass):
    with open("pass.txt", "w") as n_pass:
        if len(new_pass) < 6:
            print("Must be at least 6")
        else:
            n_pass.write(new_pass)
            print("Successfully Changed!")

def check_balance():
    with open("balance.txt", "r") as ch_bl:
        ch_balance = int(ch_bl.read())
    print(f"Your current balance is {ch_balance}")


def deposit(amount):
    with open("balance.txt", "r+") as dep_bl:
        old_balance = int(dep_bl.read())
        new_balance = old_balance + amount
        dep_bl.seek(0)
        dep_bl.write(str(new_balance))
        dep_bl.truncate()
    return new_balance


def withdrawal(amount):
    with open("balance.txt", "r+") as wd_bl:
        old_balance = int(wd_bl.read())

    if amount > old_balance:
        print("Insufficient funds!")
        return old_balance
    else:
        new_balance = old_balance - amount
        with open("balance.txt", "w") as wd_bl:
            wd_bl.write(str(new_balance))
        return new_balance


def main():
    try:
        with open("balance.txt", "x") as f:
            f.write("0")
    except FileExistsError:
        pass

    limit = 3
    while limit:
        passwd = input("Enter your Password: ")
        if check_pass(passwd):
            ops = """
            Type the Related Process Number
            1- Check the balance.
            2- Deposit.
            3- Withdrawal.
            4- Change the Password.
            5- Quit.
            """
            print(ops)

            # processes = int(input("Enter the Desired Operation: "))
            try:
                processes = int(input("Enter the Desired Operation: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue
            if processes == 1:
                check_balance()
            elif processes == 2:
                dp_amount = int(input("Enter the amount to deposit: "))
                new_balance = deposit(dp_amount)
                print(f"Successfully deposited! New balance: {new_balance}")
            elif processes == 3:
                wd_amount = int(input("Enter the amount to withdraw: "))
                new_balance = withdrawal(wd_amount)
                print(f"The balance: {new_balance}")
            elif processes == 4:
                new_pass = input("Enter the New Password: ")
                change_pass(new_pass)
            elif processes == 5:
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid operation selected.")
        else:
            print(f"[*] Limit is 3 Tries - {limit-1} Tries Remaining")
            limit -= 1
    print("See you soon!")


if __name__ == "__main__":
    main()
