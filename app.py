from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Devron Tombacco | DevOps Engineer</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #2563eb;
            --primary-dark: #1d4ed8;
            --secondary: #64748b;
            --background: #0f172a;
            --surface: #1e293b;
            --surface-light: #334155;
            --text: #f8fafc;
            --text-muted: #94a3b8;
            --accent: #22d3ee;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            background-color: var(--background);
            color: var(--text);
            line-height: 1.6;
        }

        header {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(10px);
            z-index: 1000;
            border-bottom: 1px solid var(--surface-light);
        }

        nav {
            max-width: 1200px;
            margin: 0 auto;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--accent);
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        nav a {
            color: var(--text-muted);
            text-decoration: none;
            transition: color 0.3s;
        }

        nav a:hover {
            color: var(--accent);
        }

        main {
            padding-top: 70px;
        }

        section {
            padding: 5rem 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        h2 {
            font-size: 2.5rem;
            margin-bottom: 2rem;
            color: var(--text);
            text-align: center;
        }

        #hero {
            min-height: calc(100vh - 70px);
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            background: linear-gradient(135deg, var(--background) 0%, var(--surface) 100%);
        }

        .hero-content h1 {
            font-size: 4rem;
            margin-bottom: 1rem;
            background: linear-gradient(90deg, var(--text), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .tagline {
            font-size: 1.5rem;
            color: var(--text-muted);
            margin-bottom: 1rem;
        }

        .quote {
            font-style: italic;
            color: var(--accent);
            margin-bottom: 2rem;
            font-size: 1.1rem;
        }

        .cta-buttons {
            display: flex;
            gap: 1rem;
            justify-content: center;
        }

        .btn {
            padding: 0.875rem 2rem;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s;
        }

        .btn.primary {
            background: var(--primary);
            color: var(--text);
        }

        .btn.primary:hover {
            background: var(--primary-dark);
        }

        .btn.secondary {
            border: 2px solid var(--primary);
            color: var(--primary);
        }

        .btn.secondary:hover {
            background: var(--primary);
            color: var(--text);
        }

        #about {
            background: var(--surface);
            border-radius: 16px;
            margin: 2rem auto;
        }

        .about-content p {
            font-size: 1.1rem;
            color: var(--text-muted);
            margin-bottom: 1rem;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
            text-align: center;
        }

        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
        }

        .skill-card {
            background: var(--surface);
            padding: 2rem;
            border-radius: 12px;
            border: 1px solid var(--surface-light);
            transition: transform 0.3s, border-color 0.3s;
        }

        .skill-card:hover {
            transform: translateY(-5px);
            border-color: var(--accent);
        }

        .skill-card h3 {
            color: var(--accent);
            margin-bottom: 1rem;
            font-size: 1.2rem;
        }

        .skill-card ul {
            list-style: none;
        }

        .skill-card li {
            color: var(--text-muted);
            padding: 0.5rem 0;
            border-bottom: 1px solid var(--surface-light);
        }

        .skill-card li:last-child {
            border-bottom: none;
        }

        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 1.5rem;
        }

        .project-card {
            background: var(--surface);
            padding: 2rem;
            border-radius: 12px;
            border: 1px solid var(--surface-light);
            transition: transform 0.3s, border-color 0.3s;
        }

        .project-card:hover {
            transform: translateY(-5px);
            border-color: var(--primary);
        }

        .project-card h3 {
            color: var(--text);
            margin-bottom: 1rem;
        }

        .project-card p {
            color: var(--text-muted);
            margin-bottom: 1rem;
        }

        .tech-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }

        .tech-tags span {
            background: var(--surface-light);
            color: var(--accent);
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.85rem;
        }

        .certs-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
        }

        .cert-card {
            background: var(--surface);
            padding: 2rem;
            border-radius: 12px;
            text-align: center;
            border: 1px solid var(--surface-light);
            transition: transform 0.3s;
        }

        .cert-card:hover {
            transform: translateY(-5px);
        }

        .cert-badge {
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1rem;
            font-weight: bold;
            font-size: 1.2rem;
        }

        .cert-card h3 {
            color: var(--text);
            margin-bottom: 0.5rem;
        }

        .cert-card p {
            color: var(--text-muted);
        }

        #contact {
            text-align: center;
        }

        .contact-content p {
            color: var(--text-muted);
            margin-bottom: 2rem;
            font-size: 1.1rem;
        }

        .contact-links {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 1rem;
        }

        .contact-item {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            background: var(--surface);
            padding: 1rem 1.5rem;
            border-radius: 8px;
            text-decoration: none;
            color: var(--text);
            border: 1px solid var(--surface-light);
            transition: all 0.3s;
        }

        .contact-item:hover {
            border-color: var(--accent);
            transform: translateY(-3px);
        }

        .contact-item .icon {
            width: 40px;
            height: 40px;
            background: var(--primary);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 0.9rem;
        }

        footer {
            background: var(--surface);
            padding: 2rem;
            text-align: center;
            color: var(--text-muted);
            border-top: 1px solid var(--surface-light);
        }

        @media (max-width: 768px) {
            nav ul {
                display: none;
            }

            .hero-content h1 {
                font-size: 2.5rem;
            }

            .tagline {
                font-size: 1.2rem;
            }

            .cta-buttons {
                flex-direction: column;
                align-items: center;
            }

            .projects-grid {
                grid-template-columns: 1fr;
            }

            section {
                padding: 3rem 1rem;
            }
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <div class="logo">DT</div>
            <ul>
                <li><a href="#about">About</a></li>
                <li><a href="#skills">Skills</a></li>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#certifications">Certifications</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="hero">
            <div class="hero-content">
                <h1>Devron Tombacco</h1>
                <p class="tagline">DevOps Engineer | Cloud Architect | AWS Specialist</p>
                <p class="quote">"Every architectural decision is a tradeoff"</p>
                <div class="cta-buttons">
                    <a href="#projects" class="btn primary">View Projects</a>
                    <a href="#contact" class="btn secondary">Get in Touch</a>
                </div>
            </div>
        </section>

        <section id="about">
            <h2>About Me</h2>
            <div class="about-content">
                <p>
                    I'm an experienced, certified cloud engineer specializing in networking, system design,
                    and cloud-native architecture. With a background in software engineering (web + iOS),
                    network engineering, and tech support, I bring a comprehensive understanding of the
                    full technology stack.
                </p>
                <p>
                    Currently focusing on DevOps pipelines and AWS infrastructure with emphasis on networking.
                    I believe in balancing performance, security, and reliability in every infrastructure decision.
                </p>
            </div>
        </section>

        <section id="skills">
            <h2>Technical Skills</h2>
            <div class="skills-grid">
                <div class="skill-card">
                    <h3>Cloud Platform</h3>
                    <ul>
                        <li>AWS EC2, VPC, S3, RDS</li>
                        <li>IAM, Lambda, CloudWatch</li>
                        <li>WAF, Route53, ACM</li>
                    </ul>
                </div>
                <div class="skill-card">
                    <h3>Networking</h3>
                    <ul>
                        <li>VPC Peering</li>
                        <li>Transit Gateways</li>
                        <li>Site-to-Site VPN</li>
                        <li>Security Groups & NACLs</li>
                    </ul>
                </div>
                <div class="skill-card">
                    <h3>Infrastructure as Code</h3>
                    <ul>
                        <li>Terraform</li>
                        <li>Ansible</li>
                        <li>CloudFormation</li>
                    </ul>
                </div>
                <div class="skill-card">
                    <h3>CI/CD & DevOps</h3>
                    <ul>
                        <li>Jenkins</li>
                        <li>GitHub Actions</li>
                        <li>Docker</li>
                        <li>Git/GitHub/GitLab</li>
                    </ul>
                </div>
                <div class="skill-card">
                    <h3>Systems</h3>
                    <ul>
                        <li>Linux/Ubuntu Administration</li>
                        <li>SSH/RSA Key Authentication</li>
                        <li>DNS Management</li>
                    </ul>
                </div>
            </div>
        </section>

        <section id="projects">
            <h2>Featured Projects</h2>
            <div class="projects-grid">
                <div class="project-card">
                    <h3>Dual Region Transit Gateway Peering</h3>
                    <p>Multi-region AWS infrastructure with Terraform and Ansible automation for high availability across regions.</p>
                    <div class="tech-tags">
                        <span>Terraform</span>
                        <span>Ansible</span>
                        <span>AWS</span>
                    </div>
                </div>
                <div class="project-card">
                    <h3>Multi-VPC Transit Gateway with Site-to-Site VPN</h3>
                    <p>Production-grade architecture connecting multiple VPCs via Transit Gateway with IPsec VPN connectivity.</p>
                    <div class="tech-tags">
                        <span>Transit Gateway</span>
                        <span>VPN</span>
                        <span>StrongSwan</span>
                    </div>
                </div>
                <div class="project-card">
                    <h3>Blue/Green Deployment Architecture</h3>
                    <p>Zero-downtime deployment setup using ALB, EC2, RDS Proxy, and dual RDS instances for seamless updates.</p>
                    <div class="tech-tags">
                        <span>ALB</span>
                        <span>RDS Proxy</span>
                        <span>EC2</span>
                    </div>
                </div>
                <div class="project-card">
                    <h3>Scalable Web App with WAF</h3>
                    <p>Complete stack featuring Application Load Balancer, Auto Scaling Group, and Web Application Firewall protection.</p>
                    <div class="tech-tags">
                        <span>WAF</span>
                        <span>ALB</span>
                        <span>ASG</span>
                    </div>
                </div>
                <div class="project-card">
                    <h3>Secure Bastion Architecture</h3>
                    <p>Private infrastructure access via bastion host with restricted security groups for enhanced security.</p>
                    <div class="tech-tags">
                        <span>Bastion</span>
                        <span>Security Groups</span>
                        <span>VPC</span>
                    </div>
                </div>
                <div class="project-card">
                    <h3>Static Blog with CI/CD Pipeline</h3>
                    <p>Automated static blog deployment leveraging S3, CloudFront, ACM, and GitHub Actions for continuous delivery.</p>
                    <div class="tech-tags">
                        <span>S3</span>
                        <span>CloudFront</span>
                        <span>GitHub Actions</span>
                    </div>
                </div>
            </div>
        </section>

        <section id="certifications">
            <h2>Certifications</h2>
            <div class="certs-grid">
                <div class="cert-card">
                    <div class="cert-badge">CCNA</div>
                    <h3>Cisco Certified Network Associate</h3>
                    <p>March 2024</p>
                </div>
                <div class="cert-card">
                    <div class="cert-badge">AWS</div>
                    <h3>AWS Cloud Practitioner</h3>
                    <p>March 2025</p>
                </div>
                <div class="cert-card">
                    <div class="cert-badge">TF</div>
                    <h3>Terraform Associate (003)</h3>
                    <p>August 2025</p>
                </div>
            </div>
        </section>

        <section id="contact">
            <h2>Get in Touch</h2>
            <div class="contact-content">
                <p>Interested in working together? Let's connect!</p>
                <div class="contact-links">
                    <a href="mailto:tombacco.devron@gmail.com" class="contact-item">
                        <span class="icon">@</span>
                        <span>tombacco.devron@gmail.com</span>
                    </a>
                    <a href="https://github.com/devrontombacco" target="_blank" class="contact-item">
                        <span class="icon">GH</span>
                        <span>github.com/devrontombacco</span>
                    </a>
                    <a href="https://www.linkedin.com/in/devrontombacco/" target="_blank" class="contact-item">
                        <span class="icon">in</span>
                        <span>linkedin.com/in/devrontombacco</span>
                    </a>
                    <a href="https://dtcloudnetworking.com" target="_blank" class="contact-item">
                        <span class="icon">WEB</span>
                        <span>dtcloudnetworking.com</span>
                    </a>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2025 Devron Tombacco. All rights reserved.</p>
    </footer>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
