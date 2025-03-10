class CustomList:
    def __init__(List, capacity=10):
        List._array = [None] * capacity
        List._capacity = capacity
        List._size = 0
        print(f"Created new CustomList with capacity: {List._capacity}")
        print(f"Current size: {List._size}")

    def append(List, element):
        if List._size >= List._capacity:
            print("List is full!")
            return
        List._array[List._size] = element
        List._size += 1
        print(f"Appended {element} to the list.")

    def get(List, index):
        if 0 <= index < List._size:
            print(f"Element at index {index}: {List._array[index]}")
            return List._array[index]
        else:
            print("Index out of bounds!")
            return None
        
    def set(List, index, element):
        if 0 <= index < List._size:
            List._array[index] = element
            print(f"Set element at index {index} to {element}")
        else:
            print("Index out of bounds!")

    def size(List):
        print(f"Current size: {List._size}")
        return List._size

custom_list = CustomList()
custom_list.append(5)
custom_list.get(0)
custom_list.set(0, 10)
custom_list.get(0)
custom_list.size()