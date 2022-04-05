from behaviors import display_behavior, fly_behavior, quack_behavior


class Duck:

    def __init__(self, db, fb, qb):
        self.db = db
        self.fb = fb
        self.qb = qb

    def fly(self):
        self.fb.fly()

    def quack(self):
        self.qb.quack()

    def display(self):
        self.db.display()



duck = Duck(
    db=display_behavior.VideoDisplay(),
    fb=fly_behavior.UpDownFly(),
    qb=quack_behavior.LoudQuack()
)


duck.display()
duck.fly()
duck.quack()
