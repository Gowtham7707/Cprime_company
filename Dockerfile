FROM python:3.9-slim
WORKDIR /Cprime
COPY requirements.txt /Cprime/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /Cprime/
EXPOSE 8000
CMD ["python","FaskApi.py"]