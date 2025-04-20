import numpy as np
import joblib

def create_dataset(data, step=10):
    X = []
    for i in range(len(data) - step):
        X.append(data[i:i+step])
    return np.array(X)

def predict_next_value(model_path, recent_data):
    model = joblib.load(model_path)
    X = create_dataset(recent_data[-10:])[0] 
create_dataset(recent_data[-10:])
 if len(X) == 0:
        return None
    prediction = model.predict(X)
    return round(float(prediction[-1]), 
2)

# Misol uchun test:
if __name__ == "__main__":
    recent_data = [1.53, 2.44, 1.57, 5.11, 9.56, 2.02, 1.68, 1.13, 1.09, 4.19]
    model_name = "ai_models/aviator_1win.pkl"
    result = predict_next_value(model_name, recent_data)
    print("Keyingi bashorat:", result)
