class Memory:
    def __init__(self):
        self.memory_value = None

    def save_to_memory(self, value):
        self.memory_value = value
        print(f"Значення {value} збережено в пам'ять.")

    def recall_memory(self):
        if self.memory_value is not None:
            print(f"Значення в пам'яті: {self.memory_value}")
        else:
            print("Пам'ять порожня.")

    def clear_memory(self):
        self.memory_value = None
        print("Пам'ять очищено.")
