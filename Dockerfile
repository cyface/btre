FROM python:3.6

WORKDIR /usr/src/app
COPY . .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements_prod.txt
RUN python manage.py collectstatic --no-input
