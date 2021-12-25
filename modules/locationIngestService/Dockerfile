FROM python:3.7-alpine

WORKDIR .
RUN apk add --no-cache \
  # required by grpc
  g++ \
  musl-dev \
  libffi-dev

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5005

COPY . .
CMD ["python3", "main.py"]