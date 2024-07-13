with open('vocabulary.txt', 'r', encoding='utf-8') as file:
    for line in file:
        dictionary = line.strip().split(': ')
        english_word = dictionary[0]
        korean_word = dictionary[1]

        quiz = input(f'{korean_word}: ')
        if quiz == english_word:
            print("맞았습니다!")
        else: 
            print(f"아쉽습니다. 정답은 {english_word}입니다.")