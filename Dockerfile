FROM python:3.6

RUN pip install --upgrade pip
WORKDIR /usr/src/app
COPY ./requirements*.txt ./
RUN pip install --no-cache-dir -r requirements_prod.txt
COPY . .
RUN python manage.py collectstatic --no-input
