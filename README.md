# 🏥 Clinical Decision Making & Pattern Recognition in Healthcare

## Patient Readmission Risk Predictor

**Author:** Ramesh Tare  
**College:** D Y Patil College of Engineering, Pune | University of Pune  
**Date:** August 5, 2026  
**Topic:** Clinical Decision Making and Pattern Recognition in Healthcare  
**Submitted to:** Cotiviti Intern Assessment

---

## 📌 Project Overview

This project demonstrates the application of machine learning and deep learning techniques to predict 30-day hospital readmission risk, supporting clinical decision-making with interpretable results. The project was developed as part of the Cotiviti Intern Assessment.

### Key Features
- ✅ **3 ML Models**: Random Forest, XGBoost, Deep Learning
- ✅ **Real Data**: 120,000 patient admissions from India hospital dataset
- ✅ **Web Application**: Interactive Streamlit dashboard
- ✅ **Clinical Interpretation**: Feature importance and clinical recommendations
- ✅ **Model Comparison**: Comprehensive performance analysis

---

## 🏆 Best Performing Model: Deep Learning

| Metric | Random Forest | XGBoost | Deep Learning |
|--------|---------------|---------|---------------|
| ROC-AUC | 0.735 | 0.729 | **0.736** |
| Accuracy | 70.0% | 70.5% | **88.3%** |
| Precision (Weighted) | 85.2% | 85.0% | **88.3%** |
| Recall (Weighted) | 70.0% | 70.5% | **88.3%** |
| F1-Score (Weighted) | 75.0% | 75.4% | **88.3%** |
| Training Time | 4.5s | 2.0s | 298.9s |

---

## 📊 Key Clinical Findings

| Feature | Importance | Clinical Significance | Impact |
|---------|------------|----------------------|--------|
| **Length of Stay (LOS)** | **34.0%** | Longer stays indicate clinical complexity | High-risk patients stay **60.3% longer** |
| **Charlson Index** | **21.6%** | Burden of chronic conditions | High-risk patients have **55.9% higher** burden |
| **Age** | **15.6%** | Age-related vulnerability | High-risk patients average **57.3 years** (vs 46.8 years) |
| **Procedures** | **10.5%** | Intervention intensity | High-risk patients have **51.5% more** procedures |
| **Haemoglobin** | **7.4%** | Anemia status | Lower hemoglobin associated with **higher risk** (-7.4%) |

### High Risk vs Low Risk Patient Comparison
- **Length of Stay:** +60.3% in high-risk patients
- **Charlson Index:** +55.9% in high-risk patients
- **Age:** +22.4% in high-risk patients
- **Haemoglobin:** -7.4% in high-risk patients (anemia)

---

## 🚀 Quick Start

### 1. Clone the Repository

git clone https://github.com/RLT1124/-Clinical_Decision_Making_POC.git
cd -Clinical_Decision_Making_POC


## 🔗 Links

- **GitHub Repository:** https://github.com/RLT1124/-Clinical_Decision_Making_POC
- **Video Recording:** [Watch the Demonstration Video](https://drive.google.com/file/d/16xXUxJQH_dTucjWtD-bxz9YgyV1MD1mj/view)
