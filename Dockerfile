FROM nginx:alpine

# Nginx config (Mode A: HTTP 80, CF Proxy ON)
# File at repo root — Coolify mount compatibility
COPY nginx-http.conf /etc/nginx/conf.d/default.conf

# Site dosyalarını kopyala (yalnızca gerekli olanlar)
COPY index.html styles.css script.js /usr/share/nginx/html/
COPY account-delete.html /usr/share/nginx/html/
COPY sitemap.xml robots.txt ads.txt app-ads.txt /usr/share/nginx/html/
COPY images/ /usr/share/nginx/html/images/
COPY blog/ /usr/share/nginx/html/blog/
COPY legal/ /usr/share/nginx/html/legal/
COPY .well-known/ /usr/share/nginx/html/.well-known/

# Nginx varsayılan dosyalarını temizle
RUN rm -f /usr/share/nginx/html/index.html.orig \
    /usr/share/nginx/html/50x.html

# Nginx kullanıcısı ile çalış (root değil)
RUN chown -R nginx:nginx /usr/share/nginx/html \
    && chown -R nginx:nginx /var/cache/nginx \
    && chown -R nginx:nginx /var/log/nginx \
    && touch /var/run/nginx.pid \
    && chown nginx:nginx /var/run/nginx.pid

USER nginx

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD wget -q --spider http://localhost/health || exit 1

CMD ["nginx", "-g", "daemon off;"]
