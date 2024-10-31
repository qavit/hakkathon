import random

# 錯題記錄和語料庫
correct_answers = 0
total_answers = 0
parallel_corpus = []
error_corpus = []

example_database = [
    {
        "hakka_sentence": "捱|想愛|買|番檨",
        "zh_sentence": "我想要買芒果",
        "segmented_hakka": ["捱", "想愛", "買", "_"],
        "word_to_fill": "番檨",
        "word_info": {"hakpin": "fanˊ son", "meaning": "芒果"}
    },
    {
        "hakka_sentence": "捱|去|學校|學|客語",
        "zh_sentence": "我去學校學客語",
        "segmented_hakka": ["捱", "去", "學校", "學", "_"],
        "word_to_fill": "客語",
        "word_info": {"hakpin": "hagˋ ngiˊ", "meaning": "客語"}
    },
    {
        "hakka_sentence": "今晡日|天時|恁好",
        "zh_sentence": "今天的天氣真好",
        "segmented_hakka": ["今晡日", "天氣", "_", "好"],
        "word_to_fill": "恁",
        "word_info": {"hakpin": "anˋ", "meaning": "真"}
    }
]

# 查詢功能
def lookup_word_info(word_info, mode="hakpin"):
    """查詢詞彙的客語拼音或華語翻譯"""
    if mode == "hakpin":
        return word_info["hakpin"]
    elif mode == "meaning":
        return word_info["meaning"]
    else:
        return "查詢選項無效"

# 問題生成
def create_question(entry):
    segmented_hakka = entry["segmented_hakka"]
    zh_sentence = entry["zh_sentence"]
    word_info = entry["word_info"]
    
    print("客語例句：", "|".join(segmented_hakka))
    print("華語翻譯：", zh_sentence)
    
    # 查詢選項
    # query_option = input("是否需要查詢詞彙拼音或華語翻譯？(輸入 1:拼音, 2:翻譯, 3:跳過) ")
    # if query_option == "1":
    #     print("拼音：", lookup_word_info(word_info, "hakpin"))
    # elif query_option == "2":
    #     print("華語翻譯：", lookup_word_info(word_info, "meaning"))
    # else:
    #     pass
    
    if 
    answer = input("請填寫空格中的詞彙：")
    isCorrect = answer == entry["word_to_fill"]

    return isCorrect, entry["hakka_sentence"], zh_sentence

# 問答過程
def run_quiz():
    global correct_answers, total_answers
    entry_idx = random.randint(1,len(example_database))
    entry = example_database[entry_idx]
    print(f"\n題號：{entry_idx}")
    = create_question(entry)
    
    # 結果處理
    total_answers += 1
    if isCorrect:
        correct_answers += 1
        print("回答正確！")
        parallel_corpus.append({"客語": hakka_sentence, "華語": zh_sentence})
    else:
        print("回答錯誤。")
        error_corpus.append({"客語": hakka_sentence, "華語": zh_sentence})
    
    # 提供錯題回饋
    # feedback = input("是否對此題目提供回饋？(y/n): ")
    # if feedback.lower() == "y":
    #     issue = input("請描述您發現的問題：")
    #     error_corpus[-1]["回饋"] = issue

# 顯示錯題
def show_errors():
    print("\n錯題列表：")
    for i, entry in enumerate(error_corpus):
        print(f"{i+1}. 客語：{entry['客語']}")
        print(f"   華語：{entry['華語']}")
        if "回饋" in entry:
            print(f"   回饋：{entry['回饋']}")

# 開始測驗
for _ in range(3):  # 可以根據需求調整題數
    run_quiz()

# 顯示總結
print("\n測驗完成！")
print(f"您的正確率：{correct_answers / total_answers * 100:.2f}%")
print("平行語料庫已更新。")
print(parallel_corpus)
show_errors()
