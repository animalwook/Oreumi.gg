FROM nginx:latest

RUN apt-get -y update
RUN apt-get -y install vim

RUN mkdir /etc/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
COPY html/ /etc/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]