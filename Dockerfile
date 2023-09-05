FROM python:3.10
WORKDIR /app
EXPOSE 8000
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./app /app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]