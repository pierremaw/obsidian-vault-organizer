'''
IMPORT PACKAGES
'''
import os
import os.path
import shutil
from rapidfuzz import fuzz
from collections import deque

'''
IMPORT CREATE DICT FUNCTION
'''
from create_files_dict import create_files_dict

'''
IMPORT HELPER FUNCTIONS
'''
from topic_search import topic_search
from producer_search import producer_search
from delete_circular_topics import delete_circular_topics

'''
IMPORT CONFIG VARIABLES
'''
from config import vault_path, field_folder_name, topic_folder_name, producer_folder_name, source_folder_name, key_insight_folder_name, extracted_insight_folder_name, template_folder_name

'''
DEFINE GLOBAL VARIABLES
'''
memo_file_paths = {}
memo_file_meta_data = {}
memo_file_types = {}
memo_folder_paths = {}

def update_memo_variables(vault_path):
    global memo_file_paths, memo_file_meta_data, memo_file_types, memo_folder_paths
    memo_file_paths, memo_file_meta_data, memo_file_types, memo_folder_paths = create_files_dict(vault_path)

def organize_vault_structure(root_dir):

    for note_name in memo_file_types['field']:
        try:
            field_instance_folder = f"{vault_path}{field_folder_name}{note_name}/"
            
            check_folder_path = os.path.isdir(field_instance_folder)
            
            if not check_folder_path:
                os.mkdir(field_instance_folder)

            file_path = memo_file_paths[note_name]
            destination_path = field_instance_folder+f"{note_name}.md"
        
            if file_path != destination_path:
                shutil.move(file_path, destination_path)
                memo_file_paths[note_name] = destination_path    
        except:
            continue

    for note_name in memo_file_types['topic']:
        
        try:
            note_parent_type = 'field'
            note_type = 'topic'
            
            file_path = memo_file_paths[note_name]
            note_meta_data = memo_file_meta_data[note_name]
            note_topics = note_meta_data[note_name]['topic']

            field_collection = [note_topics[0]]
            field_collection_queue = deque(field_collection)
            selected_field = None
            best_fuzzy_match = float('-inf')
            while field_collection_queue:
                current_field = field_collection_queue.pop()
                current_ratio = fuzz.ratio(current_field, note_name)
                if current_ratio > best_fuzzy_match:
                    best_fuzzy_match = current_ratio
                    selected_field = current_field

            target_folder_path = os.path.join(vault_path, field_folder_name, selected_field, note_name)
            if not os.path.exists(target_folder_path):
                os.makedirs(target_folder_path, exist_ok=True)      

            current_file_path = memo_file_paths[note_name]
            destination_path = f'{target_folder_path}/'+f"{note_name}.md"
            
            if current_file_path != destination_path:
                shutil.move(current_file_path, destination_path)
                memo_file_paths[note_name] = destination_path

            # Create a topic folder for the topic in the topics folder
            target_folder_path = os.path.join(vault_path, topic_folder_name, note_name)
            if not os.path.exists(target_folder_path):
                os.makedirs(target_folder_path, exist_ok=True)    
    
        except:
            # print(f'topic section — error with topic {note_name}')
            continue
        
    for note_name in memo_file_types['subtopic']:
        
        try:
            note_parent_type = 'topic'
            note_type = 'subtopic'  
            file_path = memo_file_paths[note_name]         
            note_meta_data = memo_file_meta_data[note_name]
            note_topics = note_meta_data[note_name]['topic']
            
            topic_collection = []

            for topic_note in note_topics:
                try:
                    topic_note = topic_note.strip()        
                    topic_file_path = memo_file_paths[topic_note]
                    topic_meta_data = memo_file_meta_data[topic_note]
                    topic_meta_data_type = topic_meta_data[topic_note]['type']
                    if topic_meta_data_type:
                        if topic_meta_data_type[0] == note_parent_type:
                            topic_collection.append(topic_note)

                except:
                    # print(f'error with topic meta data')
                    continue

            topic_collection_queue = deque(topic_collection)

            selected_topic = None
            best_fuzzy_match = float('-inf')
            
            '''SELECT THE TOPIC THAT HAS THE HIGHEST FUZZY MATCH'''
            while topic_collection_queue:
                current_topic = topic_collection_queue.pop()
                current_ratio = fuzz.ratio(current_topic, note_name)
                if current_ratio > best_fuzzy_match:
                    best_fuzzy_match = current_ratio
                    selected_topic = current_topic

            selected_topic_meta_data = memo_file_meta_data[selected_topic]
            selected_topic_topics = selected_topic_meta_data[selected_topic]['topic']
            
            '''CREATE A FIELD_COLLECTION FOLDER AND ADD ALL FIELDS TO IT'''
            field_collection = []
            for topic_note in selected_topic_topics:
                try:
                    topic_note = topic_note.strip()    
                    topic_meta_data = memo_file_meta_data[topic_note]
                    topic_meta_data_type = topic_meta_data[topic_note]['type']
                
                    if topic_meta_data_type:
                        if topic_meta_data_type[0] == 'field':
                            field_collection.append(topic_note)
                except:
                    # print(f'error with topic meta data')
                    continue

            field_collection_queue = deque(field_collection)
            selected_field = None
            best_fuzzy_match = float('-inf')

            '''PERFORM FUZZY MATCH FOR FIELD'''
            while field_collection_queue:
                current_field = field_collection_queue.pop()
                current_ratio = fuzz.ratio(current_field, note_name)
    
                if current_ratio > best_fuzzy_match:
                    best_fuzzy_match = current_ratio
                    selected_field = current_field

            target_folder_path = os.path.join(vault_path, field_folder_name, selected_field, selected_topic, note_name)
            if not os.path.exists(target_folder_path):
                os.makedirs(target_folder_path, exist_ok=True)      
    
            current_file_path = memo_file_paths[note_name]
            destination_path = f'{target_folder_path}/'+f"{note_name}.md"
            if current_file_path != destination_path:
                shutil.move(current_file_path, destination_path)
                memo_file_paths[note_name] = destination_path
        
            '''CREATE A TOPIC FOLDER FOR THE TOPIC IN THE TOPICS FOLDER'''
            target_folder_path = os.path.join(vault_path, topic_folder_name, selected_topic, note_name)
            # print(f'target folder path os.path.join:  {target_folder_path}')
            if not os.path.exists(target_folder_path):
                os.makedirs(target_folder_path, exist_ok=True)      
    
        except:
            # print(f'topic section — error with topic {note_name}')
            continue

    for note_name in memo_file_types['microtopic']:
        
        try:
            
            note_great_grandparent_type = 'field'
            note_grandparent_type = 'topic'
            note_parent_type = 'subtopic'
            note_type = 'microtopic'
        
            current_note_file_path = memo_file_paths[note_name]
            note_meta_data = memo_file_meta_data[note_name]
            note_topics = note_meta_data[note_name]['topic']
            note_type = note_meta_data[note_name]['type']

            if note_type:
                note_type = note_type[0]

            subtopic_collection = []
            for topic_note in note_topics:
                try:
                    topic_note = topic_note.strip()
                    topic_file_path = memo_file_paths[topic_note]
                    topic_meta_data = memo_file_meta_data[topic_note]
                    topic_meta_data_type = topic_meta_data[topic_note]['type']
                    if topic_meta_data_type:
                        if topic_meta_data_type[0] == note_parent_type:
                            subtopic_collection.append(topic_note)

                except:
                    # print(f'error with topic meta data')
                    continue

            subtopic_collection_queue = deque(subtopic_collection)
            selected_subtopic = None
            best_fuzzy_match = float('-inf')
            
            while subtopic_collection_queue:
                current = subtopic_collection_queue.pop()
                current_fuzzy_match = fuzz.ratio(current, note_name)
                if current_fuzzy_match > best_fuzzy_match:
                    best_fuzzy_match = current_fuzzy_match
                    selected_subtopic = current

            selected_meta_data = memo_file_meta_data[selected_subtopic]
            selected_topics = selected_meta_data[selected_subtopic]['topic']
            
            collection = []

            if selected_topics:
                for topic_note in selected_topics:
                    try:
                        topic_meta_data = memo_file_meta_data[topic_note]
                        topic_meta_data_type = topic_meta_data[topic_note]['type']
                        if topic_meta_data_type:
                            if topic_meta_data_type[0] == note_grandparent_type:
                                collection.append(topic_note)
                    except:
                        # print(f'error with topic meta data')
                        continue

            collection_queue = deque(collection)
            selected_topic = None
            best_fuzzy_match = float('-inf')
            while collection_queue:
                current = collection_queue.pop()
                current_fuzzy_match = fuzz.ratio(current, note_name)
                if current_fuzzy_match > best_fuzzy_match:
                    best_fuzzy_match = current_fuzzy_match
                    selected_topic = current

            selected_meta_data = memo_file_meta_data[selected_topic]
            selected_topics = selected_meta_data[selected_topic]['topic']

            collection = []

            if selected_topics:
                for topic_note in selected_topics:
                    try:
                        topic_meta_data = memo_file_meta_data[topic_note]
                        topic_meta_data_type = topic_meta_data[topic_note]['type']
                        if topic_meta_data_type:
                            if topic_meta_data_type[0] == note_great_grandparent_type: 
                                collection.append(topic_note)
                    except:
                        # print(f'error with topic meta data')
                        continue

            if len(collection) > 1:
                collection_queue = deque(collection)
                selected_field = None
                best_fuzzy_match = float('-inf')
                while collection_queue:
                    current = collection_queue.pop()
                    current_fuzzy_match = fuzz.ratio(current, note_name)
                    if current_fuzzy_match > best_fuzzy_match:
                        best_fuzzy_match = current_fuzzy_match
                        selected_field = current
            elif len(collection) == 1:
                selected_field = collection[0]
            
            '''
            This target folder path is a path that includes the field folder name, the field name, the topic name, and the subtopic name.
            '''
            target_folder_path = os.path.join(vault_path, field_folder_name, selected_field, selected_topic, selected_subtopic)
            if not os.path.exists(target_folder_path):
                os.makedirs(target_folder_path, exist_ok=True)              
        
            destination_path = f'{target_folder_path}/'+f"{note_name}.md"
            
            if current_note_file_path != destination_path:
                shutil.move(current_note_file_path, destination_path)
                memo_file_paths[note_name] = destination_path
    
        except:
            # print(f'microtopic section — error with topic {note_name}')
            continue
        
    for note_name in memo_file_types['key_insight']:
        
        try:
            note_type = 'key_insight'
        
            current_file_path = memo_file_paths[note_name]
            note_meta_data = memo_file_meta_data[note_name]
            note_topics = note_meta_data[note_name]['topic']
            
            topics_list = []
            fields_list = []
            for topic in note_topics:
                topic_meta_data = memo_file_meta_data[topic]
                topic_type = topic_meta_data[topic]['type']
                if topic_type and topic_type[0] == 'topic':
                    topics_list.append(topic)
                if topic_type and topic_type[0] == 'field':
                    fields_list.append(topic)

            if len(topics_list) > 1:
                topics_list_queue = deque(topics_list)
                selected_topic = None
                best_fuzzy_match = float('-inf')
                while topics_list_queue:
                    current_topic = topics_list_queue.pop()
                    current_ratio = fuzz.ratio(current_topic, note_name)
                    if current_ratio > best_fuzzy_match:
                        best_fuzzy_match = current_ratio
                        selected_topic = current_topic
            elif len(topics_list) == 1:
                selected_topic = topics_list[0]

            if len(fields_list) > 1:
                fields_list_queue = deque(fields_list)
                selected_field = None
                best_fuzzy_match = float('-inf')
                while fields_list_queue:
                    current_field = fields_list_queue.pop()
                    current_ratio = fuzz.ratio(current_field, note_name)
                    if current_ratio > best_fuzzy_match:
                        best_fuzzy_match = current_ratio
                        selected_field = current_field
            elif len(fields_list) == 1:
                selected_field = fields_list[0]

            target_folder_path = os.path.join(vault_path, key_insight_folder_name, selected_field, selected_topic)                
            if not os.path.exists(target_folder_path):
                os.makedirs(target_folder_path, exist_ok=True)      
              
            destination_path = f'{target_folder_path}/'+f"{note_name}.md"
            
            if current_file_path != destination_path:
                shutil.move(current_file_path, destination_path)
                memo_file_paths[note_name] = destination_path

        except:
            # print(f'key_insights section — error with topic {note_name}')
            continue

    for note_name in memo_file_types['extracted_insight']:
        
        try:
            note_type = 'extracted_insight'            
            current_file_path = memo_file_paths[note_name]        
            note_meta_data = memo_file_meta_data[note_name]
            note_topics = note_meta_data[note_name]['topic']
            
            topics_list = []
            fields_list = []

            # get the metadata for the extracted topic to see which one is a topic
            for topic in note_topics:
                topic_file_path = memo_file_paths[topic]
    
                # get the metadata
                if topic_file_path:
                    topic_meta_data = memo_file_meta_data[topic]
                    topic_type = topic_meta_data[topic]['type']
                    if topic_type and topic_type[0] == 'topic':
                            topics_list.append(topic)
                    elif topic_type and topic_type[0] == 'field':
                            fields_list.append(topic)

            if len(topics_list) > 1:
                topics_list_queue = deque(topics_list)
                selected_topic = None
                best_fuzzy_match = float('-inf')
                # do fuzzy match for field
                while topics_list_queue:
                    current_topic = topics_list_queue.pop()
                    current_ratio = fuzz.ratio(current_topic, note_name)
                    if current_ratio > best_fuzzy_match:
                        best_fuzzy_match = current_ratio
                        selected_topic = current_topic
            elif len(topics_list) == 1:
                selected_topic = topics_list[0]

            if len(fields_list) > 1:
                fields_list_queue = deque(fields_list)
                selected_field = None
                best_fuzzy_match = float('-inf')
                while fields_list_queue:
                    current_field = fields_list_queue.pop()
                    current_ratio = fuzz.ratio(current_field, note_name)
                    if current_ratio > best_fuzzy_match:
                        best_fuzzy_match = current_ratio
                        selected_field = current_field
            elif len(fields_list) == 1:
                selected_field = fields_list[0]

            target_folder_path = os.path.join(vault_path, extracted_insight_folder_name, selected_field, selected_topic)                
            if not os.path.exists(target_folder_path):
                os.makedirs(target_folder_path, exist_ok=True)      
                    
            # get the destination folder path
            destination_path = f'{target_folder_path}/'+f"{note_name}.md"
            
            if current_file_path != destination_path:
                shutil.move(current_file_path, destination_path)
                memo_file_paths[note_name] = destination_path

        except:
            # print(f'extracted_insights section — error with topic {note_name}')
            continue

    for note_name in memo_file_types['source']:
        '''
        Organize source notes
        '''
        try:
            note_type = 'source'

            current_file_path = memo_file_paths[note_name]
            note_meta_data = memo_file_meta_data[note_name]
            note_topics = note_meta_data[note_name]['topic']
            
            topics_list = []
            fields_list = []
            for topic in note_topics:
                topic_file_path = memo_file_paths[topic]
                # get the metadata
                if topic_file_path:
                    topic_meta_data = memo_file_meta_data[topic]
                    topic_type = topic_meta_data[topic]['type']
                    if topic_type and topic_type[0] == 'topic':
                            topics_list.append(topic)
                    elif topic_type and topic_type[0] == 'field':
                            fields_list.append(topic)

            if len(topics_list) > 1:
                topics_list_queue = deque(topics_list)
                selected_topic = None
                best_fuzzy_match = float('-inf')
                # do fuzzy match for field
                while topics_list_queue:
                    current_topic = topics_list_queue.pop()
                    current_ratio = fuzz.ratio(current_topic, note_name)
                    if current_ratio > best_fuzzy_match:
                        best_fuzzy_match = current_ratio
                        selected_topic = current_topic
            elif len(topics_list) == 1:
                selected_topic = topics_list[0]

            # get the fields in the fields_list and fuzzy match         
            if len(fields_list) > 1:
                fields_list_queue = deque(fields_list)
                selected_field = None
                best_fuzzy_match = float('-inf')
                while fields_list_queue:
                    current_field = fields_list_queue.pop()
                    current_ratio = fuzz.ratio(current_field, note_name)
                    if current_ratio > best_fuzzy_match:
                        best_fuzzy_match = current_ratio
                        selected_field = current_field
            elif len(fields_list) == 1:
                selected_field = fields_list[0]

            target_folder_path = os.path.join(vault_path, source_folder_name, selected_field, selected_topic)
            if not os.path.exists(target_folder_path):
                os.makedirs(target_folder_path, exist_ok=True)      
            
            destination_path = f'{target_folder_path}/'+f"{note_name}.md"
            
            if current_file_path != destination_path:
                shutil.move(current_file_path, destination_path)
                memo_file_paths[note_name] = destination_path

        except:
            # print(f'source section — error with topic {note_name}')
            continue
    
    for note_name in memo_file_types['producer']:
    
        try:
            note_type = 'producer'
            current_file_path = memo_file_paths[note_name]       
            note_meta_data = memo_file_meta_data[note_name]
            
            target_folder_path = os.path.join(vault_path, producer_folder_name)            
            if not os.path.exists(target_folder_path):
                os.makedirs(target_folder_path, exist_ok=True)      
            
            destination_path = f'{target_folder_path}/'+f"{note_name}.md"
            
            if current_file_path != destination_path:
                shutil.move(current_file_path, destination_path)
                memo_file_paths[note_name] = destination_path

        except:
            # # print(f'producer section — error with producer {note_name}')
            continue
                
    return True

def update_topics(memo_file_paths, memo_file_meta_data):
    
    for k,v in memo_file_paths.items():
        topic_search(v, memo_file_paths, memo_file_meta_data)

def update_producers(memo_file_paths, memo_file_meta_data):
            for v in memo_file_paths.values():
                if template_folder_name in v:
                    continue
                producer_search(v, memo_file_paths, memo_file_meta_data)

def delete_circular_topics_call(memo_file_paths, memo_file_meta_data):
    for v in memo_file_paths.values():
        delete_circular_topics(v, memo_file_meta_data)

def delete_empty_folders(memo_folder_paths):
    '''helper function that traverses the vault and deletes empty folders'''

    for root, dirs, files in os.walk(vault_path, topdown=False):
        for name in dirs:
            dir_path = os.path.join(root, name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
       
'''
INVOKE CORE FUNCTIONS
'''
update_memo_variables(vault_path)
delete_empty_folders(memo_folder_paths)
update_topics(memo_file_paths, memo_file_meta_data)
update_producers(memo_file_paths, memo_file_meta_data)
delete_circular_topics_call(memo_file_paths, memo_file_meta_data)
update_memo_variables(vault_path)
organize_vault_structure(vault_path)