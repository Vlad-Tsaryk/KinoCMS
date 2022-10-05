FROM nginx:latest
#COPY default.conf /etc/nginx
#COPY default.conf /etc/nginx/nginx.conf
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
RUN mkdir -p /home/app/staticfiles