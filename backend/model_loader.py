import pickle
import tempfile
import torch

from huggingface_hub import snapshot_download
from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification
)

MODEL_NAME = "rifal742/mental_health"

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

repo_path = snapshot_download(
    repo_id=MODEL_NAME
)

MODEL_PATH = f"{repo_path}/mental_health_model"

tokenizer = DistilBertTokenizerFast.from_pretrained(
    MODEL_PATH
)

model = DistilBertForSequenceClassification.from_pretrained(
    MODEL_PATH
)

with open(
    f"{MODEL_PATH}/label_encoder.pkl",
    "rb"
) as f:
    label_encoder = pickle.load(f)

model.to(device)
model.eval()

print("Model loaded successfully")