# Effect Size Measurement Toolkit

## Project Overview

This project provides a collection of modular, scalable, and reusable Python scripts designed to compute various effect size measurements. Effect sizes are critical statistical metrics that quantify the magnitude of relationships or differences between variables, providing deeper insights beyond p-values and significance tests. This toolkit aims to support researchers, data scientists, and analysts in performing robust and interpretable statistical analyses.

## Goals

* To develop efficient and clean Python implementations of key effect size measures.
* To enable easy application of these measures on diverse datasets with minimal modification.
* To provide a foundation for enhancing data interpretation through quantitative effect size analysis.
* To create scalable scripts that can handle multiple variables and group comparisons automatically.

## Workflow

1. **Data Preparation:** Input data is preprocessed, ensuring relevant numerical and categorical variables are selected.
2. **Effect Size Computation:** Modular functions are used to compute effect sizes between variables or groups.
3. **Interpretation:** Outputs include both numerical effect size values and qualitative interpretations to aid understanding.
4. **Extensibility:** The scripts are designed to be reusable and adaptable to various datasets and research questions.

## Project Structure

```
effect_size_toolkit/
│
├── notebooks/                # Jupyter notebooks for exploration and demonstrations
│   └── effect_size_analysis.ipynb
│
├── scripts/                  # Python scripts with reusable functions and implementations
│   ├── cohens_d.py
│   ├── hedges_g.py
│   ├── correlation_effect_sizes.py
│   └── utils.py
│
├── data/                     # Sample or example datasets (optional)
│   └── example_dataset.csv
│
├── tests/                    # Unit tests for the effect size functions
│   └── test_effect_sizes.py
│
├── requirements.txt          # Python dependencies and package versions
├── README.md                 # Project overview and instructions (this file)
└── setup.py                  # Installation script (optional)
```

## Usage

### 1. Using the Notebook for Exploration

* Open the Jupyter notebook `notebooks/effect_size_analysis.ipynb` to interactively explore example datasets and see how the effect size functions work.
* The notebook includes step-by-step demonstrations on loading data, computing different effect sizes, and interpreting results.

### 2. Using the Python Scripts in Your Project

* Import the desired functions from the `scripts` folder into your Python environment.
* Prepare your dataset with relevant numerical and categorical columns.
* Call the effect size functions, specifying your dataset and grouping variables as needed.

Example:

```python
from scripts.cohens_d import compute_cohens_d
import pandas as pd

df = pd.read_csv('data/example_dataset.csv')

results = compute_cohens_d(df, numerical_columns=['var1', 'var2'], group_column='group')
print(results)
```

### 3. Installation and Dependencies

* Install required packages (example):

```bash
pip install -r requirements.txt
```

* The main dependencies include: `pandas`, `numpy`, `scipy`, `statsmodels`, `jupyter` (for notebook).

---

## Author


This analysis was performed by **Jabulente**, a passionate and dedicated data analyst with a strong commitment to using data to drive meaningful insights and solutions. For inquiries, collaborations, or further discussions, please feel free to reach out via.  

    
<div align="center">  
    
[![GitHub](https://img.shields.io/badge/GitHub-Jabulente-black?logo=github)](https://github.com/Jabulente)  [![LinkedIn](https://img.shields.io/badge/LinkedIn-Jabulente-blue?logo=linkedin)](https://linkedin.com/in/jabulente-208019349)  [![Email](https://img.shields.io/badge/Email-jabulente@hotmail.com-red?logo=gmail)](mailto:Jabulente@hotmail.com)  

</div>
