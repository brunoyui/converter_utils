import json

MODEL_PATH = 'data/SPIDER-TEST_NUMBERSIGN_0-SHOT_CTX-200_ANS-4096_en1'
INPUT_PROMPT_REEXECUTE_PATH = MODEL_PATH + '/questions_reexecute.json'

INPUT_SQL_1 = MODEL_PATH + '/RESULTS_MODEL-gpt-3.5-turbo_without_sc.txt' 
INPUT_SQL_REEXECUTED = MODEL_PATH + '/RESULTS_MODEL-gpt-3.5-turbo_reexecuted.txt'
OUTPUT_SQL =  MODEL_PATH + '/RESULTS_MODEL-gpt-3.5-turbo_v2.txt'

def sql_file_generation(input_prompt_reexecuted_path, input_sql_path, input_sql_reexecuted_path, output_sql_path):
    with open(input_prompt_reexecuted_path) as f:
        data = json.load(f)
        question = data['questions']

    with open(input_sql_path, 'r') as file:
        file_sql = file.readlines()

    with open(input_sql_reexecuted_path, 'r') as file:
        file_sql_reexecuted = file.readlines()

    sqls_change = get_sqls_change(question, file_sql_reexecuted)

    # Initialize a list to store differences
    sqls_out = []

    for i, sql in enumerate(file_sql):
        if i not in sqls_change:
            sqls_out.append(sql)
        else:
            print(sql)
            print(sqls_change[i])
            sqls_out.append(sqls_change[i])

    with open(output_sql_path, 'w') as output_file:
        for sql in sqls_out:
            output_file.write(sql)

def get_sqls_change(question, sql_reexecuted):
    sqls = {}
    for q, s in zip(question, sql_reexecuted):
        sqls[q['index']] = s
    return sqls

def main() -> None:
    sql_file_generation(INPUT_PROMPT_REEXECUTE_PATH, INPUT_SQL_1, INPUT_SQL_REEXECUTED, OUTPUT_SQL)

if __name__ == "__main__":
    main()