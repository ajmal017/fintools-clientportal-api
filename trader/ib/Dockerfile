FROM python:3.6
ADD requirements.txt /
RUN pip install -r requirements.txt
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["app.py"]
