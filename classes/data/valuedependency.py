'''
valuedependency.py
'''
class ValueDependency:



    def __init__(self, value, dependency_tuple):
        self.value = value
        self.dependency_tuple = dependency_tuple



    def __eq__(self, value_dependency):
        return self.value == value_dependency.value and self.dependency_tuple == value_dependency.dependency_tuple
    


    def __hash__(self):
        return hash(self.value) + hash(self.dependency_tuple)
