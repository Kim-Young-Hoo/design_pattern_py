from duck import Duck
from behaviors import display_behavior, fly_behavior, quack_behavior

if __name__ == "__main__":
    duck = Duck(
        db=display_behavior.VideoDisplay(),
        fb=fly_behavior.UpDownFly(),
        qb=quack_behavior.LoudQuack()
    )

    duck.display()
    duck.fly()
    duck.quack()
