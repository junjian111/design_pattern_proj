from abstract_factory import *
from icon_family_config import icon_families

class TreeVisualizationFactory(TreeFactory):
    def __init__(self, icon_family):
        self.icon_family = icon_families[icon_family]

    def create_visualization(self):
        return TreeVisualization(self.icon_family)

class RectangleVisualizationFactory(RectangleFactory):
    def __init__(self, icon_family):
        self.icon_family = icon_families[icon_family]

    def create_visualization(self):
        return RectangleVisualization(self.icon_family)