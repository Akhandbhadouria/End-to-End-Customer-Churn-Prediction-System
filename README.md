# End-to-End Customer Churn Prediction & Retention System

🚀 A production-ready machine learning system to predict customer churn using advanced ensemble models, deployed via API and visualized through business dashboards.

## 🔥 Overview
This project builds a complete pipeline to:
* **Predict** customer churn using XGBoost & LightGBM
* **Optimize** performance using Optuna
* **Serve** predictions via a FastAPI REST API
* **Deploy** using Docker on AWS
* **Visualize** insights with Power BI

## ⚙️ Tech Stack
* **ML:** XGBoost, LightGBM, Scikit-learn
* **Backend:** FastAPI
* **Optimization:** Optuna
* **Data:** Pandas, NumPy
* **Deployment:** Docker, AWS EC2
* **Visualization:** Power BI

## 📁 Project Structure
```text
ML_final_project/
├── Bank_Churn.csv          # Raw dataset
├── requirements.txt        # Python dependencies
├── XG_boost.ipynb          # Model training & optimization script
├── models/
│   └── churn_model.pkl     # Trained & serialized ML model
└── app/                    # Web Application layer
    ├── index.html          # Frontend User Interface
    ├── main.py             # API Backend & Server logic
    ├── model_loader.py     # Utility to load the model
    └── schema.py           # Data validation definitions
```

## 🧠 How It Works (Execution Flow)
1. **User Input (UI)**: Enter details in the web interface.
2. **FastAPI (Validation)**: Pydantic ensures data integrity.
3. **Preprocessing**: `ColumnTransformer` handles categorical encoding.
4. **Model (XGBoost/LGBM)**: The ensemble model processes features.
5. **Prediction**: Returns churn probability and decision.
6. **Response**: UI displays results (**CHURNED** or **NOT CHURNED**).

## 📌 Features
✔ End-to-end ML pipeline  
✔ Handles imbalanced data (PR-AUC optimization)  
✔ Real-time prediction via API  
✔ Interactive frontend (HTML + JS)  
✔ Containerized deployment (Docker)  
✔ Cloud-ready (AWS EC2)  
✔ Business insights via dashboard  

## 🚀 Getting Started

### 1. Clone Repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run FastAPI Server
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 4. Access API Docs
Visit [http://localhost:8000/docs](http://localhost:8000/docs)

## 🐳 Docker Setup
### Build Image
```bash
docker build -t churn-api .
```
### Run Container
```bash
docker run -p 8000:8000 churn-api
```

## ☁️ AWS Deployment
1. Launch **EC2 instance**
2. Install **Docker**
3. Clone repo and build/run container
4. Open **port 8000** in Security Groups
5. Access: `http://<EC2-PUBLIC-IP>:8000/`

## 📊 Power BI Dashboard
* Churn rate by geography
* Customer segmentation
* Key churn drivers
* Risk distribution

## 📡 API Example
**Endpoint:** `POST /predict`

**Sample Request:**
```json
{
  "CreditScore": 600,
  "Geography": "France",
  "Gender": "Male",
  "Age": 40,
  "Tenure": 3,
  "Balance": 60000,
  "NumOfProducts": 2,
  "HasCrCard": 1,
  "IsActiveMember": 1,
  "EstimatedSalary": 50000
}
```

**Response:**
```json
{
  "churn_probability": 0.82,
  "prediction": 1
}
```

## 👨‍💻 Author
**Akhand Pratap Singh**  
*Aspiring ML Engineer | Backend Developer*
