class Factory:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def _get_rank(self) -> str:
        print("This method got called...")
        if self.age > 30:
            return "Old"
        return "Young"

def main():
    fact1 = Factory("Kartik", 22)
    print(fact1._get_rank())

if __name__ == "__main__":
    main()
