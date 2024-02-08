FROM tiangolo/uvicorn-gunicorn:python3.11-slim
ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages
WORKDIR /app
ADD . /app
RUN pip install --no-cache-dir bson==0.5.9
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x run.sh
CMD ["./run.sh"]