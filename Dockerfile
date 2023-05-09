FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE 1 #запрещает Python записывать файлы pyc на диск
ENV PYTHONUNBUFFERED 1 #запрещает Python буферизовать stdout и stderr

WORKDIR /app

RUN python -m pip install --upgrade pip && \
    apt update && \
#    apt install python3-dev default-libmysqlclient-dev build-essential -y && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app
CMD ["python", "./main.py", "Приложение_к_заданию_бек_разработчика.xlsx"]
