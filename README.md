# 🤖 Machine Learning with Adarsh

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-ML%20Models-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Status-Active%20Learning-brightgreen?style=for-the-badge)](#)

Welcome to my personal Machine Learning repository! 🚀  
This repository documents my step-by-step journey of mastering Machine Learning from ground zero — starting with **Python & Data Analysis**, moving into **Data Preprocessing & Feature Engineering**, also and advancing towards **Supervised, Unsupervised ML algorithms, Deep Learning, and Real-world Projects**.

---

## 📌 Learning Roadmap & Progress Tracker

Here is the structured roadmap being actively executed in this repository:

### 🟢 Phase 1: Python for Data Analysis & Core Concepts `[Completed / Active]`
- [x] Python Fundamentals, Control Flow & Loops
- [x] Data Structures (Lists, Tuples, Dictionaries, Sets)
- [x] Object-Oriented Programming (OOP: Classes, Objects, Constructors)
- [x] Broadcasting & Functional Concepts in Python
- [x] Hands-on mini logic scripts & data manipulation

### 🟡 Phase 2: Data Cleaning & Preprocessing `[Active / Advanced]`
Data preprocessing is the backbone of any reliable ML pipeline:
- [x] **Missing Value Imputation**: Mean, Median, Mode & Forward/Backward fill (`Missing_Values.ipynb`)
- [x] **Duplicate Record Handling**: Identifying & dropping redundant data (`Duplicate_Removal.ipynb`)
- [x] **Outlier Detection & Treatment**: IQR, Z-Score, and Visual Boxplots (`outlier_detection.ipynb`)
- [x] **Categorical Encoding**:
  - [x] Label Encoding (`label_encoding.ipynb`)
  - [x] One-Hot Encoding (`one_hot_encoding.ipynb`)
  - [x] Ordinal Encoding (`ordinal_encoding.ipynb`)
- [x] **Feature Scaling & Transformation**:
  - [x] Feature Scaling (`feature_scaling.ipynb`)
  - [x] Standardization (`standardization.ipynb`)
  - [x] Normalization (`normalization.ipynb`)
- [x] **Pipeline, Data Splitting & Prevention**:
  - [x] Train-Test Split (`train_test_split.ipynb`)
  - [x] Data Leakage Prevention (`data_leakage.ipynb`)
  - [x] Scikit-Learn Pipeline (`sklearn_pipeline.ipynb`)
- [x] **End-to-End Workflows**:
  - [x] Data Cleaning (`Data_Cleaning.ipynb`)
  - [x] Comprehensive Preprocessing (`Data_Preprocessing.ipynb`)
- [ ] Handling Imbalanced Datasets (SMOTE, Undersampling, Class Weights)

### 🔵 Phase 3: Exploratory Data Analysis (EDA) & Visualization `[Upcoming]`
- [ ] Univariate, Bivariate, and Multivariate Analysis
- [ ] Correlation Matrix & Heatmaps
- [ ] Data Visualization using Matplotlib & Seaborn
- [ ] Automated EDA (ydata-profiling / Sweetviz)

### 🟣 Phase 4: Supervised Machine Learning `[Upcoming]`
#### 📈 Regression:
- [ ] Linear Regression (Simple & Multiple)
- [ ] Ridge & Lasso (L1 & L2 Regularization)
- [ ] Polynomial Regression
- [ ] Decision Tree Regressor & Random Forest Regressor

#### 🏷️ Classification:
- [ ] Logistic Regression
- [ ] K-Nearest Neighbors (KNN)
- [ ] Support Vector Machines (SVM)
- [ ] Naive Bayes Classifier
- [ ] Decision Trees & Random Forest Classifier
- [ ] Gradient Boosting (XGBoost, LightGBM, CatBoost)

### 🟠 Phase 5: Unsupervised Machine Learning `[Upcoming]`
- [ ] Clustering (K-Means, Hierarchical, DBSCAN)
- [ ] Dimensionality Reduction (PCA - Principal Component Analysis, t-SNE)
- [ ] Anomaly Detection Algorithms

### 🔴 Phase 6: Model Evaluation, Tuning & Deployment `[Upcoming]`
- [ ] Metrics: Confusion Matrix, Precision, Recall, F1-Score, ROC-AUC, RMSE, MAE, R²
- [ ] Cross-Validation Strategies (K-Fold, Stratified K-Fold)
- [ ] Hyperparameter Optimization (GridSearchCV, RandomizedSearchCV, Optuna)
- [ ] Model Serialization (Joblib, Pickle) & Deployment (Streamlit / Flask / FastAPI)

---

## 📂 Repository Structure

```text
Machine_Learning-with-adarsh/
│
├── Data_Analysis_in_Python/              # Core Python & Data Analysis scripts
│   ├── broadcasting.py                   # NumPy / Python broadcasting mechanics
│   ├── clas.py & class.py                # OOP concepts & class structures
│   ├── constructor.py                    # OOP constructors & instance handling
│   ├── dict.py                           # Dictionary operations & methods
│   ├── list_and_tuple.py                 # Lists and tuples manipulations
│   ├── loops.py & conditional.py         # Flow control & logical branching
│   ├── Dsa.py                            # Data structures & problem solving
│   └── ...                               # Other utility & practice scripts
│
├── Data_Preprocessing_for_ML/            # Comprehensive Data Preprocessing & Feature Engineering
│   ├── Data_Cleaning.ipynb               # End-to-end data cleaning workflows
│   ├── Data_Preprocessing.ipynb          # Systematic preprocessing pipelines
│   ├── Duplicate_Removal.ipynb           # Identifying & removing duplicate rows
│   ├── Missing_Values.ipynb              # Handling missing / NaN values
│   ├── outlier_detection.ipynb           # Outlier detection (IQR, Boxplots, etc.)
│   ├── label_encoding.ipynb              # Label encoding implementation
│   ├── one_hot_encoding.ipynb            # One-hot encoding implementation
│   ├── ordinal_encoding.ipynb            # Ordinal encoding implementation
│   ├── feature_scaling.ipynb             # Feature scaling techniques
│   ├── standardization.ipynb             # Standardization (StandardScaler)
│   ├── normalization.ipynb               # Normalization (MinMaxScaler)
│   ├── train_test_split.ipynb            # Train-Test data splitting strategies
│   ├── data_leakage.ipynb                # Preventing data leakage in ML pipelines
│   ├── sklearn_pipeline.ipynb            # Scikit-Learn Pipeline building
│   ├── my_data.csv                       # Practice dataset
│   ├── student_cleaned.csv               # Post-cleaning dataset
│   └── student_one_hot_encoded.csv       # Post-encoding demonstration dataset
│
├── .gitignore                            # Standard git ignore definitions
└── README.md                             # Documentation & learning roadmap
```

---

## 🛠️ Tech Stack & Libraries Used

| Category | Tools & Libraries |
| :--- | :--- |
| **Language** | Python 3.x |
| **Environment** | Jupyter Notebook, VS Code |
| **Data Manipulation** | Pandas, NumPy |
| **Data Visualization** | Matplotlib, Seaborn *(integrated in upcoming notebooks)* |
| **Machine Learning** | Scikit-Learn |
| **Version Control** | Git, GitHub |

---

## 🚀 Getting Started Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dwivediadarsh496-commits/Machine_Learning-with-adarsh-.git
   cd Machine_Learning-with-adarsh-
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install required packages:**
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn jupyter
   ```

4. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

---

## 👨‍💻 Author

**Adarsh Dwivedi**  
- GitHub: [@dwivediadarsh496-commits](https://github.com/dwivediadarsh496-commits)
- Repository: [Machine_Learning-with-adarsh-](https://github.com/dwivediadarsh496-commits/Machine_Learning-with-adarsh-)

⭐ *Feel free to star this repository to follow along with the ML learning journey!*
