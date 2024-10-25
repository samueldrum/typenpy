

class Vector:
    def __init__(self, data, filter=None):
        self.data_list = []
        self.result_list = []

        for elem in data:
            self.data_list.append(elem)
        
        self.data = self.data_list


    def __add__(self, other):
        if isinstance(other, (int, float)):
            for elem in self.data:
                self.result_list.append(elem + other)
        elif isinstance(other):
            for list1, list2 in zip(self.data, other):
                self.result_list.append(list1 + list2)
        elif isinstance(other, Vector):
            for vec1, vec2 in zip(self.data, other.data):
                self.result_list.append(vec1 + vec2)
        return self.result_list
    

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            for elem in self.data:
                self.result_list.append(elem - other)
        elif isinstance(other):
            for list1, list2 in zip(self.data, other):
                self.result_list.append(list1 - list2)
        elif isinstance(other, Vector):
            for vec1, vec2 in zip(self.data, other.data):
                self.result_list.append(vec1 - vec2)
        return self.result_list
    

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            for elem in self.data:
                self.result_list.append(elem * other)
        elif isinstance(other):
            for list1, list2 in zip(self.data, other):
                self.result_list.append(list1 * list2)
        elif isinstance(other, Vector):
            for vec1, vec2 in zip(self.data, other.data):
                self.result_list.append(vec1 * vec2)
        return self.result_list
    

    def __matmul__(self, other):
        if isinstance(other, (int, float)):
            for elem in self.data:
                self.result_list.append(elem * other)
        elif isinstance(other):
            for list1, list2 in zip(self.data, other):
                self.result_list.append(list1 * list2)
        elif isinstance(other, Vector):
            for vec1, vec2 in zip(self.data, other.data):
                self.result_list.append(vec1 * vec2)
        return self.result_list
    

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            for elem in self.data:
                self.result_list.append(elem / other)
        elif isinstance(other):
            for list1, list2 in zip(self.data, other):
                self.result_list.append(list1 / list2)
        elif isinstance(other, Vector):
            for vec1, vec2 in zip(self.data, other.data):
                self.result_list.append(vec1 / vec2)
        return self.result_list
    

    def __divemod__(self, other):
        if isinstance(other, (int, float)):
            for elem in self.data:
                self.result_list.append(elem // other)
        elif isinstance(other):
            for list1, list2 in zip(self.data, other):
                self.result_list.append(list1 // list2)
        elif isinstance(other, Vector):
            for vec1, vec2 in zip(self.data, other.data):
                self.result_list.append(vec1 // vec2)
        return self.result_list

    def __getitem__(self, index):
        return self.data[index]
    
    
    def __setitem__(self, index, value):
        value = self.dtype(value)
        self.data[index] = value


    def __iter__(self):
        return iter(self.data)
    

    def __len__(self):
        return len(self.data)


    def __repr__(self) -> str:
        return f"Vector({self.data})"