FROM python:3.10

# create user (WAJIB untuk HF Spaces best practice)
RUN useradd -m -u 1000 user
USER user

ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

# copy backend
COPY --chown=user backend/ backend/

# upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# install dependencies
RUN pip install --no-cache-dir -r backend/requirement.txt

# HF wajib port 7860
EXPOSE 7860

# jalankan FastAPI
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "7860"]