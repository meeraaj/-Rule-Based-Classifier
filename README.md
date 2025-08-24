# 🏦 Loan Approval Rule-Based Classifier  

## 📌 Project Overview  
This project implements a **rule-based classifier** to predict whether a loan application will be **Approved** or **Rejected** based on simple applicant features.  
Instead of using advanced machine learning models, this classifier uses **if-else logic rules**, making it beginner-friendly and easy to explain.  

---

## 📊 Dataset  
The dataset (`dataset.csv`) contains **10 rows** with the following features:  

- **Income** → High / Low  
- **Credit Score** → Good / Poor  
- **Employment Status** → Yes / No  
- **Approved** → Target variable (Approved / Rejected)  

**Example:**  

| Income | Credit | Employed | Approved |
|--------|--------|----------|----------|
| High   | Good   | Yes      | Approved |
| Low    | Poor   | No       | Rejected |
| High   | Poor   | Yes      | Approved |
| Low    | Good   | Yes      | Approved |

---

## ⚙️ Classifier Rules  
The loan decision is based on these simple rules:  

1. If **Income = High** and **Credit = Good** → Approved ✅  
2. If **Credit = Good** and **Employed = Yes** → Approved ✅  
3. If **Income = High** and **Employed = Yes** → Approved ✅  
4. Else → Rejected ❌  

---

## 🖥️ Features  
✔ Reads dataset and applies rule-based classifier  
✔ Evaluates model accuracy using **scikit-learn**  
✔ Confusion Matrix visualization with **matplotlib + seaborn**  
✔ **Real-time user input** for live predictions  

---

## 🚀 How to Run  

### 1. Clone Repository  
```bash
https://github.com/meeraaj/-Rule-Based-Classifier
