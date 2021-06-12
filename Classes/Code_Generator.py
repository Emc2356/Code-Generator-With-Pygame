import random


class Code_Generator:
    def __init__(self):
        self.password = ""
        self.amount = 0
        self.A = 65
        self.chars_up = [x + self.A for x in range(26)]
        self.a = 97
        self.chars_low = [x + self.a for x in range(26)]
        self.zero = 48
        self.nums = [x + self.zero for x in range(9)]
        self.special_char = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59,
                             60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96, 123, 124, 125, 126, 127
                             ]
        self.char_up = False
        self.char_down = False
        self.char_num = False
        self.char_spec = False

    def get_amount(self):
        try:
            to_convert = input("how many characters would you like: ")
            self.amount = round(float(to_convert))
        except ValueError:
            print(f"""'{to_convert}' is not a valid number""")
            self.get_amount()
        except Exception as e:
            print(f"""error: {e} \ntype{type(e)}""")

    def ask_types(self):
        """
        checks with the user what type of chars he wants in his code
        :return: None
        """
        try:
            print("answer the following questions with n/y:")
            char_up = input("would you like upper letters?: ").lower()
            if char_up == "y":
                self.char_up = True
            elif char_up == "n":
                self.char_up = True
            else:
                self.char_up = False
                print(f"""'{char_up}' isint y/n and the value has been set to false \n if you want this to be true rerun the program""")

            char_down = input("would you like lower letters?: ").lower()
            if char_down == "y":
                self.char_down = True
            elif char_down == "n":
                self.char_down = True
            else:
                self.char_down = False
                print(
                    f"""'{char_down}' isint y/n and the value has been set to false \n if you want this to be true rerun the program""")

            nums = input("would you like numbers? ").lower()
            if nums == "y":
                self.char_num = True
            elif char_up == "n":
                self.char_num = True
            else:
                self.char_num = False
                print(
                    f"""'{nums}' isint y/n and the value has been set to false \n if you want this to be true rerun the program""")

            special_chr = input("would you like special characters?: ").lower()
            if special_chr == "y":
                self.char_spec = True
            elif special_chr == "n":
                self.char_spec = True
            else:
                self.char_spec = False
                print(
                    f"""'{special_chr}' isint y/n and the value has been set to false \n if you want this to be true rerun the program""")

            if not self.char_up and not self.char_down and not self.char_num and not self.char_spec:
                print("you haven't selected anything, the program exits automatically")
                quit(-1)

        except Exception as e:
            print(f"""error: {e} \ntype{type(e)}""")

    def get_code(self):

        to_chose = []
        if self.char_up:
            to_chose += self.chars_up
        if self.char_down:
            to_chose += self.chars_low
        if self.char_num:
            to_chose += self.nums
        if self.char_spec:
            to_chose += self.special_char

        self.password = ""
        if not to_chose:
            self.password = ""
            return None
        for i in range(self.amount):
            self.password += chr(random.choice(to_chose))
