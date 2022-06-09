# LAB 1 : Threading - Bank accounts
"""
At a bank, we have to keep track of the balance of some accounts. Also, each account has an associated log
(the list of records of operations performed on that account).
Each operation record shall have a unique serial number, that is incremented for each operation performed in the bank.
We have concurrently run transfer operations, to be executed on multiple threads.
Each operation transfers a given amount of money from one account to some other account,
and also appends the information about the transfer to the logs of both accounts.

From time to time, as well as at the end of the program, a consistency check shall be executed.
It shall verify that the amount of money in each account corresponds with the operations records
associated to that account, and also that all operations on each account appear
also in the logs of the source or destination of the transfer.

Operations:
- transfer (- one account, + the other account)
- consistency check : in the main thread, function that: (each 60s)
                    - checks the amount of money with the history of operations from the start
                    - check each operation to appear in the history of source/dest
"""
import time
from threading import Lock
import threading
import random

operation_id = 0
operation_mutex = Lock()
no_of_threads = 10
bank_accounts = []
max_runtime = 420


class BankAccount:
    def __init__(self, iban, balance, log_file):
        self.__iban = iban
        self.__start_balance = balance
        self.__balance = balance
        self.__log_file = log_file
        self.__mutex = Lock()
        self.__log_mutex = Lock()

    def get_iban(self):
        return self.__iban

    def receive_money(self, op_id, amount, sender):
        self.__mutex.acquire()
        self.__balance += amount
        self.__mutex.release()

        self.__log_mutex.acquire()
        self.log_transfer(op_id,"receive",amount,sender)
        self.__log_mutex.release()
        # provide with mutex lock and log the transfer with the sender

    def send_money(self, amount, dest):
        self.__mutex.acquire()
        if amount > self.__balance:
            self.__mutex.release()
            raise Exception(self.__str__() + " - insufficient founds")
        self.__balance -= amount
        self.__mutex.release()

        operation_mutex.acquire()
        global operation_id
        operation_id += 1  # this should also be locked
        new_op_id = operation_id
        operation_mutex.release()

        self.__log_mutex.acquire()

        self.log_transfer(new_op_id,"send",amount,dest)
        self.__log_mutex.release()

        return new_op_id
        # provide with mutex lock and log the transfer with the dest

    def log_transfer(self, op_id, transfer_type, amount, sender_or_dest):
        with open(self.__log_file, "a+") as log:
            print("\nLogging: in file " + self.__iban + " transfer from/to " + sender_or_dest)
            log.write("ID" + str(op_id) + "-" + transfer_type + "-" + str(amount) + "-" + sender_or_dest + "\n")

    def consistency_check(self):
        self.__mutex.acquire()
        self.__log_mutex.acquire()
        log_computed_balance = self.__start_balance
        with open(self.__log_file,"r") as log:
            lines = log.readlines()
            for line in lines:
                tokens = line.split("-")
                op_id = tokens[0]
                found = False
                second_account_file = tokens[3][:-1] + ".log"
                with open(second_account_file,"r") as log2:
                    lines2 = log2.readlines()
                    for l2 in lines2:
                        if l2.split("-")[0] == op_id:
                            found = True
                            break
                if not found:
                    break
                if tokens[1] == "receive":
                    log_computed_balance += int(tokens[2])
                elif tokens[1] == "send":
                    log_computed_balance -= int(tokens[2])
        if log_computed_balance == self.__balance and found:
            print(self.__str__(),"consistency check passed.")
        else:
            print(self.__str__(),"consistency check FAILED: "
                                 "found ->",found,
                                 ", log balance ->", log_computed_balance,
                                 ", balance ->", self.__balance)
        self.__log_mutex.release()
        self.__mutex.release()

    def __str__(self):
        return "Account " + self.__iban


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    global bank_accounts
    for ba in bank_accounts:
        print(ba)


def thread_function(idx):
    while True:
        if operation_id >= 1111:
            break

        account1 = random.choice(bank_accounts)
        account2 = random.choice([ba for ba in bank_accounts if ba.get_iban() != account1.get_iban()])
        amount = random.randint(1,420)
        print("\nThread " + str(idx) + " working: " + str(account1) + " transfer to " + str(account2))
        try:
            new_op_id = account1.send_money(amount, account2.get_iban())
            account2.receive_money(new_op_id, amount, account1.get_iban())
        except Exception as e:
            print(e)

        if operation_id >= 1111 or time.time() - start_time >= max_runtime:
            break
        time.sleep(2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a1 = BankAccount("IBAN1",42000420,"IBAN1.log")
    a2 = BankAccount("IBAN2",42200420,"IBAN2.log")
    a3 = BankAccount("IBAN3",12220420,"IBAN3.log")
    a4 = BankAccount("IBAN4",22220420,"IBAN4.log")
    a5 = BankAccount("IBAN5",44444420,"IBAN5.log")
    bank_accounts = [a1,a2,a3,a4,a5]
    threads = []
    print_hi('Main thread')
    start_time = time.time()
    for index in range(no_of_threads):
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    consistency_check_time = time.time()
    while True:
        if time.time() - consistency_check_time >= 10:
            for a in bank_accounts:
                a.consistency_check()
            consistency_check_time = time.time()

        if operation_id >= 1111 or time.time() - start_time >= max_runtime:
            for x in threads:
                x.join()
            break

    for a in bank_accounts:
        a.consistency_check()

    print(f"\n{no_of_threads} threads done:\n{operation_id} operations in {'{:.2f}'.format(time.time()-start_time)} s")
