import sys
from typing import List, Dict

def parse_log_line(line: str) -> dict:
    parts = line.strip().split(' ', 3)
    if len(parts) < 4:
        return {}
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }

def load_logs(file_path: str) -> List[dict]:
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"Файл не знайдено: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка читання файлу: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    return list(filter(lambda log: log['level'].lower() == level.lower(), logs))

def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    counts = {}
    for log in logs:
        level = log['level']
        counts[level] = counts.get(level, 0) + 1
    return counts

def display_log_counts(counts: Dict[str, int]):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17} | {count}")

def display_logs(logs: List[dict]):
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Використання: python3 main.py <шлях_до_файлу> рівень_логування")
        sys.exit(1)

    log_file = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(log_file)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level_filter:
        filtered = filter_logs_by_level(logs, level_filter)
        print(f"\nДеталі логів для рівня '{level_filter.upper()}':")
        display_logs(filtered)

#python3 3/3.py /Users/elenabelova/Neoversity/python/goit-pycore-hw-05/3/logfile.log
#python3 3/3.py /Users/elenabelova/Neoversity/python/goit-pycore-hw-05/3/logfile.log info