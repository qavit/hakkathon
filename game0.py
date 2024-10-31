import random

# 基本詞彙資料集
vocabulary = [
    {"word": "正來尞", "hakka": "zang loiˇ liau", "meaning": "再見"},
    {"word": "爺哀", "hakka": "iaˇ oiˊ", "meaning": "父母"},
    {"word": "𤌍窯", "hakka": "kogˋ ieuˇ eˋ", "meaning": "燜烤番薯"},
    {"word": "包粟", "hakka": "bauˊ xiugˋ", "meaning": "玉米"}
]

# 計分系統
score = 0
total_questions = 0

# 隨機題型生成
def ask_matching_question():
    global score, total_questions
    total_questions += 1
    question = random.choice(vocabulary)
    answer = input(f"請問「{question['meaning']}」的客語怎麼說？ ")
    if answer.lower() == question['hakka']:
        print("正確！")
        score += 1
    else:
        print(f"錯誤，正確答案是「{question['hakka']}」")

def ask_choice_question():
    global score, total_questions
    total_questions += 1
    question = random.choice(vocabulary)
    options = [question['hakka']]
    while len(options) < 4:
        option = random.choice(vocabulary)['hakka']
        if option not in options:
            options.append(option)
    random.shuffle(options)
    
    print(f"請選出「{question['meaning']}」的正確客語說法：")
    for i, opt in enumerate(options):
        print(f"{i+1}. {opt}")
    answer = int(input("你的選擇是（輸入編號）： "))
    if options[answer - 1] == question['hakka']:
        print("正確！")
        score += 1
    else:
        print(f"錯誤，正確答案是「{question['hakka']}」")

def ask_fill_in_the_blank_question():
    global score, total_questions
    total_questions += 1
    question = random.choice(vocabulary)
    word_hint = question['hakka'][0] + '_' * (len(question['hakka']) - 1)
    answer = input(f"補全詞語：{word_hint} 是指「{question['meaning']}」的客語說法 ")
    if answer.lower() == question['hakka']:
        print("正確！")
        score += 1
    else:
        print(f"錯誤，正確答案是「{question['hakka']}」")

# 問題問答循環
def run_quiz():
    print("歡迎來到客語詞彙測驗！")
    for _ in range(5):
        print(f"第 {total_questions+1:02d} 題")
        question_type = random.choice([ask_matching_question, ask_choice_question, ask_fill_in_the_blank_question])
        question_type()
    evaluate_score()

# 評估成績並給出建議
def evaluate_score():
    print("\n測驗完成！")
    print(f"你的得分：{score}/{total_questions}")
    if score / total_questions >= 0.8:
        print("太棒了！你對基本詞彙非常熟悉，可以嘗試進階課程。")
    elif score / total_questions >= 0.5:
        print("不錯！建議進行更多的詞彙練習，增強記憶力。")
    else:
        print("加油！建議從基礎詞彙開始學習，並反覆練習。")

run_quiz()
