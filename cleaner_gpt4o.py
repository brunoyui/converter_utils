import re

INPUT_PATH = 'data/SPIDER-TEST_SQL_5-SHOT_COSSIMILAR_QA-EXAMPLE_CTX-200_ANS-4096/RESULTS_MODEL-gpt-4o-mini.txt'
OUTPUT_PATH = 'data/SPIDER-TEST_SQL_5-SHOT_COSSIMILAR_QA-EXAMPLE_CTX-200_ANS-4096/RESULTS_MODEL-gpt-4o-mini_cleaner.txt'

def cleaner(file_path, output_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(output_path, 'w') as output_file:
        for line in lines:
            sql = extract_sql_query(line)
            output_file.write(sql)
        
def extract_sql_query(text):
    # Define a regex pattern to match the SQL query within ```sql ``` markers
    pattern = r'```sql\s+(.*?)\s+```'
    
    # Search for the pattern in the text
    match = re.search(pattern, text, re.DOTALL)
    
    if match:
        # Return the matched SQL query
        return match.group(1).strip() + "\n"
    else:
        return text


def main() -> None:
    cleaner(INPUT_PATH, OUTPUT_PATH)

if __name__ == "__main__":
    main()

# Ajustar manualmente SELECT select