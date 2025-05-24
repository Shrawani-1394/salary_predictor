## Salary Prediction Using Machine Learning

This project uses machine learning algorithms to predict employee salaries based on years of experience. Implemented using Python and visualized in Google Colab, the model helps understand how experience influences salary.


## Project Overview

- **Goal:** Predict the salary of a person based on their years of experience.
- **Dataset:** A simple CSV file containing two columns: `YearsExperience` and `Salary`.
- **Tech Stack:** Python, Google Colab, Pandas, Matplotlib, Scikit-learn


## Algorithms Used

- **Linear Regression**
- **Decision Tree Regressor**

---

## Model Performance

| Metric        | Score          |
|---------------|----------------|
| R² Score      | ~0.92          |
| MSE           | ~21,000,000    |

The model achieved a high R² score, showing strong correlation between experience and salary.

---

## Visualizations

- Scatter Plot (Actual vs Predicted)
- Decision Tree Diagram
- Bar and Pie Charts for analysis

---

## Dataset

The dataset is in CSV format and includes:

| YearsExperience | Salary      |
|------------------|-------------|
| 1.1              | 39343.00    |
| 1.3              | 46205.00    |
| ...              | ...         |

You can download the dataset from the repo or upload your own in Google Colab.

---

## 🛠️ How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/salary-prediction-ml.git
   cd salary-prediction-ml
2. **Open the notebook in Google Colab**

3. **Upload CSV dataset using:**
from google.colab import files
uploaded = files.upload()
4. **Run all cells to see training, prediction, and visualizations.**

## Requirements
No local setup needed (Google Colab).
But if running locally, install:
pip install pandas matplotlib scikit-learn

## Conclusion
This project demonstrates how machine learning models can be used to understand and predict salary trends using experience as a key input feature. It provides insights through performance metrics and visual tools.

## References
1.Scikit-learn Documentation

2.Kaggle: Salary Dataset

3.Google Colab


