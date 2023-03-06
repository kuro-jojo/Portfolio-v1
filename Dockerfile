FROM python:3.9

WORKDIR /app
ENV PORT=5000

COPY requirements.txt .

RUN python -m venv venv
RUN . venv/bin/activate

RUN pip install -r requirements.txt

COPY . /app

CMD gunicorn --bind 0.0.0.0:$PORT app:app --log-level "debug" --preload