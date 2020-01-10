FROM python:3.6
RUN mkdir -p /usr/src/app
COPY .. /usr/src/app
WORKDIR /usr/src/app/mydemo/
RUN pip install -r /usr/src/app/mydemo/requirements.txt
EXPOSE 8000
CMD ["/bin/sh","run.sh"]
