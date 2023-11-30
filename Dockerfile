# Build stage
FROM python:3.11 AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.11
WORKDIR /project
COPY --from=builder /build /project
COPY . /project
RUN pip install --upgrade pip && \
    pip install gunicorn && \
    pip install -r requirements.txt
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project.wsgi:application"]