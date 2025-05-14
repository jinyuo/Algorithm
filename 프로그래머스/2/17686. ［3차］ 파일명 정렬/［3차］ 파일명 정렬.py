import re

def solution(files):
    pattern = '\d+'
    list_files = []
    for file in files:
        number = re.search(pattern, file).group()
        head, *tail = file.split(number)
        list_files.append(
            {'file': file, 'head': head.lower(), "number": int(number), "tail": tail[0].lower()}
        )
    list_files = sorted(list_files, key=lambda x: (x['head'], x['number']))

    return [file['file'] for file in list_files]