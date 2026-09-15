# 🔢 NumPy Analyzer

A menu-driven **Python + NumPy command-line application** for creating, manipulating, searching, sorting, filtering, and performing statistical operations on **1D, 2D, and 3D NumPy arrays**.

This project demonstrates practical implementation of **Object-Oriented Programming (OOP)** concepts along with fundamental **NumPy and Data Analytics operations**.

---

## 📌 Project Overview

**NumPy Analyzer** provides an interactive CLI where users can create NumPy arrays and perform different analytical operations without writing individual NumPy commands manually.

The project is designed as a learning and portfolio project for practicing:

* Python
* Object-Oriented Programming
* NumPy
* Array manipulation
* Mathematical operations
* Statistics
* Command-Line Interface development

---

## ✨ Features

### 📦 Array Creation

Supports creation of:

* 1D arrays
* 2D arrays
* 3D arrays

Example:

```text
1D Array:
[10 20 30 40 50]

2D Array:
[[10 20 30]
 [40 50 60]]

3D Array:
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
```

---

### 🔍 Indexing & Slicing

The application supports:

* Array indexing
* Multi-dimensional indexing
* 2D array slicing

Example:

```python
array[1, 2]
```

2D slicing:

```python
array[0:2, 1:3]
```

---

### ➕ Mathematical Operations

Perform element-wise operations between two arrays:

* Addition
* Subtraction
* Multiplication
* Division

The application verifies that both arrays have matching shapes before performing element-wise operations.

Example:

```text
Array 1:
[10 20 30]

Array 2:
[1  2  3]

Addition:
[11 22 33]
```

---

### 🔢 Dot Product & Matrix Multiplication

The `DataAnalytics` class also provides methods for:

```python
dot_product()
```

and:

```python
matrix_multiply()
```

These demonstrate NumPy's linear algebra capabilities.

---

### 🔗 Combine & Split Arrays

The project supports:

* Vertical stacking
* Horizontal stacking
* Splitting an array into multiple sections

Examples of NumPy operations used internally:

```python
np.vstack()
np.hstack()
np.array_split()
```

---

### 🔎 Search, Sort & Filter

Users can:

* Search for a specific value
* Sort arrays
* Sort in ascending or descending order
* Filter values using a condition

Example:

```text
Enter condition:
> 30
```

The application returns elements satisfying the condition.

---

### 📊 Aggregations & Statistics

The project includes several statistical operations:

* Sum
* Mean
* Median
* Standard Deviation
* Variance
* Minimum
* Maximum
* Percentile
* Correlation

These operations provide a foundation for basic numerical data analysis.

---

# 🧠 OOP Concepts Demonstrated

One of the main goals of this project is to demonstrate Python OOP concepts.

## 1. Class

The main functionality is organized inside:

```python
class DataAnalytics:
```

This class manages the current NumPy array and provides methods for different operations.

---

## 2. Constructor

The constructor initializes the internal array:

```python
def __init__(self):
    self._array = None
```

Initially, no array is loaded.

---

## 3. Encapsulation

The current array is stored using:

```python
self._array
```

The class provides controlled access through:

```python
set_array()
get_array()
```

Example:

```python
analytics.set_array([10, 20, 30])

print(analytics.get_array())
```

---

## 4. Private-Style Helper Method

The project contains:

```python
def _is_array_loaded(self):
```

This method checks whether an array is available before performing operations.

Example message:

```text
[!] No array found. Please create or load an array first.
```

---

## 5. Class Method

The project demonstrates `@classmethod` through:

```python
@classmethod
def from_list(cls, data_list):
```

It allows an object to be created directly from a Python list.

Example:

```python
analytics = DataAnalytics.from_list([10, 20, 30, 40])
```

---

## 6. Static Method

The input parser uses:

```python
@staticmethod
def parse_input_to_array(input_str, dtype=int):
```

Because this method does not depend on a particular object instance, it is implemented as a static method.

Example:

```python
arr = DataAnalytics.parse_input_to_array("10 20 30 40")
```

---

# 🏗️ Project Structure

A recommended GitHub repository structure is:

```text
numpy-analyzer/
│
├── numpy_analyzer.py
├── README.md
├── requirements.txt
└── .gitignore
```

### `numpy_analyzer.py`

Contains the complete NumPy Analyzer application.

### `README.md`

Project documentation.

### `requirements.txt`

Contains project dependencies.

Example:

```text
numpy
```

### `.gitignore`

Prevents unnecessary files from being committed to GitHub.

Example:

```text
__pycache__/
*.pyc
.venv/
venv/
.env
.ipynb_checkpoints/
```

---

# 🛠️ Technologies Used

| Technology | Purpose                             |
| ---------- | ----------------------------------- |
| Python     | Application development             |
| NumPy      | Numerical and array operations      |
| OOP        | Code organization and encapsulation |
| CLI        | Interactive user interface          |

---

# 📋 Application Menu

When the application starts, the following menu is displayed:

```text
========================================
Welcome to the NumPy Analyzer!
========================================

Choose an option:

1. Create a NumPy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit
```

---

# 🚀 Installation

## Prerequisites

Make sure Python is installed.

Check your Python version:

```bash
python --version
```

You can also use:

```bash
python3 --version
```

---

## Install NumPy

Install NumPy using:

```bash
pip install numpy
```

Or install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/numpy-analyzer.git
```

Navigate to the project:

```bash
cd numpy-analyzer
```

Run the application:

```bash
python numpy_analyzer.py
```

---

# 💻 Example Usage

## Step 1: Create a 1D Array

Select:

```text
1. Create a NumPy Array
```

Then:

```text
1. 1D Array
```

Enter:

```text
10 20 30 40 50
```

Output:

```text
Array created successfully:
[10 20 30 40 50]
```

---

## Step 2: Perform Addition

Select:

```text
2. Perform Mathematical Operations
```

Then:

```text
1. Addition
```

Enter:

```text
1 2 3 4 5
```

Result:

```text
[11 22 33 44 55]
```

---

## Step 3: Calculate Statistics

Select:

```text
5. Compute Aggregates and Statistics
```

Then select:

```text
1. Sum
```

For:

```text
[10 20 30 40 50]
```

The result is:

```text
150
```

---

# 📚 Main Class Methods

## Array Management

```python
set_array()
get_array()
_is_array_loaded()
```

## Array Creation

```python
create_1d_array()
create_2d_array()
create_3d_array()
```

## Indexing & Slicing

```python
index_array()
slice_array()
```

## Mathematical Operations

```python
perform_elementwise_op()
dot_product()
matrix_multiply()
```

## Combining & Splitting

```python
combine_array()
split_array()
```

## Search, Sort & Filter

```python
search_value()
sort_array()
filter_values()
```

## Statistics

```python
compute_aggregates()
compute_percentile()
compute_correlation()
```

---

# 📊 Supported Operations

| Category            | Operations                                      |
| ------------------- | ----------------------------------------------- |
| Array Creation      | 1D, 2D, 3D                                      |
| Indexing            | Single and multi-dimensional indexing           |
| Slicing             | 2D slicing                                      |
| Mathematics         | Addition, subtraction, multiplication, division |
| Linear Algebra      | Dot product, matrix multiplication              |
| Combining           | Vertical and horizontal stacking                |
| Splitting           | Array splitting                                 |
| Searching           | Search for values                               |
| Sorting             | Ascending / descending                          |
| Filtering           | Conditional filtering                           |
| Statistics          | Sum, mean, median, standard deviation, variance |
| Advanced Statistics | Minimum, maximum, percentile, correlation       |

---

# ⚠️ Error Handling

The project contains basic checks to prevent operations when an array has not been created.

Example:

```text
[!] No array found. Please create or load an array first.
```

For element-wise mathematical operations, the project checks array shapes:

```text
[!] Error: Shapes of both arrays must match for element-wise operations.
```

---

# 🎯 Learning Objectives

This project helps develop practical understanding of:

* Python classes and objects
* Constructors
* Encapsulation
* Class methods
* Static methods
* Protected-style attributes
* NumPy arrays
* Multi-dimensional arrays
* Array indexing
* Array slicing
* Element-wise operations
* Matrix operations
* Array stacking
* Array splitting
* Searching
* Sorting
* Boolean filtering
* Statistical calculations
* CLI-based applications

---

# 🔮 Future Improvements

The project can be expanded with:

* [ ] CSV file loading
* [ ] Excel file loading
* [ ] JSON data support
* [ ] Pandas integration
* [ ] Matplotlib visualization
* [ ] Better input validation
* [ ] Comprehensive exception handling
* [ ] Matrix transpose
* [ ] Additional linear algebra operations
* [ ] Export analysis results
* [ ] Automated unit testing
* [ ] Graphical User Interface (GUI)
* [ ] More advanced data-analysis features

---

# 📈 Future Data Analytics Integration

A future version can transform this project into a small data-analysis toolkit by integrating:

```text
NumPy
   ↓
Pandas
   ↓
Data Cleaning
   ↓
Data Analysis
   ↓
Matplotlib / Seaborn
   ↓
Data Visualization
```

This would make the project more closely aligned with real-world **Data Analyst workflows**.

---

# 🧪 Testing

Automated tests can be added in the future using `pytest`.

Recommended structure:

```text
tests/
│
├── test_array_creation.py
├── test_math_operations.py
├── test_search_sort.py
├── test_statistics.py
└── test_array_operations.py
```

Example future test:

```python
def test_array_creation():
    analytics = DataAnalytics.from_list([10, 20, 30])

    assert analytics.get_array().tolist() == [10, 20, 30]
```

---

# 👨‍💻 Skills Demonstrated

This project demonstrates practical experience with:

**Python • NumPy • Object-Oriented Programming • Encapsulation • Static Methods • Class Methods • Numerical Computing • Array Manipulation • Statistics • CLI Development**

---

# 📄 License

This project is intended for **educational and personal portfolio use**.

You are welcome to modify and improve the project for learning purposes.

---

# 🤝 Contributing

Contributions and suggestions are welcome.

To contribute:

```bash
git clone https://github.com/YOUR_USERNAME/numpy-analyzer.git
```

Create a new branch:

```bash
git checkout -b feature/new-feature
```

Make your changes, test the application, and submit a pull request.

---

# 👤 Author

**Dharmendra Rajput**

Aspiring Data Analyst

**Skills:** Python | NumPy | Pandas | SQL | Data Visualization

---

# ⭐ Support

If you found this project useful for learning Python, NumPy, or Data Analytics, consider giving the repository a ⭐ on GitHub.
