import numpy as np

class DataAnalytics:
    def __init__(self):
        """Constructor to initialize internal array store."""
        self._array = None  # Encapsulated private attribute

    # Encapsulation
    def set_array(self, arr : np.ndarray):
        """Sets the current working array."""
        self._array = np.array(arr)

    def get_array(self) -> np.ndarray:
        """Returns the current working array."""
        return self._array

    def _is_array_loaded(self) -> bool:
        """Private helper method to check if an array exists."""
        if self._array is None:
            print("\n[!] No array found. Please create or load an array first.")
            return False
        return True

    # ------------------ OOP Decorators ------------------
    @classmethod
    def from_list(cls, data_list):
        """Class method to instantiate DataAnalytics directly from a list."""
        instance = cls()
        instance.set_array(data_list)
        return instance

    @staticmethod
    def parse_input_to_array(input_str: str, dtype=int) -> np.ndarray:
        """Static method to parse space-separated input string to a 1D numpy array."""
        try:
            return np.fromstring(input_str, sep=' ', dtype=dtype)
        except Exception as e:
            print(f"Parsing error: {e}")
            return None

    # ------------------ Array Creation & Slicing ------------------
    def create_1d_array(self, elements: list):
        self._array = np.array(elements)

    def create_2d_array(self, rows: int, cols: int, elements: list):
        self._array = np.array(elements).reshape(rows, cols)

    def create_3d_array(self, dim1: int, dim2: int, dim3: int, elements: list):
        self._array = np.array(elements).reshape(dim1, dim2, dim3)

    def index_array(self, indices: tuple):
        if self._is_array_loaded():
            return self._array[indices]

    def slice_array(self, slice_tuples: tuple):
        """Accepts a tuple of slice objects, e.g., (slice(0, 2), slice(1, 3))"""
        if self._is_array_loaded():
            return self._array[slice_tuples]

    # ------------------ Mathematical Operations ------------------
    def perform_elementwise_op(self, second_arr: np.ndarray, operation: str):
        if not self._is_array_loaded():
            return None
        
        if self._array.shape != second_arr.shape:
            print("\n[!] Error: Shapes of both arrays must match for element-wise operations.")
            return None

        if operation == 'add':
            return np.add(self._array, second_arr)
        elif operation == 'subtract':
            return np.subtract(self._array, second_arr)
        elif operation == 'multiply':
            return np.multiply(self._array, second_arr)
        elif operation == 'divide':
            return np.divide(self._array, second_arr)

    def dot_product(self, second_arr: np.ndarray):
        if self._is_array_loaded():
            return np.dot(self._array, second_arr)

    def matrix_multiply(self, second_arr: np.ndarray):
        if self._is_array_loaded():
            return np.matmul(self._array, second_arr)

    # ------------------ Combine & Split ------------------
    def combine_array(self, second_arr: np.ndarray, axis=0):
        if self._is_array_loaded():
            return np.vstack((self._array, second_arr)) if axis == 0 else np.hstack((self._array, second_arr))

    def split_array(self, sections: int, axis=0):
        if self._is_array_loaded():
            return np.array_split(self._array, sections, axis=axis)

    # ------------------ Search, Sort, Filter ------------------
    def search_value(self, target):
        if self._is_array_loaded():
            indices = np.where(self._array == target)
            return indices

    def sort_array(self, ascending=True, axis=-1):
        if self._is_array_loaded():
            sorted_arr = np.sort(self._array, axis=axis)
            if not ascending:
                sorted_arr = np.flip(sorted_arr, axis=axis)
            return sorted_arr

    def filter_values(self, condition_str: str):
        if self._is_array_loaded():
            # Example condition_str: "> 20" or "== 5"
            arr = self._array
            condition = eval(f"arr {condition_str}")
            return arr[condition]

    # ------------------ Aggregations & Statistics ------------------
    def compute_aggregates(self, op: str, axis=None):
        if not self._is_array_loaded():
            return None

        ops = {
            'sum': np.sum,
            'mean': np.mean,
            'median': np.median,
            'std': np.std,
            'var': np.var,
            'min': np.min,
            'max': np.max
        }
        if op in ops:
            return ops[op](self._array, axis=axis)

    def compute_percentile(self, q: float):
        if self._is_array_loaded():
            return np.percentile(self._array, q)

    def compute_correlation(self, second_arr: np.ndarray):
        if self._is_array_loaded():
            return np.corrcoef(self._array.flatten(), second_arr.flatten())
        
# UI FUNCTION

def main():
    analytics = DataAnalytics()
    print("\n" + "=" * 40)
    print("Welcome to the NumPy Analyzer!")
    while True:
        print("\n","=" * 40)
        print("\nChoose an option:\n")
        print("1. Create a NumPy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()

        # ------------------ Option 1: Array Creation ------------------
        if choice == '1':
            print("\nSelect the type of array to create:")
            print("1. 1D Array\n2. 2D Array\n3. 3D Array")
            type_choice = input("Enter your choice: ").strip()

            if type_choice == '1':
                raw_input = input("Enter elements separated by space: ")
                elements = DataAnalytics.parse_input_to_array(raw_input)
                analytics.create_1d_array(elements)
            elif type_choice == '2':
                rows = int(input("Enter the number of rows: "))
                cols = int(input("Enter the number of columns: "))
                raw_input = input(f"Enter {rows * cols} elements separated by space: ")
                elements = DataAnalytics.parse_input_to_array(raw_input)
                analytics.create_2d_array(rows, cols, elements)
            elif type_choice == '3':
                d1 = int(input("Enter dimension 1: "))
                d2 = int(input("Enter dimension 2: "))
                d3 = int(input("Enter dimension 3: "))
                raw_input = input(f"Enter {d1 * d2 * d3} elements separated by space: ")
                elements = DataAnalytics.parse_input_to_array(raw_input)
                analytics.create_3d_array(d1, d2, d3, elements)

            print("\nArray created successfully:")
            print(analytics.get_array())

            # Indexing / Slicing Submenu
            print("\nChoose an operation:")
            print("1. Indexing\n2. Slicing\n3. Go Back")
            sub_choice = input("Enter your choice: ").strip()

            if sub_choice == '1':
                idx_str = input("Enter comma-separated index values (e.g. 0,1): ")
                indices = tuple(map(int, idx_str.split(',')))
                print(f"Element at {indices}: {analytics.index_array(indices)}")
            elif sub_choice == '2':
                if analytics.get_array().ndim == 2:
                    r_str = input("Enter the row range (start:end): ")
                    c_str = input("Enter the column range (start:end): ")
                    r_start, r_end = map(int, r_str.split(':'))
                    c_start, c_end = map(int, c_str.split(':'))
                    slices = (slice(r_start, r_end), slice(c_start, c_end))
                    print("\nSliced Array:")
                    print(analytics.slice_array(slices))
                else:
                    print("Slicing demonstration configured for 2D array.")

        # ------------------ Option 2: Math Operations ------------------
        elif choice == '2':
            if not analytics._is_array_loaded():
                continue

            print("\nChoose a mathematical operation:")
            print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
            m_choice = input("Enter your choice: ").strip()
            
            ops_map = {'1': 'add', '2': 'subtract', '3': 'multiply', '4': 'divide'}
            if m_choice in ops_map:
                size = analytics.get_array().size
                raw_input = input(f"Enter the same-size array elements ({size} elements separated by space): ")
                second_arr = DataAnalytics.parse_input_to_array(raw_input).reshape(analytics.get_array().shape)

                print("\nOriginal Array:")
                print(analytics.get_array())
                print("\nSecond Array:")
                print(second_arr)
                
                result = analytics.perform_elementwise_op(second_arr, ops_map[m_choice])
                print(f"\nResult of Operation:")
                print(result)

        # ------------------ Option 3: Combine or Split ------------------
        elif choice == '3':
            if not analytics._is_array_loaded():
                continue

            print("\nChoose an option:\n1. Combine Arrays\n2. Split Array")
            cs_choice = input("Enter your choice: ").strip()

            if cs_choice == '1':
                size = analytics.get_array().size
                raw_input = input(f"Enter the elements of another array to combine ({size} elements separated by space): ")
                second_arr = DataAnalytics.parse_input_to_array(raw_input).reshape(analytics.get_array().shape)
                
                print("\nOriginal Array:\n", analytics.get_array())
                print("\nSecond Array:\n", second_arr)
                
                combined = analytics.combine_array(second_arr, axis=0)
                print("\nCombined Array (Vertical Stack):\n", combined)
            elif cs_choice == '2':
                sections = int(input("Enter number of splits: "))
                splits = analytics.split_array(sections)
                print("\nSplit Arrays:")
                for i, s in enumerate(splits):
                    print(f"Part {i+1}:\n{s}")

        # ------------------ Option 4: Search, Sort, Filter ------------------
        elif choice == '4':
            if not analytics._is_array_loaded():
                continue

            print("\nChoose an option:\n1. Search a value\n2. Sort the array\n3. Filter values")
            ssf_choice = input("Enter your choice: ").strip()

            if ssf_choice == '1':
                val = float(input("Enter value to search: "))
                pos = analytics.search_value(val)
                print(f"Value found at index positions: {pos}")
            elif ssf_choice == '2':
                print("\nOriginal Array:\n", analytics.get_array())
                sorted_arr = analytics.sort_array(ascending=True, axis=-1)
                print("\nSorted Array:\n", sorted_arr)
                print("(Sorting applied row-wise.)")
            elif ssf_choice == '3':
                cond = input("Enter condition relative to elements (e.g. '> 30'): ")
                filtered = analytics.filter_values(cond)
                print(f"\nFiltered elements ({cond}): {filtered}")

        # ------------------ Option 5: Aggregates & Statistics ------------------
        elif choice == '5':
            if not analytics._is_array_loaded():
                continue

            print("\nChoose an aggregate/statistical operation:")
            print("1. Sum\n2. Mean\n3. Median\n4. Standard Deviation\n5. Variance")
            stat_choice = input("Enter your choice: ").strip()

            stat_map = {'1': 'sum', '2': 'mean', '3': 'median', '4': 'std', '5': 'var'}
            if stat_choice in stat_map:
                op_name = stat_map[stat_choice]
                res = analytics.compute_aggregates(op_name)
                print("\nOriginal Array:\n", analytics.get_array())
                print(f"\n{op_name.capitalize()} of Array: {res}")

        # ------------------ Option 6: Exit ------------------
        elif choice == '6':
            print("\nThank you for using the NumPy Analyzer!\nGoodbye!")
            break
        else:
            print("\n[!] Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
