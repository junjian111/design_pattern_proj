from abc import ABC, abstractmethod
from code_visualization import *

class VisualizationFactory(ABC):
    @abstractmethod
    def create_visualization(self):
        pass

class TreeFactory(VisualizationFactory):
    def create_visualization(self):
        return TreeVisualization()

class RectangleFactory(VisualizationFactory):
    def create_visualization(self):
        return RectangleVisualization()
