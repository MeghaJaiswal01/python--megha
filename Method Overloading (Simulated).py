class Printer:
    def print_msg(self, message,times=3):
        for i in range(times):
            print(message)



if __name__ == "__main__":
    e = Printer()

    e.print_msg('Hello')