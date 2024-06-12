from builder import *
from visualization_factory import *

class FunnyJsonExplorer:
    def __init__(self, builder):
        self.builder = builder

    def load(self, data):
        self.builder.build_product(data)

    def show(self):
        result = self.builder.get_product()
        self.builder.draw(result)

def main():
    import json
    import argparse
    from icon_family_config import icon_families
    parser = argparse.ArgumentParser(description='Funny JSON Explorer')
    parser.add_argument('-f', '--file', help='<json file>')
    parser.add_argument('-s', '--style', help='<style>')
    parser.add_argument('-i', '--icon_family', help='<icon family>')
    args = parser.parse_args()

    if args.style == 'tree':
        factory = TreeVisualizationFactory(args.icon_family)
    elif args.style == 'rectangle':
        factory = RectangleVisualizationFactory(args.icon_family)
    else:
        raise ValueError('Invalid style')

    builder = JsonBuilder(factory)
    explorer = FunnyJsonExplorer(builder)

    with open(args.file, 'r') as f:
        data = json.load(f)

    explorer.load(data)
    explorer.show()

if __name__ == '__main__':
    main()
