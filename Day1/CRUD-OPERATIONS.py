class crud:

    def create(self, arr, value):
        arr.append(value)
        print(f"Added {value}. Updated List:", arr)


    def read(self, arr):
        print("Current List:", arr)


    def update(self, arr, index, new_value):
        if 0 <= index < len(arr):  # Valid index check
            arr[index] = new_value
            print(f"Updated index {index} to {new_value}. Updated List:", arr)
        else:
            print("Invalid index!")


    def remove(self, arr, index):
        if 0 <= index < len(arr):  # Valid index check
            del arr[index]
            print("Updated List after removal:", arr)
        else:
            print("Invalid index!")



arr = [2, 3, 4, 6, 7, 8]
crud_obj = crud()


crud_obj.create(arr, 10)


crud_obj.read(arr)


crud_obj.update(arr, 2, 99)


crud_obj.remove(arr, 3)


crud_obj.read(arr)
