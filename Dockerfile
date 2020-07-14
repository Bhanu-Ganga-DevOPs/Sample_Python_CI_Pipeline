FROM python:3.7.5

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

RUN useradd --create-home a_user
WORKDIR /home/a_user
USER a_user

COPY sample_package/ sample_package/
COPY test/ test/
COPY pytest.ini .

ENV PYTHONPATH "${PYTHONPATH}:/home/a_user"
