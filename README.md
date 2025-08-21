# Employee Salary Prediction

This project demonstrates the implementation of Decision Tree and Random Forest regression models to predict employee salaries based on their position levels. The models are trained on a dataset containing employee position levels and their corresponding salaries.

## Features

- Implements Decision Tree Regression
- Implements Random Forest Regression
- Visualizes the regression results
- Makes salary predictions for given position levels

## Prerequisites

- Python 3.x
- Required Python packages:
  - numpy
  - pandas
  - scikit-learn
  - matplotlib

## Installation

1. Clone this repository
2. Install the required packages:
   ```
   pip install numpy pandas scikit-learn matplotlib
   ```

## Dataset

The project uses `emp_sal.csv` which should contain two columns:
1. Position Level
2. Salary

## Usage

1. Ensure the `emp_sal.csv` file is in the same directory as `code.py`
2. Run the script:
   ```
   python code.py
   ```

The script will:
1. Load and preprocess the data
2. Train both Decision Tree and Random Forest regression models
3. Make sample predictions for position levels 6 and 20
4. Print the predicted salaries

## Output

The script outputs the predicted salaries for:
- Decision Tree prediction for position level 20
- Random Forest prediction for position level 6

## Notes

- The Random Forest implementation uses a fixed random state for reproducibility
- The models are trained on the provided dataset and may need retraining for different data distributions
