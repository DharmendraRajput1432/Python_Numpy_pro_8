import numpy as np


class DataAnalytics:
    """Simple class for creating and analyzing NumPy arrays."""

    def __init__(self):
        # Store the current NumPy array
        self.array = None

    # ---------------------------------------------------------
    # ARRAY SETTER / GETTER
    # ---------------------------------------------------------

    def set_array(self, array):
        """Store an array."""
        self.array = np.array(array)

    def get_array(self):
        """Return the current array."""
        return self.array

    def is_array_loaded(self):
        """Check whether an array has been created."""
        if self.array is None:
            print("\nNo array found. Please create an array first.")
            return False

        return True

    # ---------------------------------------------------------
    # CLASS METHOD AND STATIC METHOD
    # ---------------------------------------------------------

    @classmethod
    def from_list(cls, data_list):
        """Create a DataAnalytics object directly from a list."""
        analytics = cls()
        analytics.set_array(data_list)
        return analytics

    @staticmethod
    def parse_input_to_array(user_input, data_type=int):
        """Convert space-separated input into a NumPy array."""
        try:
            return np.fromstring(user_input, sep=" ", dtype=data_type)
        except Exception as error:
            print(f"Input error: {error}")
            return None

    # ---------------------------------------------------------
    # CREATE ARRAYS
    # ---------------------------------------------------------

    def create_1d_array(self, elements):
        """Create a 1D array."""
        self.array = np.array(elements)

    def create_2d_array(self, rows, columns, elements):
        """Create a 2D array."""
        self.array = np.array(elements).reshape(rows, columns)

    def create_3d_array(self, dim1, dim2, dim3, elements):
        """Create a 3D array."""
        self.array = np.array(elements).reshape(dim1, dim2, dim3)

    # ---------------------------------------------------------
    # INDEXING AND SLICING
    # ---------------------------------------------------------

    def index_array(self, indices):
        """Get an element using its index."""
        if self.is_array_loaded():
            return self.array[indices]

    def slice_array(self, slices):
        """Return a sliced part of the array."""
        if self.is_array_loaded():
            return self.array[slices]

    # ---------------------------------------------------------
    # MATHEMATICAL OPERATIONS
    # ---------------------------------------------------------

    def perform_elementwise_operation(self, second_array, operation):
        """Perform addition, subtraction, multiplication, or division."""

        if not self.is_array_loaded():
            return None

        if self.array.shape != second_array.shape:
            print("\nError: Both arrays must have the same shape.")
            return None

        if operation == "add":
            return np.add(self.array, second_array)

        if operation == "subtract":
            return np.subtract(self.array, second_array)

        if operation == "multiply":
            return np.multiply(self.array, second_array)

        if operation == "divide":
            return np.divide(self.array, second_array)

        print("\nInvalid mathematical operation.")
        return None

    def dot_product(self, second_array):
        """Calculate the dot product of two arrays."""
        if self.is_array_loaded():
            return np.dot(self.array, second_array)

    def matrix_multiply(self, second_array):
        """Perform matrix multiplication."""
        if self.is_array_loaded():
            return np.matmul(self.array, second_array)

    # ---------------------------------------------------------
    # COMBINE AND SPLIT ARRAYS
    # ---------------------------------------------------------

    def combine_array(self, second_array, axis=0):
        """Combine two arrays vertically or horizontally."""
        if not self.is_array_loaded():
            return None

        if axis == 0:
            return np.vstack((self.array, second_array))

        return np.hstack((self.array, second_array))

    def split_array(self, number_of_parts, axis=0):
        """Split the current array into multiple parts."""
        if self.is_array_loaded():
            return np.array_split(self.array, number_of_parts, axis=axis)

    # ---------------------------------------------------------
    # SEARCH, SORT AND FILTER
    # ---------------------------------------------------------

    def search_value(self, value):
        """Find the positions of a value in the array."""
        if self.is_array_loaded():
            return np.where(self.array == value)

    def sort_array(self, ascending=True, axis=-1):
        """Sort the array."""
        if not self.is_array_loaded():
            return None

        sorted_array = np.sort(self.array, axis=axis)

        if not ascending:
            sorted_array = np.flip(sorted_array, axis=axis)

        return sorted_array

    def filter_values(self, condition):
        """
        Filter values using a condition.

        Supported conditions:
        > 20
        < 20
        >= 20
        <= 20
        == 20
        != 20
        """
        if not self.is_array_loaded():
            return None

        condition = condition.strip()

        operators = [">=", "<=", "!=", "==", ">", "<"]

        for operator in operators:
            if condition.startswith(operator):
                value = float(condition[len(operator):].strip())

                if operator == ">":
                    mask = self.array > value
                elif operator == "<":
                    mask = self.array < value
                elif operator == ">=":
                    mask = self.array >= value
                elif operator == "<=":
                    mask = self.array <= value
                elif operator == "==":
                    mask = self.array == value
                else:
                    mask = self.array != value

                return self.array[mask]

        print("\nInvalid condition.")
        return None

    # ---------------------------------------------------------
    # AGGREGATIONS AND STATISTICS
    # ---------------------------------------------------------

    def compute_aggregate(self, operation, axis=None):
        """Calculate common statistical values."""

        if not self.is_array_loaded():
            return None

        if operation == "sum":
            return np.sum(self.array, axis=axis)

        if operation == "mean":
            return np.mean(self.array, axis=axis)

        if operation == "median":
            return np.median(self.array, axis=axis)

        if operation == "std":
            return np.std(self.array, axis=axis)

        if operation == "var":
            return np.var(self.array, axis=axis)

        if operation == "min":
            return np.min(self.array, axis=axis)

        if operation == "max":
            return np.max(self.array, axis=axis)

        print("\nInvalid statistical operation.")
        return None

    def compute_percentile(self, percentage):
        """Calculate a percentile."""
        if self.is_array_loaded():
            return np.percentile(self.array, percentage)

    def compute_correlation(self, second_array):
        """Calculate correlation between two arrays."""
        if self.is_array_loaded():
            first = self.array.flatten()
            second = second_array.flatten()

            return np.corrcoef(first, second)


# =============================================================
# HELPER FUNCTIONS FOR USER INPUT
# =============================================================

def create_array_menu(analytics):
    """Create a 1D, 2D, or 3D array."""

    print("\nSelect array type:")
    print("1. 1D Array")
    print("2. 2D Array")
    print("3. 3D Array")

    choice = input("Enter your choice: ").strip()

    try:
        if choice == "1":
            user_input = input("Enter elements separated by spaces: ")
            elements = DataAnalytics.parse_input_to_array(user_input)

            if elements is not None:
                analytics.create_1d_array(elements)

        elif choice == "2":
            rows = int(input("Enter number of rows: "))
            columns = int(input("Enter number of columns: "))

            total_elements = rows * columns
            user_input = input(
                f"Enter {total_elements} elements separated by spaces: "
            )

            elements = DataAnalytics.parse_input_to_array(user_input)

            if elements is not None and len(elements) == total_elements:
                analytics.create_2d_array(rows, columns, elements)
            else:
                print("\nError: Number of elements does not match the shape.")

        elif choice == "3":
            dim1 = int(input("Enter dimension 1: "))
            dim2 = int(input("Enter dimension 2: "))
            dim3 = int(input("Enter dimension 3: "))

            total_elements = dim1 * dim2 * dim3

            user_input = input(
                f"Enter {total_elements} elements separated by spaces: "
            )

            elements = DataAnalytics.parse_input_to_array(user_input)

            if elements is not None and len(elements) == total_elements:
                analytics.create_3d_array(dim1, dim2, dim3, elements)
            else:
                print("\nError: Number of elements does not match the shape.")

        else:
            print("\nInvalid choice.")
            return

        print("\nArray created successfully:")
        print(analytics.get_array())

        indexing_and_slicing_menu(analytics)

    except ValueError:
        print("\nPlease enter valid numbers.")


def indexing_and_slicing_menu(analytics):
    """Show indexing and slicing options."""

    print("\nChoose an operation:")
    print("1. Indexing")
    print("2. Slicing")
    print("3. Go Back")

    choice = input("Enter your choice: ").strip()

    try:
        if choice == "1":
            index_input = input(
                "Enter comma-separated indexes (example: 0,1): "
            )

            indexes = tuple(
                map(int, index_input.split(","))
            )

            print(
                f"Element at {indexes}: "
                f"{analytics.index_array(indexes)}"
            )

        elif choice == "2":
            if analytics.get_array().ndim == 2:
                row_range = input("Enter row range (start:end): ")
                column_range = input("Enter column range (start:end): ")

                row_start, row_end = map(int, row_range.split(":"))
                column_start, column_end = map(
                    int,
                    column_range.split(":")
                )

                slices = (
                    slice(row_start, row_end),
                    slice(column_start, column_end)
                )

                print("\nSliced Array:")
                print(analytics.slice_array(slices))

            else:
                print("\nSlicing example is currently configured for 2D arrays.")

    except (ValueError, IndexError):
        print("\nInvalid index or slicing format.")


def mathematical_operations_menu(analytics):
    """Perform mathematical operations on two arrays."""

    if not analytics.is_array_loaded():
        return

    print("\nChoose a mathematical operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice: ").strip()

    operation_map = {
        "1": "add",
        "2": "subtract",
        "3": "multiply",
        "4": "divide"
    }

    if choice not in operation_map:
        print("\nInvalid choice.")
        return

    try:
        size = analytics.get_array().size

        user_input = input(
            f"Enter {size} elements for the second array: "
        )

        second_array = DataAnalytics.parse_input_to_array(user_input)

        if second_array is None or len(second_array) != size:
            print("\nError: Please enter the correct number of elements.")
            return

        second_array = second_array.reshape(
            analytics.get_array().shape
        )

        print("\nOriginal Array:")
        print(analytics.get_array())

        print("\nSecond Array:")
        print(second_array)

        result = analytics.perform_elementwise_operation(
            second_array,
            operation_map[choice]
        )

        print("\nResult:")
        print(result)

    except ValueError:
        print("\nInvalid input.")


def combine_and_split_menu(analytics):
    """Combine or split arrays."""

    if not analytics.is_array_loaded():
        return

    print("\nChoose an option:")
    print("1. Combine Arrays")
    print("2. Split Array")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        try:
            size = analytics.get_array().size

            user_input = input(
                f"Enter {size} elements for the second array: "
            )

            second_array = DataAnalytics.parse_input_to_array(user_input)

            if second_array is None or len(second_array) != size:
                print("\nError: Please enter the correct number of elements.")
                return

            second_array = second_array.reshape(
                analytics.get_array().shape
            )

            print("\nOriginal Array:")
            print(analytics.get_array())

            print("\nSecond Array:")
            print(second_array)

            combined_array = analytics.combine_array(
                second_array,
                axis=0
            )

            print("\nCombined Array:")
            print(combined_array)

        except ValueError:
            print("\nInvalid input.")

    elif choice == "2":
        try:
            number_of_splits = int(
                input("Enter number of splits: ")
            )

            split_arrays = analytics.split_array(number_of_splits)

            print("\nSplit Arrays:")

            for number, array_part in enumerate(split_arrays, start=1):
                print(f"\nPart {number}:")
                print(array_part)

        except ValueError:
            print("\nPlease enter a valid number.")

    else:
        print("\nInvalid choice.")


def search_sort_filter_menu(analytics):
    """Search, sort, or filter the current array."""

    if not analytics.is_array_loaded():
        return

    print("\nChoose an option:")
    print("1. Search a value")
    print("2. Sort the array")
    print("3. Filter values")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        try:
            value = float(input("Enter value to search: "))
            positions = analytics.search_value(value)

            print("\nValue found at index positions:")
            print(positions)

        except ValueError:
            print("\nPlease enter a valid number.")

    elif choice == "2":
        print("\nOriginal Array:")
        print(analytics.get_array())

        sorted_array = analytics.sort_array(
            ascending=True,
            axis=-1
        )

        print("\nSorted Array:")
        print(sorted_array)
        print("\nSorting is applied row-wise.")

    elif choice == "3":
        condition = input(
            "Enter condition (example: > 30): "
        )

        filtered_values = analytics.filter_values(condition)

        print(f"\nFiltered values ({condition}):")
        print(filtered_values)

    else:
        print("\nInvalid choice.")


def statistics_menu(analytics):
    """Calculate statistics for the current array."""

    if not analytics.is_array_loaded():
        return

    print("\nChoose a statistical operation:")
    print("1. Sum")
    print("2. Mean")
    print("3. Median")
    print("4. Standard Deviation")
    print("5. Variance")

    choice = input("Enter your choice: ").strip()

    operation_map = {
        "1": "sum",
        "2": "mean",
        "3": "median",
        "4": "std",
        "5": "var"
    }

    if choice not in operation_map:
        print("\nInvalid choice.")
        return

    operation = operation_map[choice]

    result = analytics.compute_aggregate(operation)

    print("\nOriginal Array:")
    print(analytics.get_array())

    print(f"\n{operation.capitalize()} of Array:")
    print(result)


# =============================================================
# MAIN PROGRAM
# =============================================================

def main():
    """Start the NumPy Analyzer program."""

    analytics = DataAnalytics()

    while True:
        print("\n" + "=" * 45)
        print("        NUMPY ANALYZER")
        print("=" * 45)

        print("\nChoose an option:")
        print("1. Create a NumPy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            create_array_menu(analytics)

        elif choice == "2":
            mathematical_operations_menu(analytics)

        elif choice == "3":
            combine_and_split_menu(analytics)

        elif choice == "4":
            search_sort_filter_menu(analytics)

        elif choice == "5":
            statistics_menu(analytics)

        elif choice == "6":
            print("\nThank you for using NumPy Analyzer!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()
