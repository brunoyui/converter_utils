import re

INPUT_PATH = 'data/SPIDER-TEST_SQL_5-SHOT_COSSIMILAR_QA-EXAMPLE_CTX-200_ANS-4096/RESULTS_MODEL-gpt-4o-mini.txt'
OUTPUT_PATH = 'data/SPIDER-TEST_SQL_5-SHOT_COSSIMILAR_QA-EXAMPLE_CTX-200_ANS-4096/RESULTS_MODEL-gpt-4o-mini_cleaner.txt'

def cleaner(file_path, output_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        lines = file.readlines()

    with open(output_path, 'w') as output_file:
        for line in lines:
            line = line.replace("`", "")
            #sql = extract_sql_query_3shot(line)
            sql = extract_sql_query_5shot(line)
            sql = extract_sql_query(sql)
            #sql = extract_sql_query_1shot(sql)
            sql = add_select_on_start(sql)
            output_file.write(sql)
        
def extract_sql_query(text):
    #pattern = r'(?:\: SELECT|\*\/ SELECT)\s+.*?\b(?:This\s*(?:SQL\s*)?query)'
    pattern = r'(?:\: SELECT|\*\/ SELECT|\? SELECT|\. SELECT)\s+.*'
    pattern2 = r'\s(This|Essa consulta|Este comando|Essa query|Explicaç|Isso\s)'
    pattern3 = r'SELECT\s+.*'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        sql_query = match.group(0).strip()
        match2 = re.search(pattern2, sql_query,re.DOTALL)
        if match2:
            sql_query = sql_query[:match2.start()].strip()
        match3 = re.search(pattern3, sql_query,re.DOTALL)
        sql_query = match3.group().strip()
        return sql_query + '\n' if sql_query.startswith('SELECT') else text
    else:
        sql_query = text
        match2 = re.search(pattern2, sql_query, re.DOTALL)
        if match2:
            #print(text)
            sql_query = text[:match2.start()].strip() + '\n'
        return sql_query

def extract_sql_query_1shot(text):
    pattern = r'Here are the\s+.*'
    pattern2 = r'(\*\*2.|\*\*Second).*\*\*.*'
    pattern3 = r'SELECT\s+.*'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        match2 = re.search(pattern2, text)
        if match2:
            match3 = re.search(pattern3, match2.group().strip())
            return match3.group().strip() + '\n'
        else:
            return text
    else:
        return text

def extract_sql_query_3shot(text):
    #pattern = r'Here are the\s+.*'
    pattern = r'(4\.\s).*'
    pattern2 = r'SELECT\s+.*'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        match2 = re.search(pattern2, match.group().strip())
        if match2:
            #print(match2.group().strip())
            return match2.group().strip() + '\n'
        else:
            return text
    else:
        return text

def extract_sql_query_5shot(text):
    #pattern = r'Here are the\s+.*'
    pattern = r'(6\.\s).*'
    pattern2 = r'SELECT\s+.*'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        match2 = re.search(pattern2, match.group().strip())
        if match2:
            print(match2.group().strip())
            return match2.group().strip() + '\n'
        else:
            return text
    else:
        return text

def add_select_on_start(text):
    if (text.upper().startswith('SELECT') or text.upper().startswith('WITH') or text.upper().startswith('CREATE')):
        return text
    else:
        #print(text)
        return 'SELECT ' + text

def main() -> None:
    cleaner(INPUT_PATH, OUTPUT_PATH)

if __name__ == "__main__":
    main()

# Ajustar manualmente SELECT select