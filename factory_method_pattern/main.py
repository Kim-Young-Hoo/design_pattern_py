import chocolate_factories



if __name__ == "__main__":

    sweet_choco_factory = chocolate_factories.SweetChocolateFactory()
    bitter_choco_factory = chocolate_factories.BitterChocolateFactory()

    print("달달구리 초꼬릿 생산")
    print(sweet_choco_factory.produce_chocolate("DarkChocolate"))
    print(sweet_choco_factory.produce_chocolate("WhiteChocolate"))
    print("씁쓰리 초꾸리 생산")
    print(bitter_choco_factory.produce_chocolate("DarkChocolate"))
    print(bitter_choco_factory.produce_chocolate("WhiteChocolate"))
