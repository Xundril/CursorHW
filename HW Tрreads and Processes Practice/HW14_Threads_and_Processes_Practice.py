"""
Create a script that should find the lines by provided pattern in the provided path directory with recursion (it means if the directory has other directories,
the script should get all the info from them as well) and threads.
"""

import glob
import time
from concurrent.futures import ThreadPoolExecutor


def find_by_pattern(filename, pattern):
    line_container = set()
    with open(filename) as f:
        for line in f:
            if pattern in line:
                line_container.add(line)
    return line_container


def find_all_files(directory_path, pattern):
    files = glob.glob(f'{directory_path}/**/*.py', recursive=True)
    print(files)
    container = set()
    with ThreadPoolExecutor() as pool:
        result = pool.map(find_by_pattern, files, pattern)
        for res in result:
            container.update(res)
    return container


if __name__ == "__main__":
    start = time.time()
    search = find_all_files('.', pattern='for')
    end = time.time() - start
    print(f'Time for searching: {end} seconds')
    for i in search:
        print(i)

# Output:

# C:\Users\Zver\PycharmProjects\CursorHW\venv\Scripts\python.exe "C:/Users/Zver/PycharmProjects/CursorHW/HW Tрreads and Processes Practice/HW14_Threads_and_Processes_Practice.py"
# ['.\\HW14_Threads_and_Processes_Practice.py']
# Time for searching: 0.0009970664978027344 seconds
# from concurrent.futures import ThreadPoolExecutor
#
#         for res in result:
#
#     search = find_all_files('.', pattern='for')
#
#         result = pool.map(find_by_pattern, files, pattern)
#
# def find_by_pattern(filename, pattern):
#
#             if pattern in line:
#
# if __name__ == "__main__":
#
# def find_all_files(directory_path, pattern):
#
# Create a script that should find the lines by provided pattern in the provided path directory with recursion (it means if the directory has other directories,
#
# the script should get all the info from them as well) and threads.
#
#     print(f'Time for searching: {end} seconds')
#
#         for line in f:
#
#     files = glob.glob(f'{directory_path}/**/*.py', recursive=True)
#
#     with open(filename) as f:
#
#     for i in search:
#
#     print(files)
#
#
# Process finished with exit code 0