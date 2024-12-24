import threading
import time

def process_file(filename):
    try:
        # Simulate file processing
        with open(filename, 'r') as f:
            data = f.read()
            # Do some processing with the data...
            time.sleep(1)
            print(f"File '{filename}' processed successfully.")

    except Exception as e:
        print(f"Error processing file '{filename}': {e}")

def main():
    # Define a list of files to process
    files = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']

    # Create threads for each file
    threads = []
    for filename in files:
        thread = threading.Thread(target=process_file, args=(filename,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()