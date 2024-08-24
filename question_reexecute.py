import json

INPUT_PATH = 'data/SPIDER-TEST_NUMBERSIGN_1-SHOT_COSSIMILAR_QA-EXAMPLE_CTX-200_ANS-4096/questions.json'
INPUT_V2_PATH = 'data/SPIDER-TEST_NUMBERSIGN_1-SHOT_COSSIMILAR_QA-EXAMPLE_CTX-200_ANS-4096/questions_v2.json'
OUTPUT_PATH = 'data/SPIDER-TEST_NUMBERSIGN_1-SHOT_COSSIMILAR_QA-EXAMPLE_CTX-200_ANS-4096/questions_reexecute.json'

def reexecute(file_path, file_path_v2, output_path):
    with open(file_path) as f:
        data = json.load(f)
        question = data['questions']

    with open(file_path_v2) as f:
        data1 = json.load(f)
        question1 = data1['questions']

    # Initialize a list to store differences
    reexecute = []

    # Assuming both JSON files are lists of dictionaries
    for i, (item1, item2) in enumerate(zip(question, question1)):
        if item1.get('prompt') != item2.get('prompt'):
            item2['index'] = i
            print(item2)
            reexecute.append(item2)

    # Write the differences to a new JSON file
    with open(output_path, 'w') as outfile:
        json.dump(reexecute, outfile, indent=4)

def main() -> None:
    reexecute(INPUT_PATH, INPUT_V2_PATH, OUTPUT_PATH)

if __name__ == "__main__":
    main()