import os
import pickle
import torch

from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification
)

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "mental_health_model"
)

print("MODEL PATH:", MODEL_PATH)

device = torch.device("cpu")

tokenizer = DistilBertTokenizerFast.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

model = DistilBertForSequenceClassification.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

model.to(device)

model.eval()

with open(
    os.path.join(MODEL_PATH, "label_encoder.pkl"),
    "rb"
) as f:

    label_encoder = pickle.load(f)