class Helper:
    def __init__(self, work):
        self.work = work
    def __call__(self, work):
        return f"Спочатку ми вирушимо до {self.work} , а потім поїдем до {work}"
helper = Helper("Карпат")
print(helper("Львова"))