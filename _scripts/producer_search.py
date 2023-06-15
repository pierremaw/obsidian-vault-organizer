import re
import os
import os.path
from collections import deque

from config import vault_path, producer_folder_name, template_folder_name
from read_files import read_file

'''
PRODUCER SEARCH
'''
def producer_search(file_path: str, memo_file_paths: dict, memo_file_meta_data: dict) -> list:

    try:
        if template_folder_name in file_path:
            return

        memo = {}
        producers = _producer_search(file_path, memo, memo_file_paths, memo_file_meta_data)

        if not producers:
            return 

        unique_producers = []
        queue = deque(producers)
        while queue:
            element = queue.popleft()
            if element not in unique_producers:
                unique_producers.append(element.strip())   

        if unique_producers == ['']:
            return

        # add formatting
        new_producers = [f'[[{producer}]]' for producer in unique_producers]
        new_producer_string = " " + ", ".join(new_producers)
            
        # update the original file
        file_string = read_file(f"{file_path}")
        new_file_string = re.sub(r"(?<=Producer:).*", new_producer_string, file_string)

        # write to the file
        with open(file_path, "w") as f:
            f.write(new_file_string)
        
        # See if there is an obsidian note for the producer by searching the vault for a file that has the producer's name
        for producer in unique_producers:
            if producer not in memo_file_paths.keys():
                new_file_path = os.path.join(f'{vault_path}', producer_folder_name, f'{producer}.md')

                with open(new_file_path, "w") as f:
                    f.write(f'Type: #producer\n')
                    f.write(f'___\n')
                    f.close()

    except:
        return
    # print (f'unique_producers: {unique_producers}')
    return unique_producers


'''
HELPER FUNCTION FOR PRODUCER SEARCH
TASK: This helper function does a DFS for the producers connected to a file and returns a list containing producers
'''
def _producer_search(file_path, memo, memo_file_path, memo_file_meta_data):
    
    file_name = os.path.basename(file_path)
    file_name, postfix = os.path.splitext(file_name)
    
    # base case 1
    if file_name in memo:
        return
    
    # if the file name is not in the memo, add it to the memo
    memo[file_name] = []    
    note_meta_data = memo_file_meta_data[file_name]
    note_producer = note_meta_data[file_name]['producer']
    
    # base case 2
    if note_producer == [] or note_producer == None:
        return

    producer_collection = []
    for producer in note_producer:
        producer = producer.strip()
        producer_collection.append(producer)

    producer_substrings = producer_collection[0].split(", ")
    
    clean_producer_collection = []
    for substring in producer_substrings:
        substring = substring.strip()
    
        extracted_string = re.findall(r"\[\[([\w\s.]+)\]\]", substring)
        if extracted_string:
            clean_producer_collection.append(extracted_string[0])
        if not extracted_string:
            clean_producer_collection.append(substring)
    
    return clean_producer_collection