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
