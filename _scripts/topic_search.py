import re
import os
import os.path
from read_files import read_file
from config import template_folder_name

'''
TOPIC SEARCH FUNCTION
'''
def topic_search(file_path: str, memo_file_paths: dict, memo_file_meta_data: dict) -> list:
    '''
    This script searches for the topics of a file and returns a list that contains unique topics
    '''

    if template_folder_name in file_path:
        return

    memo = {}
    topics = _topic_search(file_path, 0, memo, memo_file_paths, memo_file_meta_data)

    if topics == None:
        return 

    topics_and_distances = []
    for value in topics.values():
        if value != []:
            for element in value:
                topics_and_distances.append(element)

    topic_list = []
    for element in topics_and_distances:
        topic, distance = element
        if topic_list == []:
            topic_list.append((topic, distance))
        else:
            for item in topic_list:
                topic_2, distance_2 = item
                if topic_2 == topic:
                    if distance_2 < distance:
                        topic_list.remove((topic_2, distance_2))
                        topic_list.append((topic, distance))
                else:
                    topic_list.append((topic, distance))
    
    sorted_tuple_list = sorted(topic_list, key=lambda x: x[1], reverse=True)

    unique_topics = []
    for topic in sorted_tuple_list:
        ref, distance = topic
        if ref not in unique_topics:
            unique_topics.append(ref) 
            
    if unique_topics == []:
        return
    
    new_topics = [f'[[{topic}]]' for topic in unique_topics]
    new_topic_string = " " + ", ".join(new_topics)
        
    # update the original file
    file_string = read_file(f"{file_path}")
    new_file_string = re.sub(r"(?<=Topics:).*", new_topic_string, file_string)

    # write to the file
    with open(file_path, "w") as f:
        f.write(new_file_string)
    
    return unique_topics

'''
TOPIC SEARCH HELPER FUNCTION
'''
def _topic_search(file_path, distance, memo, memo_file_paths, memo_file_meta_data):
    '''
    Helper function for topic_search.
    This helper function does a DFS for the topics connected to a file and returns a tuple list
    that contains the topic and the distance from the source file
    '''
    
    try:
        file_name = os.path.basename(file_path)
        file_name, postfix = os.path.splitext(file_name)

        # base case 1
        if file_name in memo:
            return
        
        memo[file_name] = []

        topic_meta_data = memo_file_meta_data[file_name]
        topic_list = topic_meta_data[file_name]['topic']

        # base case 2
        if topic_list == [] or topic_list == None:
            return
        
        for topic_text in topic_list:
            substring = topic_text.strip()
        
            if substring:
                extracted_string = re.findall(r"\[\[([\w\s.]+)\]\]", substring)
                if extracted_string:
                    memo[file_name].append((extracted_string, distance+1))
                if not extracted_string or extracted_string == []:
                    memo[file_name].append((substring, distance+1))

                file_path = memo_file_paths[topic_text]
                _topic_search(file_path, distance+1, memo, memo_file_paths, memo_file_meta_data)
    
    except:
        return

    return memo