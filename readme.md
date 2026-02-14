# Portfolio Project with Custom Domain, SSL and Reverse Proxy

A personal DevOps portfolio website built with Flask, served via Gunicorn, reverse proxied through Nginx, secured with SSL, and accessible via a custom domain. The project demonstrates a production-grade deployment pattern on AWS EC2.

**Live site:** https://devron.cloud

---

## Project Overview

The portfolio is a single-page Flask application showcasing projects, technical skills, and certifications. Rather than using Flask's built-in development server, the app is served by Gunicorn — a production-grade WSGI server — with Nginx sitting in front as a reverse proxy. Traffic is encrypted via an SSL certificate issued by Let's Encrypt, and the site is accessible via a custom domain managed through AWS Route 53.

---

## Architecture & Stack

```
Browser → Nginx (port 443/HTTPS) → Gunicorn (port 5000) → Flask app
```

| Layer                      | Technology              |
| -------------------------- | ----------------------- |
| Cloud                      | AWS EC2, Route 53       |
| OS                         | Amazon Linux 2023       |
| Web Server / Reverse Proxy | Nginx                   |
| Application Server         | Gunicorn                |
| Web Framework              | Flask (Python)          |
| SSL                        | Let's Encrypt / Certbot |
| Domain Registrar           | Namecheap               |
| Version Control            | Git / GitHub            |

---

## EC2 & Nginx Setup

The application runs on an Amazon Linux 2023 EC2 instance. Nginx is installed and configured as a reverse proxy, forwarding incoming HTTP and HTTPS requests to Gunicorn on port 5000. The Nginx configuration lives in `/etc/nginx/sites-available/` and is activated via a symlink to `/etc/nginx/sites-enabled/`, following standard Nginx conventions.

The Nginx config handles two server blocks — one on port 80 that redirects all HTTP traffic to HTTPS, and one on port 443 that terminates SSL and proxies requests through to Gunicorn:

```nginx
server {
    listen 80;
    server_name devron.cloud;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name devron.cloud;

    ssl_certificate /etc/letsencrypt/live/devron.cloud/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/devron.cloud/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

---

## Gunicorn & Flask

The Flask application is served by Gunicorn, which is configured to run as a systemd service so it starts automatically on boot and restarts if it crashes. The service binds Gunicorn to `127.0.0.1:5000`, making it accessible only internally — Nginx is the only entry point for external traffic.

The systemd service file at `/etc/systemd/system/portfolio.service` manages the Gunicorn process:

```ini
[Unit]
Description=Gunicorn instance to serve portfolio Flask app
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/home/ec2-user/Portfolio_with_ssl_and_reverse_proxy
ExecStart=/home/ec2-user/.local/bin/gunicorn --bind 127.0.0.1:5000 app:app

[Install]
WantedBy=multi-user.target
```

Dependencies are managed via `requirements.txt` and installed with:

```bash
pip3 install -r requirements.txt
```

---

## DNS with Route 53

The custom domain `devron.cloud` was registered through Namecheap. DNS management was delegated to AWS Route 53 by replacing Namecheap's default nameservers with the four Route 53 nameservers assigned to the hosted zone. An A record was created in Route 53 pointing the domain to the EC2 instance's public IP address.

---

## SSL with Certbot & Let's Encrypt

HTTPS is enabled using a free SSL certificate issued by Let's Encrypt via Certbot. The `python3-certbot-nginx` plugin was used to handle certificate issuance and automatically update the Nginx configuration to serve traffic over port 443. The systemd renewal timer is enabled to automatically renew the certificate before its 90-day expiry:

```bash
sudo systemctl enable certbot-renew.timer
```

---

## Git Workflow

The project follows a local → GitHub → EC2 deployment workflow. All changes are made and tested locally, committed and pushed to GitHub, then pulled onto the EC2 instance. This keeps the server as a clean deployment target and ensures GitHub remains the single source of truth for the codebase.

```
local machine → GitHub → EC2 instance
```

The EC2 instance authenticates with GitHub via an SSH key pair, with the public key added to the GitHub account.

---

## How to Deploy

To recreate this project from scratch:

**1. Clone the repo onto your EC2 instance:**

```bash
git clone git@github.com:devrontombacco/Portfolio_with_ssl_and_reverse_proxy.git
cd Portfolio_with_ssl_and_reverse_proxy
```

**2. Install dependencies:**

```bash
pip3 install -r requirements.txt
```

**3. Set up the Gunicorn systemd service:**

```bash
sudo cp portfolio.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start portfolio
sudo systemctl enable portfolio
```

**4. Set up Nginx:**

```bash
sudo cp nginx.conf /etc/nginx/sites-available/portfolio
sudo ln -s /etc/nginx/sites-available/portfolio /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

**5. Issue SSL certificate:**

```bash
sudo certbot --nginx -d your-domain.com
sudo systemctl enable certbot-renew.timer
```
