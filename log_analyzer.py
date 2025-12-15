import sys

def analyze_log(file_path):
    # Dictionary to store counts
    status_counts = {}
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.split()
                
                if len(parts) < 9:
                    continue
                
                status_code = parts[7]
                
                # Dictionary তে count করি
                if status_code in status_counts:
                    status_counts[status_code] += 1
                else:
                    status_counts[status_code] = 1
        
        return status_counts
    
    except FileNotFoundError:
        print("File not found!")
        return {}

def print_report(counts):
    print("--- Server Health Report ---")
    
    for code, count in counts.items():
        print(f"Status {code}: {count} occurrences")
    
    # Alert logic
    if counts.get("500", 0) > 2:
        print("!!! CRITICAL ALERT: High rate of server failures detected !!!")

if __name__ == "__main__":
    # Command line argument support
    log_file = sys.argv[1] if len(sys.argv) > 1 else "server.log"
    
    data = analyze_log(log_file)
    print_report(data)
