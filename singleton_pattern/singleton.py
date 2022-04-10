class Singleton:
    instance = None

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = Singleton()
        return cls.instance

    @staticmethod
    def some_method():
        print("hello world!")


if __name__ == "__main__":
    Singleton.get_instance().some_method()
    Singleton.get_instance().some_method()
    Singleton.get_instance().some_method()
    Singleton.get_instance().some_method()


