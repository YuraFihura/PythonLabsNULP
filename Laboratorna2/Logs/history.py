class History:
    def __init__(self):
        self.records = []

    def add_record(self, expression, result):
        self.records.append(f"{expression} = {result}")

    def show_history(self):
        if self.records:
            for record in self.records:
                print(record)
        else:
            print("Історія порожня.")

    def clear_history(self):
        self.records = []
        print("Історія очищена.")
