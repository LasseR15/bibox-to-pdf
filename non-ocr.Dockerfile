FROM python:3-alpine

LABEL maintainer=LasseR15
LABEL email=lasse.roth@lasse-it.de


COPY /src /app/src
COPY /requirements-non-ocr.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt


RUN python -m playwright install-deps chromium
RUN python -m playwright install chromium

ENV PYTHONPATH=/app/src/
ENV BASE_OUTPUT_PATH=/app/output

ENTRYPOINT ["python3", "/app/src/main.py", "--no-ocr"]
