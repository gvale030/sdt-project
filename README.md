# 🚗 Car Dashboard App

An interactive dashboard built with Streamlit that visualizes used car advertisement data in the U.S. The app helps explore trends in pricing, mileage, and other vehicle attributes through interactive charts.

---

## 📦 Dataset

The dataset contains listings for used vehicles in the U.S. It includes features such as:

- `model`
- `model_year`
- `price`
- `odometer`
- `paint_color`
- `condition`
- `is_4WD`
- `cylinders`
- `transmission`

The dataset is preloaded in the app and does not require user upload.

---

## ⚙️ Features of the App

- ✅ Automatically loads and displays the vehicle dataset
- 📊 Visualizes trends with histogram and scatter plots
- 🔎 Allows selection of columns for interactive analysis
- 🧼 Performs basic cleaning and data preview

---

## 🧪 How to Run the App Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gvale030/sdt-project.git
cd sdt-project
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py


⚙️ Features of the App:

- Automatically loads vehicle dataset
- Visualizes pricing trends with scatter and bar plots
- Filters by model year, paint color, and condition