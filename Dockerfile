FROM nginx:alpine

# Nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Site dosyalarını kopyala
COPY . /usr/share/nginx/html

# Gereksiz dosyaları sil
RUN rm -f /usr/share/nginx/html/Dockerfile \
    /usr/share/nginx/html/nginx.conf \
    /usr/share/nginx/html/vercel.json \
    /usr/share/nginx/html/*.md \
    /usr/share/nginx/html/*.ps1 \
    /usr/share/nginx/html/*.sh

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
