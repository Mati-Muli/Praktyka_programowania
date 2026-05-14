class House:
    def __init__(self):
        self.components = []
    def show(self):
        print(self.components)
class Builder:
    def __init__(self):
        self.house= House()
    def BuildWall(self):
        self.house.components.append("Wall")
        return self
    def BuildCelling(self):
        self.house.components.append("Celling")
        return self
    def BuildWindows(self):
        self.house.components.append("Windows")
        return self
    def build(self):
        return self.house
if __name__ == '__main__':

    builder = Builder()
    dom = (builder
            .BuildWall()
           .BuildCelling()
           .BuildWindows()
           .build())
    dom.show()

