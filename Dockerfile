FROM python:3.8-slim-bullseye

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

#Create working directory
WORKDIR ~/converter

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the application:
COPY src/converter.py .
COPY src/utils.py .
ENTRYPOINT ["python3", "-u", "converter.py"]



