import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def create_dataset(data, step=10):
    X, y = [], []
    for i in range(len(data) - step):
        X.append(data[i:i+step])
        y.append(data[i+step])
    return np.array(X), np.array(y)

def train_and_save_model(data, name):
    X, y = create_dataset(data)
    model = RandomForestRegressor()
    model.fit(X, y)
    os.makedirs("ai_models", exist_ok=True)
    joblib.dump(model, f"ai_models/{name}.pkl")
    print(f"{name}.pkl modeli saqlandi.")

# --- Ma'lumotlar ---
aviator_1win = [
    1.59, 1.58, 1.32, 63.96, 6.89, 1.56, 4.48, 2.20, 2.14, 17.47, 1.26, 2.22, 2.56, 1.83, 3.20, 2.08,
    2.78, 1.60, 2.58, 7.46, 1.26, 7.08, 5.06, 94.01, 4.65, 1.08, 1.12, 1.99, 1.59, 2.02, 2.95, 21.92,
    2.20, 1.69, 1.06, 4.28, 10.16, 3.84, 2.02, 1.10, 1.42, 1.59, 2.60, 2.49, 1.16, 1.59, 1.58, 1.32,
    63.96, 6.89, 1.56, 4.48, 2.20, 2.14, 17.47
]

luckyjet_1win = [
    2.02, 9.56, 5.11, 1.57, 2.44, 11.40, 18.36, 1.08, 3.17, 1.85,
    1.47, 1.00, 1.15, 2.09, 1.00, 4.19, 1.09, 1.13, 1.68, 1.00
]

aviator_mostbet = [
    2.53, 1.19, 1.60, 1.47, 1.31, 1.62, 2.71, 2.11, 1.08, 9.72, 1.30, 8.10,
    1.98, 1.19, 2.38, 4.40, 1.38, 3.55, 27.04, 3.02, 1.52, 1.20, 1.76, 9.50,
    1.53, 1.33, 8.11, 1.06, 2.53, 1.19, 1.60, 1.47, 1.31, 1.62, 2.71, 2.11,
    1.08, 9.72, 1.30, 8.10, 1.98, 1.19, 2.38, 1.38, 3.55, 27.04, 3.02, 1.52,
    1.20, 1.76, 1.53, 4.40, 9.50, 1.33
]

# --- Modellarni o‘qitish ---
train_and_save_model(aviator_1win, "aviator_1win")
train_and_save_model(luckyjet_1win, "luckyjet_1win")
train_and_save_model(aviator_mostbet, "aviator_mostbet")
