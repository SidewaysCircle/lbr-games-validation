import os, sys, csv, re

def validate_globle(score):
    validChars = ['🟥', '🟧', '🟨', '⬜', '🟩']
    rawScore = ''
    for char in score[5]:
        if char in validChars:
            rawScore += char
    scoreNumber = rawScore.index('🟩') + 1
    return [score[0], score[1], score[2], score[3], score[4], scoreNumber, rawScore]


def validate_connections(score):
    validChars = ['🟨', '🟩', '🟦', '🟪']
    rawScore = ''
    scoreNumber = 0
    scoreMult = 64
    for char in score[5]:
        if char in validChars:
            rawScore += char
    #rawScore = ''.join(re.sub(r'[a-zA-Z#0123456789]', '', score[5]).splitlines()).replace(' ', '')

    if len(rawScore) % 4 == 0:
        for char in range(len(rawScore)//4):
            row = rawScore[char*4:(char*4)+4]
            if row == '🟨🟨🟨🟨':
                scoreNumber += 1 * scoreMult
            elif row == '🟩🟩🟩🟩':
                scoreNumber += 2 * scoreMult
            elif row == '🟦🟦🟦🟦':
                scoreNumber += 3 * scoreMult
            elif row == '🟪🟪🟪🟪':           
                scoreNumber += 4 * scoreMult
            scoreMult /= 2
    else:
        print("Connections score is invalid.")
        return None
    return [score[0], score[1], score[2], score[3], score[4], scoreNumber, rawScore]

def validate_wordle(score):
    validChars = ['⬛', '⬜', '🟨', '🟩']
    rawScore = ''
    scoreNumber = 7
    for char in score[5]:
        if char in validChars:
            rawScore += char
    if len(rawScore) % 5 == 0:
        for char in range(len(rawScore)//5):
            row = rawScore[char*5:(char*5)+5]
            if row == '🟩🟩🟩🟩🟩':
                scoreNumber = char+1
    else:
        print("Connections score is invalid.")
        return None
    return [score[0], score[1], score[2], score[3], score[4], scoreNumber, rawScore]

def validate_strands(score):
    validChars = ['💡', '🔵', '🟡']
    rawScore = ''
    for char in score[5]:
        if char in validChars:
            rawScore += char
    scoreNumber = rawScore.count('💡')
    return [score[0], score[1], score[2], score[3], score[4], scoreNumber, rawScore]

def validate_pub(score):
    exit

def validate_csv(file_path):
    validatedScores = []
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return False

    with open(file_path, mode='r', newline='', encoding='UTF-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader, None)
        if header is None:
            print("CSV file is empty.")
            return False
        
        for row in reader:
            if row[2] == 'Globle':
                validatedScores.append(validate_globle(row))
            elif row[2] == 'Connections':
                validatedScores.append(validate_connections(row))
            elif row[2] == 'Wordle':
                validatedScores.append(validate_wordle(row))
            elif row[2] == 'Strands':
                validatedScores.append(validate_strands(row))
            elif row[2] == 'Pub':
                validatedScores.append(validate_pub(row))
            else:
                print(f"Unknown game type: {row[2]}")
                continue
    return validatedScores


def main():
    file_path = 'src_csv/2025-11-19_Leeds_Games_Scores.csv'
    validated = validate_csv(file_path)
    print(validated)

main()
