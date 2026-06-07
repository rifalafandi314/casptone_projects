import re
import torch
import torch.nn.functional as F

from model_loader import (
    tokenizer,
    model,
    label_encoder,
    device
)

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"www\S+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def predict_text(text):

    cleaned_text = clean_text(text)

    inputs = tokenizer(
        cleaned_text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=256
    )

    inputs = {
        k: v.to(device)
        for k, v in inputs.items()
    }

    with torch.no_grad():
        outputs = model(**inputs)
        probs = F.softmax(outputs.logits, dim=1)

    probs = probs.cpu().numpy()[0]

    top2_idx = probs.argsort()[-2:][::-1]

    labels = label_encoder.inverse_transform(top2_idx)

    return {
        "prediction": labels[0],
        "confidence": float(probs[top2_idx[0]]),
        "top2": [
            {
                "label": labels[0],
                "score": float(probs[top2_idx[0]])
            },
            {
                "label": labels[1],
                "score": float(probs[top2_idx[1]])
            }
        ]
    }