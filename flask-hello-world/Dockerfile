FROM alpine
ENV http_proxy=$http_proxy
ENV https_proxy=$https_proxy
RUN echo $http_proxy
RUN apk update
RUN apk add --update py-pip
RUN pip install flask
COPY app.py .
WORKDIR .
EXPOSE 5050
ENTRYPOINT python app.py
