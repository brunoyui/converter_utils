import re

INPUT_PATH = 'data/SPIDER-TEST_SQL_5-SHOT_COSSIMILAR_QA-EXAMPLE_CTX-200_ANS-4096/RESULTS_MODEL-Meta-Llama-3-8B-Instruct.txt'
OUTPUT_PATH = 'data/SPIDER-TEST_SQL_5-SHOT_COSSIMILAR_QA-EXAMPLE_CTX-200_ANS-4096/RESULTS_MODEL-Meta-Llama-3-8B-Instruct_cleaner.txt'

def extractor(file_path, output_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(output_path, 'w') as ouput_file:
        for line in lines:
            sql = extract_sql_query(line)
            #print(sql)
            ouput_file.write(sql)
        
def extract_sql_query(text):
    #pattern = r'(?:\: SELECT|\*\/ SELECT)\s+.*?\b(?:This\s*(?:SQL\s*)?query)'
    pattern = r'(?:\: SELECT|\*\/ SELECT|\? SELECT|\. SELECT)\s+.*'
    pattern2 = r'\sThis'
    pattern3 = r'SELECT\s+.*'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        sql_query = match.group(0).strip()
        match2 = re.search(pattern2, sql_query,re.DOTALL)
        if match2:
            sql_query = sql_query[:match2.start()].strip()
        else:
            print(sql_query)
        match3 = re.search(pattern3, sql_query,re.DOTALL)
        sql_query = match3.group().strip()
        return sql_query + '\n' if sql_query.startswith('SELECT') else text
    else:
        return text


def main() -> None:
    extractor(INPUT_PATH, OUTPUT_PATH)

if __name__ == "__main__":
    main()

# Ajustar manualmente SELECT select