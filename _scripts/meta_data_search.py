import re
import os
import os.path

from read_files import read_file

def _meta_data_search(file_path, memo):
    '''
    Searches for meta data in a file and returns a dictionary containing metadata
    The key is the filename and the value is a dictionary containing the metadata
    The value containing dictionary contains the following keys:
    - producer
    - topics
    - type
    - reference

    The values for each key is a list that contains strings
    '''
    
    file_name = os.path.basename(file_path)
    file_name, postfix = os.path.splitext(file_name)
        
    # base case 1
    if file_name in memo:
        return
    
    memo[file_name] = {}

    # if the file name is not in the memo, add it to the memo
    file_string = read_file(f"{file_path}")  
    
    # Producer field metadata
    memo[file_name]['producer'] = []
    note_producer = re.findall(r"(?<=Producer:).*", file_string)

    if note_producer != []:
        note_producer = note_producer[0].strip()

        # print(f'note_producer: {note_producer}')
        # check if the note_producer is empty
        if note_producer != "":

            note_producer = note_producer.split(",")
            # print(f'note_producer: {note_producer}')

            for i in range(len(note_producer)):
                note = note_producer[i]
                note_producer[i] = note.strip()
                # print(f'note: {note}')
                # memo[file_name]['producer'].append(note)
            # print(f'note_producer: {note_producer}')

            for i in range(len(note_producer)):
                note = note_producer[i]
                # print(f'note: {note}')

                # check if the element is a string
                if isinstance(note, str):
                    # check if the string starts with [[ and ends with ]]
                    if note.startswith("[[") and note.endswith("]]"):
                        # print (f'note starts with [[ and ends with ]]')
                        # extract the string between the brackets
                        extracted_string = note[2:-2]
                        # print(f'extracted_string: {extracted_string}')
                        # append the extracted string to the memo
                        memo[file_name]['producer'].append(extracted_string)
                    elif note.startswith("#"):
                        # print (f'note starts with #')
                        # extract the string between the brackets
                        extracted_string = note[1:]
                        # print(f'extracted_string: {extracted_string}')
                        # append the extracted string to the memo
                        memo[file_name]['type'].append(extracted_string)
                    else:
                        # print (f'note does not start with [[ and end with ]]')
                        memo[file_name]['producer'].append(note)


     # Type field metadata
    memo[file_name]['type'] = []
    note_type = re.findall(r"(?<=Type:).*", file_string)

    if note_type != []:
        note_type = note_type[0].strip()

        # print(f'note_type: {note_type}')
        # check if the note_type is empty
        if note_type != "":

            note_type = note_type.split(",")
            # print(f'note_type: {note_type}')

            for i in range(len(note_type)):
                note = note_type[i]
                note_type[i] = note.strip()
                # print(f'note: {note}')
                # memo[file_name]['type'].append(note)
            # print(f'note_type: {note_type}')

            for i in range(len(note_type)):
                note = note_type[i]
                # print(f'note: {note}')

                # check if the element is a string
                if isinstance(note, str):
                    # check if the string starts with [[ and ends with ]]
                    if note.startswith("[[") and note.endswith("]]"):
                        # print (f'note starts with [[ and ends with ]]')
                        # extract the string between the brackets
                        extracted_string = note[2:-2]
                        # print(f'extracted_string: {extracted_string}')
                        # append the extracted string to the memo
                        memo[file_name]['type'].append(extracted_string)
                    elif note.startswith("#"):
                        # print (f'note starts with #')
                        # extract the string between the brackets
                        extracted_string = note[1:]
                        # print(f'extracted_string: {extracted_string}')
                        # append the extracted string to the memo
                        memo[file_name]['type'].append(extracted_string)
                    else:
                        # print (f'note does not start with [[ and end with ]]')
                        memo[file_name]['type'].append(note)


    # Topics field metadata
    memo[file_name]['topic'] = []
    note_topic = re.findall(r"(?<=Topics:).*", file_string)

    if note_topic != []:
        note_topic = note_topic[0].strip()

        # print(f'note_topic: {note_topic}')
        # check if the note_topic is empty
        if note_topic != "":

            note_topic = note_topic.split(",")
            # print(f'note_topic: {note_topic}')

            for i in range(len(note_topic)):
                note = note_topic[i]
                note_topic[i] = note.strip()
                # print(f'note: {note}')
                # memo[file_name]['topic'].append(note)
            # print(f'note_topic: {note_topic}')

            for i in range(len(note_topic)):
                note = note_topic[i]
                # print(f'note: {note}')

                # check if the element is a string
                if isinstance(note, str):
                    # check if the string starts with [[ and ends with ]]
                    if note.startswith("[[") and note.endswith("]]"):
                        # print (f'note starts with [[ and ends with ]]')
                        # extract the string between the brackets
                        extracted_string = note[2:-2]
                        # print(f'extracted_string: {extracted_string}')
                        # append the extracted string to the memo
                        memo[file_name]['topic'].append(extracted_string)
                    elif note.startswith("#"):
                        # print (f'note starts with #')
                        # extract the string between the brackets
                        extracted_string = note[1:]
                        # print(f'extracted_string: {extracted_string}')
                        # append the extracted string to the memo
                        memo[file_name]['type'].append(extracted_string)
                    else:
                        # print (f'note does not start with [[ and end with ]]')
                        memo[file_name]['topic'].append(note)

    

    # Reference field metadata
    memo[file_name]['reference'] = []
    note_reference = re.findall(r"(?<=Reference:).*", file_string)

    if note_reference != []:
        note_reference = note_reference[0].strip()

        # print(f'note_reference: {note_reference}')
        # check if the note_reference is empty
        if note_reference != "":

            note_reference = note_reference.split(",")
            # print(f'note_reference: {note_reference}')

            for i in range(len(note_reference)):
                note = note_reference[i]
                note_reference[i] = note.strip()
                # print(f'note: {note}')
                # memo[file_name]['reference'].append(note)
            # print(f'note_reference: {note_reference}')

            for i in range(len(note_reference)):
                note = note_reference[i]
                # print(f'note: {note}')

                # check if the element is a string
                if isinstance(note, str):
                    # check if the string starts with [[ and ends with ]]
                    if note.startswith("[[") and note.endswith("]]"):
                        # print (f'note starts with [[ and ends with ]]')
                        # extract the string between the brackets
                        extracted_string = note[2:-2]
                        # print(f'extracted_string: {extracted_string}')
                        # append the extracted string to the memo
                        memo[file_name]['reference'].append(extracted_string)
                    elif note.startswith("#"):
                        # print (f'note starts with #')
                        # extract the string between the brackets
                        extracted_string = note[1:]
                        # print(f'extracted_string: {extracted_string}')
                        # append the extracted string to the memo
                        memo[file_name]['type'].append(extracted_string)
                    else:
                        # print (f'note does not start with [[ and end with ]]')
                        memo[file_name]['reference'].append(note)


    
    # print(f'note_reference: {note_reference}')

    return memo
