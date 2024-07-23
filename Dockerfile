FROM python:3

WORKDIR /etl

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./etl .

CMD [ "python", "./etl.py" ]