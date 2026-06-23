FROM nginx:alpine

# Google Analytics 4 — build-time substitute (Coolify env: GA4_MEASUREMENT_ID)
# Default değer: G-PLJEZCGT27BU (senin ölçüm ID'n). Coolify'da env ile override et.
ARG GA4_MEASUREMENT_ID=G-PLJEZCGT27BU

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

# Build arg → index.html inject (sed)
RUN if [ -n "$GA4_MEASUREMENT_ID" ]; then \
      sed -i "s|__GA4_ID__|${GA4_MEASUREMENT_ID}|g" /usr/share/nginx/html/index.html && \
      echo "GA4 ID injected: ${GA4_MEASUREMENT_ID}"; \
    fi

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
