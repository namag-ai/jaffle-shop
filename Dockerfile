FROM python:3.12

WORKDIR /etl
# SETUP SOFTWARE

ARG NIDAQMX_INSTALL_VER=ni-ubuntu2204-drivers-2023Q3

RUN apt update

RUN apt purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false

RUN apt clean -y && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install psycopg2
RUN pip3 install -v --no-cache-dir -r requirements.txt
RUN pip freeze > ./test.txt

COPY ./etl .

CMD [ "python", "./etl.py" ]