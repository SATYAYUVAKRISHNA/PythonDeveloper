import os

def analyze_logs(file_path):
    if os.path.getsize(file_path) > 100 * 1024 * 1024:
        print("File too large. Must be ≤ 100MB.")
        return

    ip_count = {}
    url_count = {}
    code_count = {}

    try:
        with open(file_path, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) < 9:
                    continue
                ip, url, code = parts[0], parts[6], parts[8]
                ip_count[ip] = ip_count.get(ip, 0) + 1
                url_count[url] = url_count.get(url, 0) + 1
                code_count[code] = code_count.get(code, 0) + 1

        print("Top 5 IPs:", sorted(ip_count.items(), key=lambda x: x[1], reverse=True)[:5])
        print("Top 5 URLs:", sorted(url_count.items(), key=lambda x: x[1], reverse=True)[:5])
        print("Response Codes Count:", code_count)

    except FileNotFoundError:
        print("File not found.")

# Uncomment and pass your log file path to test:
# analyze_logs("access.log")