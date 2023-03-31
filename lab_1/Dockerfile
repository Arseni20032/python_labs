FROM python:3

COPY requirements.txt .
COPY main.py .
COPY task_1.py .
COPY task_2.py .
COPY task_3.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]

