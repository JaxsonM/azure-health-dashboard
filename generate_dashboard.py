#!/usr/bin/env python3

LOG_FILE = "/var/log/health_check.log"
OUTPUT_FILE = "/var/www/html/index.html"

lines = []
try:
    with open(LOG_FILE, "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    lines = []

latest = lines[-1].strip() if lines else ""

def parse_line(line):
    try:
        timestamp = line[1:20]
        parts = line[22:].split("|")
        disk = parts[0].split(":", 1)[1].strip()
        memory = parts[1].split(":", 1)[1].strip()
        load = parts[2].split(":", 1)[1].strip()
        nginx = parts[3].split(":", 1)[1].strip()
        return timestamp, disk, memory, load, nginx
    except:
        return ("N/A", "N/A", "N/A", "N/A", "N/A")

timestamp, disk, memory, load, nginx = parse_line(latest)

def status_color(value, metric):
    try:
        num = float(value.replace("%", ""))
        if metric in ("disk", "memory"):
            if num >= 85:
                return "#ff4d4d"
            elif num >= 70:
                return "#ffaa00"
            else:
                return "#4dff91"
    except:
        pass
    if metric == "nginx":
        return "#4dff91" if value == "active" else "#ff4d4d"
    return "#ffffff"

disk_color = status_color(disk, "disk")
mem_color = status_color(memory, "memory")
nginx_color = status_color(nginx, "nginx")

recent = lines[-10:]
rows = ""
for line in reversed(recent):
    t, d, m, l, n = parse_line(line.strip())
    n_color = "#4dff91" if n == "active" else "#ff4d4d"
    rows += f"""
    <tr>
        <td>{t}</td>
        <td>{d}</td>
        <td>{m}</td>
        <td>{l}</td>
        <td style="color:{n_color}; font-weight:bold;">{n}</td>
    </tr>"""

html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Health Dashboard</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            background: #0f0f0f;
            color: #e0e0e0;
            font-family: 'Segoe UI', sans-serif;
            padding: 40px;
        }}
        h1 {{
            font-size: 1.6rem;
            color: #ffffff;
            margin-bottom: 4px;
        }}
        .subtitle {{
            font-size: 0.85rem;
            color: #888;
            margin-bottom: 32px;
        }}
        .cards {{
            display: flex;
            gap: 16px;
            margin-bottom: 40px;
            flex-wrap: wrap;
        }}
        .card {{
            background: #1a1a1a;
            border: 1px solid #2a2a2a;
            border-radius: 10px;
            padding: 20px 28px;
            min-width: 160px;
        }}
        .card .label {{
            font-size: 0.75rem;
            color: #888;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 8px;
        }}
        .card .value {{
            font-size: 1.8rem;
            font-weight: bold;
        }}
        h2 {{
            font-size: 1rem;
            color: #aaa;
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.85rem;
        }}
        th {{
            text-align: left;
            padding: 10px 14px;
            background: #1a1a1a;
            color: #888;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            font-size: 0.75rem;
        }}
        td {{
            padding: 10px 14px;
            border-bottom: 1px solid #1e1e1e;
        }}
        tr:hover td {{
            background: #1a1a1a;
        }}
    </style>
</head>
<body>
    <h1>linux-lab-vm-jjm8 - Health Dashboard</h1>
    <div class="subtitle">Last updated: {timestamp}</div>

    <div class="cards">
        <div class="card">
            <div class="label">Disk Usage</div>
            <div class="value" style="color:{disk_color}">{disk}</div>
        </div>
        <div class="card">
            <div class="label">Memory Usage</div>
            <div class="value" style="color:{mem_color}">{memory}</div>
        </div>
        <div class="card">
            <div class="label">Load Average</div>
            <div class="value" style="color:#ffffff">{load}</div>
        </div>
        <div class="card">
            <div class="label">Nginx</div>
            <div class="value" style="color:{nginx_color}">{nginx}</div>
        </div>
    </div>

    <h2>Recent History</h2>
    <table>
        <thead>
            <tr>
                <th>Timestamp</th>
                <th>Disk</th>
                <th>Memory</th>
                <th>Load</th>
                <th>Nginx</th>
            </tr>
        </thead>
        <tbody>
            {rows}
        </tbody>
    </table>
</body>
</html>"""

with open(OUTPUT_FILE, "w") as f:
    f.write(html)

print("Dashboard generated.")
