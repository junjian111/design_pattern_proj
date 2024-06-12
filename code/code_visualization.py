class DataVisualization:
    def __init__(self, icon_family, data=None):
        self.icon_family = icon_family
        self.data = data
        self.output = []

    def create_conversion(self, data, level=0, parent_last=[]):
        pass

    def rebuild_output(self):
        pass

class TreeVisualization(DataVisualization):
    def create_conversion(self, data, level=0, parent_last=[]):
        for i, (key, value) in enumerate(data.items()):
            is_last = i == len(data) - 1
            sign = (self.icon_family[0] if level == 0 else self.icon_family[1]) + " "
            prefix = ''.join('│  ' if not last else '   ' for last in parent_last)
            prefix += '└─' if is_last else "├─"
            self.add_node(key, value, is_last, sign, prefix, level, parent_last)

    def add_node(self, key, value, is_last, sign, prefix, level, parent_last):
        if isinstance(value, dict):
            self.add_branch_node(key, value, is_last, sign, prefix, level, parent_last)
        else:
            self.add_leaf_node(key, value, is_last, sign, prefix)

    def add_branch_node(self, key, value, is_last, sign, prefix, level, parent_last):
        final_str = prefix + sign + str(key)
        self.output.append(final_str)
        self.create_conversion(value, level + 2, parent_last + [is_last])

    def add_leaf_node(self, key, value, is_last, sign, prefix):
        final_str = prefix + sign + str(key) + ("" if value is None else (": " + str(value)))
        self.output.append(final_str)

    def rebuild_output(self):
        pass


class RectangleVisualization(DataVisualization):
    def create_conversion(self, data, level=0, parent_last=[]):
        for i, (key, value) in enumerate(data.items()):
            is_last = i == len(data) - 1
            sign = (self.icon_family[0] if level == 0 else self.icon_family[1]) + " "
            prefix = '│  ' * len(parent_last)
            
            if level == 0 and i == 0:
                prefix = '┌─'
            elif all(parent_last) and not isinstance(value, dict):
                prefix = "└─" + prefix[2:].replace(' ', '─')
            else:
                prefix = "├─" + prefix[2:]

            if isinstance(value, dict):
                final_str = prefix + sign + str(key)
                self.output.append(final_str)
                self.create_conversion(value, level + 2, parent_last + [is_last])
            else:
                final_str = prefix + sign + str(key) + ("" if value is None else (": " + str(value)))
                self.output.append(final_str)

    def rebuild_output(self):
        max_len = max(len(i) for i in self.output) + 10
        for i in range(len(self.output)):
            self.output[i] = self.output[i].ljust(max_len, '─')
            if i == 0:
                self.output[i] = self.output[i][:max_len - 1] + '┐'
            elif i == len(self.output) - 1:
                self.output[i] = self.output[i][:max_len - 1] + '┘'
            else:
                self.output[i] = self.output[i][:max_len - 1] + '│'

