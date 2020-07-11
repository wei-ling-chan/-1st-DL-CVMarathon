# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 11:51:51 2020

@author: JU
"""

import re  #載入re模組

# 定義一個函數，用來測試正規表達式是否匹配文本
def RegexMatchingTest(regex, input_text):
    #將正規表達式轉換成pattern
    pattern = re.compile(regex)
    # pattern = re.compile(regex, flags=re.IGNORECASE)  #若要忽略大小寫，在編譯時加上flags=re.IGNORECASE
    
    # 帶入編譯後的pattern，來測試是否匹配
    # 這裡也可以用match()、split()、findall()、sub()等其他函數來測試匹配
    result = re.search(pattern, input_text)

    if result:
        # 匹配完的結果會儲存在group()的屬性中，我們可以把匹配的結果列印出來
        print("Matched: %s" % (result.group()))
        
        if result.lastindex is not None:
            # group(0)代表整個字串，group(1)、group(2)...代表分組中，匹配的內容
            for i in range(0, result.lastindex+1):
                print("  group(%d): %s" % (i, result.group(i)))
    else:
        print("Not matched.")
        
test_string = "My plate number is XYZ-1234."
regex = 'My plate number is \w\w\w-\d\d\d\d'
RegexMatchingTest(regex, test_string)

test_string = "My phone number is 0912-345 678."
regex = 'My phone number is \d\d\d\d-\d\d\d\s\d\d\d'
RegexMatchingTest(regex, test_string)

#利用量詞{n,m}來簡化寫法
test_string = "My phone number is 0912-345 678."
regex = 'My phone number is \d{4}-\d{3}\s{1}\d{3}'
RegexMatchingTest(regex, test_string)

# 更偷懶的寫法，用「.」來代表任何字元
test_string = "My phone number is 0912-345 678."
regex = 'My phone number is .{4}-.{3}.{1}.{3}'
RegexMatchingTest(regex, test_string)

test_string = "I love dogs."
regex = 'I love [acdgnost]'
RegexMatchingTest(regex, test_string)

test_string = "I love cats."
regex = 'I love [acdgnost]'
RegexMatchingTest(regex, test_string)

# 若要匹配超過一個以上的字元，必須加入量詞(「+」或「*」或「?」)來表達
test_string = "I love dogs."
regex = 'I love [acdgnost]+'
RegexMatchingTest(regex, test_string)

test_string = "I love people."
regex = 'I love [acdgnost]+'
RegexMatchingTest(regex, test_string)
# people裡面只有'p'、'e'、'o'、'l'等字元，無法滿足[acdgnost]裡面所列出的條件

test_string = "I like baseball sport."
regex = 'I like (hiking|baseball) sport'
RegexMatchingTest(regex, test_string)

test_string = "I like hiking sport."
regex = 'I like (hiking|basketball) sport'
RegexMatchingTest(regex, test_string)

test_string = "Please call number (02)2882-5252."
regex = 'Please call number \([0-9]{2}\)[0-9]{4}-[0-9]{4}'  #用「\(」來匹配左括號"("，用「\)」來匹配右括號")"
RegexMatchingTest(regex, test_string)

test_string = "Here are 中文字 and English"  #中英夾雜的句子
regex = '[\u4e00-\u9fa5]+'                  #中文的UNICODE，範圍是0x4E00 ~ 0x9FA5
RegexMatchingTest(regex, test_string)