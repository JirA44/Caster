class Caster:
    def __init__(self):
        self.dictionary = {}

    def add_entry(self, key: str, value: str):
        self.dictionary[key] = value

    def get_entry(self, key: str) -> str:
        return self.dictionary.get(key, "Entry not found")

if __name__ == "__main__":
    caster = Caster()
    caster.add_entry("hello", "Greeting to someone")
    print(caster.get_entry("hello"))