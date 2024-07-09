# 파일의 모든 내용을 지움
# with open('vocabulary.txt', 'w', encoding='utf-8') as f:
#     pass

with open('vocabulary.txt', 'a', encoding='utf-8') as f:
    while True:
        english = input("영어 단어를 입력하세요: ")
        if english == 'q':
            break

        korean = input("한국어 뜻을 입력하세요: ")
        if korean == 'q':
            break
    
        f.write(f"{english}: {korean}\n")