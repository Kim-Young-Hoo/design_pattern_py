class Duck:

    def __init__(self):
        pass

    def fly(self):
        print("fly!!!!")

    def quack(self):
        print("quack!!!!")

    def display(self):
        print("display!!!!")


class UpDownDuck(Duck):
    # 위아래로 날아다니는 오리
    def fly(self):
        print("fly up and down!")


class RoundDuck(Duck):
    # 빙글빙글 날아다니는 오리
    def fly(self):
        print("fly round round round!")


class LoudAndUpDownDuck(Duck):
    # 위아래로 날아다니면서 시끄럽게 우는 오리
    def fly(self):
        print("fly up and down!")

    def quack(self):
        print("Fucking Loud!!!!!!!!")


class QuietAndUpDownDuck(Duck):
    # 위아래로 날아다니면서 시끄럽게 우는 오리
    def fly(self):
        print("fly up and down!")

    def quack(self):
        print("quiet")
