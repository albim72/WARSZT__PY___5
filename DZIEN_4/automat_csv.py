import time
import csv
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CsvHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".csv"):
            print(f"Nowy plik CSV utworzony: {event.src_path}")
            self.process_csv(event.src_path)

    def process_csv(self, file_path):
        output_file = file_path.replace(".csv", "_processed.csv")
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]

        processed_data = []
        for row in data:
            processed_row = {k: v.upper() for k, v in row.items()}
            processed_data.append(processed_row)

        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = processed_data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(processed_data)
        print(f"Plik CSV został przetworzony i zapisany jako: {output_file}")

if __name__ == "__main__":
    path = "C:/tmp_csv"  # Katalog do monitorowania
    event_handler = CsvHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)

    print(f"Rozpoczęto monitorowanie katalogu: {path}")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
