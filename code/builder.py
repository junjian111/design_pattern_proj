class Builder:
    def __init__(self, factory):
        self.factory = factory
        self.output = []

    def build_product(self):
        pass

    def get_product(self):
        pass

    def draw(self):
        pass

class JsonBuilder(Builder):
    def __init__(self, factory):
        super().__init__(factory)
        self.output = []

    def build_product(self, data):
        self.visualization = self.factory.create_visualization()
        self.visualization.create_conversion(data)
        self.visualization.rebuild_output()
        self.output = self.visualization.output

    def get_product(self):
        return self.output

    def draw(self, result):
        for line in result:
            print(line)
