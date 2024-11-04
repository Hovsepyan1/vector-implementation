import numpy as np

class Vector:
    def __init__(self):
        self.arr = np.array([], dtype="int")
        self.v_size = 0
        self.v_capacity = 0
    
    @property
    def v_size(self) -> int:
        return self.__v_size
    
    @v_size.setter
    def v_size(self, size: int):
        if not isinstance(size, int):
            raise TypeError("Invalid type.")
        self.__v_size = size

    @property
    def v_capacity(self) -> int:
        return self.__v_capacity
    
    @v_capacity.setter
    def v_capacity(self, capacity: int):
        if not isinstance(capacity, int):
            raise TypeError("Invalid type.")
        self.__v_capacity = capacity

    def __str__(self):
        return str(self.arr[:self.v_size])
    
    def __repr__(self):
        return f"Vector(arr = {self.arr}, size = {self.__v_size}, capacity = {self.__v_capacity})"

    def is_empty(self) -> bool:
        return not self.v_size
    
    def __resize(self):
        self.v_capacity = 2 if not self.v_capacity else self.v_capacity * 2
        self.arr = np.pad(self.arr, (0, self.v_capacity - self.v_size), 'constant', constant_values=0) #version 1
        # self.arr = np.concatenate((self.arr, [0 for i in range(new_capacity - self.v_size)])) #version 2
        
        # else: 
        #     self.arr = self.arr[:new_capacity]
        #     self.v_size = new_capacity
        #     self.v_capacity = new_capacity

    def push_back(self, element):
        if self.v_size == self.v_capacity: 
            self.__resize()
        self.arr[self.v_size] = element
        self.v_size += 1
            
    def pop_back(self):
        if self.is_empty():
            print("Vector is empty!")
            return
        self.v_size -= 1
        return self.arr[self.v_size + 1]
    
    def shrink_to_fit(self):
        if self.v_size == self.v_capacity:
            return
        self.arr.resize(self.v_size)
        # self.arr = self.arr[:self.v_size]
        self.v_capacity = self.v_size

    def at(self, index: int):
        if not isinstance(index, int):
            raise TypeError("Invalid type.")
        if index >= self.v_size or index < 0:
            raise IndexError("Invalid index.")
        return self.arr[index]
    
    def push_front(self, element):
        if self.v_size == self.v_capacity:
            self.__resize()
        for i in range(self.v_size, 0, -1):
            self.arr[i] = self.arr[i - 1]
        self.arr[0] = element
        self.v_size += 1
        print(self.arr)
        
    def pop_front(self):
        if self.is_empty():
            print("Vector is empty!")
            return 
        retval = self.arr[0]
        for i in range(self.v_size):
            self.arr[i] = self.arr[i + 1]
        self.v_size -= 1
        return retval
        
    def front(self):
        return self.arr[0]
    
    def back(self):
        return self.arr[self.v_size - 1]
    
    def __index_validator(self, index: int) -> bool:
        return isinstance(index, int) and (0 <= index < self.v_size)
        
    def erase_by_index(self, *args):
        if len(args) == 2:
            start, end = args
            if self.__index_validator(start) and self.__index_validator(end) and start < end:
                for i in range(self.v_size - end):
                    self.arr[start + i] = self.arr[end + i]
                self.v_size -= (end - start)
                return
        elif len(args) == 1:
            if self.__index_validator(args[0]):
                for i in range(args[0], self.v_size - 1):
                    self.arr[i] = self.arr[i + 1]
                self.v_size -= 1
                return
        print("Invalid function call.")

    def erase_by_value(self, value, count: int = 1):
        if not self.__index_validator(count):
            raise IndexError("Invalid index.")
        founded_count = 0
        i = 0
        while(i != self.v_size):
            if self.arr[i] == value:
                founded_count += 1
                self.erase_by_index(i)
            else:
                i += 1
            if founded_count == count:
                break
        print(f"Deleted {founded_count}/{count} elements.")

    def swap(self, other: 'Vector'):
        if not isinstance(other, Vector):
            raise TypeError("Invalid type.")
        # version 1
        # self.arr, other.arr = other.arr, self.arr
        # self.v_size, other.v_size = other.v_size, self.v_size
        # self.v_capacity, other.v_capacity = other.v_capacity, self.v_capacity
        # version 2
        size = max(self.v_size, other.v_size)
        if self.v_capacity < size:
            self.__resize()
        if other.v_capacity < size:
            other.__resize()
        for i in range(size):
            self.arr[i], other.arr[i] = other.arr[i], self.arr[i]
        self.v_size, other.v_size = other.v_size, self.v_size
        self.v_capacity, other.v_capacity = other.v_capacity, self.v_capacity

    def clear(self):
        self.v_size = 0

    def copy(self, other: 'Vector'):
        if not isinstance(other, Vector):
            raise TypeError("Invalid type.")
        if self.v_capacity < other.v_size:
            self.__resize()
        for i in range(other.v_size):
            self.arr[i] = other.arr[i]
        self.v_size = other.v_size
        
    def __eq__(self, other: "Vector") -> bool:
        if self.v_size != other.v_size:
            return False
        return all(self.arr == other.arr)
    
    def __le__(self, other: "Vector") -> bool:
        min_size = min(self.v_size, other.v_size)
        for i in range(min_size):
            if self.arr[i] > other.arr[i]:
                return False
        return self.v_size <= other.size or self == other
    
    def __lt__(self, other: "Vector"):
        min_size = min(self.v_size, other.v_size)
        for i in range(min_size):
            if self.arr[i] > other.arr[i]:
                return False
            if self.arr[i] < other.arr[i]:
                return True
        return self.v_size < other.size 
    
    def __gt__(self, other: "Vector"):
        return not self <= other
    
    def __ge__(self, other: "Vector"):
        return not self.arr < other

    def __getitem__(self, index: int):
        return self.arr[:self.v_size][index]
    
    def __add__(self, other: "Vector"):
        max_size = max(self.v_size, other.v_size)
        new_arr = np.zeros(max_size, dtype=self.arr.dtype)
    
        for i in range(min(self.v_size, other.v_size)):
            new_arr[i] = self.arr[i] + other.arr[i]
    
        if self.v_size > other.v_size:
            new_arr[i+1:max_size] = self.arr[i+1:self.v_size]
        elif self.v_size < other.v_size:
            new_arr[i+1:max_size] = other.arr[i+1:other.v_size]
    
        return new_arr


    def __sub__(self, other: "Vector"):
        max_size = max(self.v_size, other.v_size)
        new_arr = np.zeros(max_size, dtype=self.arr.dtype)
    
        for i in range(min(self.v_size, other.v_size)):
            new_arr[i] = self.arr[i] - other.arr[i]
    
        if self.v_size > other.v_size:
            new_arr[i+1:max_size] = self.arr[i+1:self.v_size]
        elif self.v_size < other.v_size:
            new_arr[i+1:max_size] = other.arr[i+1:other.v_size]
    
        return new_arr
    
    def __mul__(self, other: "Vector"):
        max_size = max(self.v_size, other.v_size)
        new_arr = np.zeros(max_size, dtype=self.arr.dtype)
    
        for i in range(min(self.v_size, other.v_size)):
            new_arr[i] = self.arr[i] * other.arr[i]
    
        if self.v_size > other.v_size:
            new_arr[i+1:max_size] = self.arr[i+1:self.v_size]
        elif self.v_size < other.v_size:
            new_arr[i+1:max_size] = other.arr[i+1:other.v_size]
    
        return new_arr
    
    def __truediv__(self, other: "Vector"):
        max_size = max(self.v_size, other.v_size)
        new_arr = np.zeros(max_size, dtype=self.arr.dtype)
    
        for i in range(min(self.v_size, other.v_size)):
            new_arr[i] = self.arr[i] / other.arr[i]
    
        if self.v_size > other.v_size:
            new_arr[i+1:max_size] = self.arr[i+1:self.v_size]
        elif self.v_size < other.v_size:
            new_arr[i+1:max_size] = other.arr[i+1:other.v_size]
    
        return new_arr
    
    def __floordiv__(self, other: "Vector"):
        max_size = max(self.v_size, other.v_size)
        new_arr = np.zeros(max_size, dtype=self.arr.dtype)
    
        for i in range(min(self.v_size, other.v_size)):
            new_arr[i] = self.arr[i] // other.arr[i]
    
        if self.v_size > other.v_size:
            new_arr[i+1:max_size] = self.arr[i+1:self.v_size]
        elif self.v_size < other.v_size:
            new_arr[i+1:max_size] = other.arr[i+1:other.v_size]
    
        return new_arr
    
    def __iadd__(self, other: "Vector"):
        self.arr = self.__add__(other)
        return self.arr
    
    def __isub__(self, other: "Vector"):
        self.arr = self.__sub__(other)
        return self.arr
    
    def __imul__(self, other: "Vector"):
        self.arr = self.__mul__(other)
        return self.arr
    
    def __itruediv__(self, other: "Vector"):
        self.arr = self.__truediv__(other)
        return self.arr
    
    def __ifloordiv__(self, other: "Vector"):
        self.arr = self.__floordiv__(other)
        return self.arr
    
    

v = Vector()
v.push_back(7)
v.push_back(5)
v.push_back(2)
v.push_back(0)

v1 = Vector()
v1.push_back(7)
v1.push_back(1)
v1.push_back(2)
v1.push_back(6)
v1.push_back(9)

print(v)
print(v1)
# print("Addition: ", v + v1)
# print("Subtraction: ", v - v1)
# print("Multiplication: ", v * v1)
# print("Division: ", v / v1)
# print("Floor Division: ", v // v1)

# v += v1
# print("V is: ", v)
# v -= v1
# print("V is: ", v)
# v *= v1
# print("V is: ", v)
# v /= v1
# print("V is: ", v)
v //= v1
print("V is: ", v)
