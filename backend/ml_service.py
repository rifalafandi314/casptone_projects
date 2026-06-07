import joblib
import pandas as pd
from pathlib import Path

# =========================
# PATH
# =========================
BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"

# =========================
# GLOBAL ARTIFACTS
# =========================
ARTIFACTS = {
    "stress": {},
    "anxiety": {},
    "depression": {}
}

# =========================
# LOAD MODEL
# =========================
def load_all_artifacts():
    """Load semua model saat server start"""

    conditions = ["stress", "anxiety", "depression"]

    for cond in conditions:

        model_path = MODELS_DIR / f"model_{cond}.pkl"
        pre_path = MODELS_DIR / f"preprocessor_{cond}.pkl"
        label_path = MODELS_DIR / f"label_encoder_{cond}.pkl"

        if not model_path.exists():
            raise FileNotFoundError(f"Tidak ditemukan: {model_path}")

        if not pre_path.exists():
            raise FileNotFoundError(f"Tidak ditemukan: {pre_path}")

        if not label_path.exists():
            raise FileNotFoundError(f"Tidak ditemukan: {label_path}")

        try:
            ARTIFACTS[cond]["model"] = joblib.load(model_path)
            ARTIFACTS[cond]["preprocessor"] = joblib.load(pre_path)
            ARTIFACTS[cond]["label_encoder"] = joblib.load(label_path)

            print(f"[OK] {cond.upper()} loaded")

        except Exception as e:
            raise RuntimeError(f"Gagal load model {cond}: {e}")

# Auto-load saat import
load_all_artifacts()

# =========================
# SINGLE PREDICTION
# =========================
def get_single_prediction(condition, df_subset):

    if condition not in ARTIFACTS or not ARTIFACTS[condition]:
        raise RuntimeError(f"Model {condition} belum ter-load")

    preprocessor = ARTIFACTS[condition]["preprocessor"]
    model = ARTIFACTS[condition]["model"]
    label_encoder = ARTIFACTS[condition]["label_encoder"]

    X_processed = preprocessor.transform(df_subset)

    pred_encoded = model.predict(X_processed)[0]
    pred_label = label_encoder.inverse_transform([pred_encoded])[0]

    return {
        "prediction": str(pred_label)
    }

# =========================
# MAIN PREDICTION
# =========================
def predict_all_conditions(input_data: dict):

    df = pd.DataFrame([input_data])

    demographics = [
        "Age",
        "Gender",
        "University",
        "Department",
        "Academic_Year",
        "CGPA",
        "Scholarship"
    ]

    stress_cols = demographics + [f"Q{i}" for i in range(1, 11)]
    anxiety_cols = demographics + [f"AQ{i}" for i in range(1, 8)]
    depression_cols = demographics + [f"DQ{i}" for i in range(1, 10)]

    return {
        "stress": get_single_prediction("stress", df[stress_cols]),
        "anxiety": get_single_prediction("anxiety", df[anxiety_cols]),
        "depression": get_single_prediction("depression", df[depression_cols])
    }