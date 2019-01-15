FROM sunilkhokalay/alpine-python-flask
COPY app.py .
RUN mkdir templates
COPY templates/* templates 
WORKDIR .
EXPOSE 5050
ENTRYPOINT python app.py
