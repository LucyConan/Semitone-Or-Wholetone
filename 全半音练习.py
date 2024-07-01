import re

# 字符定义
# shengdiao = '\u266F'
# jiangdiao = '\u266D'
# chongshengdiao = 'X'
# chongjiangdiao = '\u266D\u266D'
# sub = ["\u2080", "\u2081", "\u2082", "\u2083", "\u2084", "\u2085", "\u2086", "\u2087", "\u2088", "\u2089"] # 下标 0-9
# sup = ["\u2070", "\u00B9", "\u00B2", "\u00B3", "\u2074", "\u2075", "\u2076", "\u2077", "\u2078", "\u2079"] # 上标 0-9
# ₀₁₂₃₄₅₆₇₈₉
# ⁰¹²³⁴⁵⁶⁷⁸⁹


# 所有音名的字典 0-87
all_musical_alphabet = dict()


# 大字二组
# 不存在于琴键的两个音名，容错用
all_musical_alphabet[-2] = 'G-2 XF-2 bbA-2'
all_musical_alphabet[-1] = '#G-2 bA-2'

all_musical_alphabet[0] = 'A-2 XG-2 bbB-2'
all_musical_alphabet[1] = '#A-2 bB-2 bbC-1'
all_musical_alphabet[2] = 'B-2 bC-1 XA-2'

# 大字一组
all_musical_alphabet[3] = 'C-1 #B-2 bbD-1'
all_musical_alphabet[4] = '#C-1 bD-1 XB-2'
all_musical_alphabet[5] = 'D-1 XC-1 bbE-1'
all_musical_alphabet[6] = '#D-1 bE-1 bbF-1'
all_musical_alphabet[7] = 'E-1 XD-1 bF-1'
all_musical_alphabet[8] = 'F-1 #E-1 bbG-1'
all_musical_alphabet[9] = '#F-1 bG-1 XE-1'
all_musical_alphabet[10] = 'G-1 XF-1 bbA-1'
all_musical_alphabet[11] = '#G-1 bA-1'
all_musical_alphabet[12] = 'A-1 XG-1 bbB-1'
all_musical_alphabet[13] = '#A-1 bB-1 bbC'
all_musical_alphabet[14] = 'B-1 XA-1 bC'

# 大字组
all_musical_alphabet[15] = 'C #B-1 bbD'
all_musical_alphabet[16] = '#C bD XB-1'
all_musical_alphabet[17] = 'D XC bbE'
all_musical_alphabet[18] = '#D bE bbF'
all_musical_alphabet[19] = 'E XD bF'
all_musical_alphabet[20] = 'F #E bbG'
all_musical_alphabet[21] = '#F bG XE'
all_musical_alphabet[22] = 'G XF bbA'
all_musical_alphabet[23] = '#G bA'
all_musical_alphabet[24] = 'A XG bbB'
all_musical_alphabet[25] = '#A bB bbc'
all_musical_alphabet[26] = 'B XA bc'

# 小字组
all_musical_alphabet[27] = 'c #B bbd'
all_musical_alphabet[28] = '#c bd XB'
all_musical_alphabet[29] = 'd Xc bbe'
all_musical_alphabet[30] = '#d be bbf'
all_musical_alphabet[31] = 'e Xd bf'
all_musical_alphabet[32] = 'f #e bbg'
all_musical_alphabet[33] = '#f bg Xe'
all_musical_alphabet[34] = 'g Xf bba'
all_musical_alphabet[35] = '#g ba'
all_musical_alphabet[36] = 'a Xg bbb'
all_musical_alphabet[37] = '#a bb bbc1'
all_musical_alphabet[38] = 'b Xa bc1'

# 小字一组
all_musical_alphabet[39] = 'c1 #b bbd1'
all_musical_alphabet[40] = '#c1 bd1 Xb'
all_musical_alphabet[41] = 'd1 Xc1 bbe1'
all_musical_alphabet[42] = '#d1 be1 bbf1'
all_musical_alphabet[43] = 'e1 Xd1 bf1'
all_musical_alphabet[44] = 'f1 #e1 bbg1'
all_musical_alphabet[45] = '#f1 bg1 Xe1'
all_musical_alphabet[46] = 'g1 Xf1 bba1'
all_musical_alphabet[47] = '#g1 ba1'
all_musical_alphabet[48] = 'a1 Xg1 bbb1'
all_musical_alphabet[49] = '#a1 bb1 bbc2'
all_musical_alphabet[50] = 'b1 Xa1 bc2'

# 小字二组
all_musical_alphabet[51] = 'c2 #b1 bbd2'
all_musical_alphabet[52] = '#c2 bd2 Xb1'
all_musical_alphabet[53] = 'd2 Xc2 bbe2'
all_musical_alphabet[54] = '#d2 be2 bbf2'
all_musical_alphabet[55] = 'e2 Xd2 bf2'
all_musical_alphabet[56] = 'f2 #e2 bbg2'
all_musical_alphabet[57] = '#f2 bg2 Xe2'
all_musical_alphabet[58] = 'g2 Xf2 bba2'
all_musical_alphabet[59] = '#g2 ba2'
all_musical_alphabet[60] = 'a2 Xg2 bbb2'
all_musical_alphabet[61] = '#a2 bb2 bbc3'
all_musical_alphabet[62] = 'b2 Xa2 bc3'

# 小字三组
all_musical_alphabet[63] = 'c3 #b2 bbd3'
all_musical_alphabet[64] = '#c3 bd3 Xb2'
all_musical_alphabet[65] = 'd3 Xc3 bbe3'
all_musical_alphabet[66] = '#d3 be3 bbf3'
all_musical_alphabet[67] = 'e3 Xd3 bf3'
all_musical_alphabet[68] = 'f3 #e3 bbg3'
all_musical_alphabet[69] = '#f3 bg3 Xe3'
all_musical_alphabet[70] = 'g3 Xf3 bba3'
all_musical_alphabet[71] = '#g3 ba3'
all_musical_alphabet[72] = 'a3 Xg3 bbb3'
all_musical_alphabet[73] = '#a3 bb3 bbc4'
all_musical_alphabet[74] = 'b3 Xa3 bc4'

# 小字四组
all_musical_alphabet[75] = 'c4 #b3 bbd4'
all_musical_alphabet[76] = '#c4 bd4 Xb3'
all_musical_alphabet[77] = 'd4 Xc4 bbe4'
all_musical_alphabet[78] = '#d4 be4 bbf4'
all_musical_alphabet[79] = 'e4 Xd4 bf4'
all_musical_alphabet[80] = 'f4 #e4 bbg4'
all_musical_alphabet[81] = '#f4 bg4 Xe4'
all_musical_alphabet[82] = 'g4 Xf4 bba4'
all_musical_alphabet[83] = '#g4 ba4'
all_musical_alphabet[84] = 'a4 Xg4 bbb4'
all_musical_alphabet[85] = '#a4 bb4 bbc5'
all_musical_alphabet[86] = 'b4 Xa4 bc5'

# 小字五组
all_musical_alphabet[87] = 'c5 #b4 bbd5'
# 不存在于琴键的两个音名，容错用
all_musical_alphabet[88] = '#c5 bd5 Xb4'
all_musical_alphabet[89] = 'd5 Xc5 bbe5'


# 改成易读形式
def translate(o_str):
    o_str = re.sub(r'bb([a-gA-G])', r'♭♭\1', o_str)
    mapping = {"-2": "₂", "-1": "₁", "1": "¹", "2": "²", "3": "³", "4":  "⁴", "5": "⁵", "#": "♯"}
    for i in mapping:
        o_str = o_str.replace(i, mapping[i])
    return o_str

# 查找用户输入的音名在字典的索引
def find(str):
    for k in all_musical_alphabet:
        l = all_musical_alphabet[k].split()
        if str in l:
            return k
    return -99


while True:
    user  = input('1.半音 2.全音 0.退出\n')
    if user == '0':
        break
    if user == '1':
        while True:
            musical_alphabet = input('请输入音名：')
            if musical_alphabet == '0':
                break
            else:
                tmp = find(musical_alphabet)
                if tmp == -99:
                    print("没有此音名")
                    break
                answer1 = tmp - 1
                answer2 = tmp + 1
                print('降半音：' + translate(all_musical_alphabet[answer1]) + ' 升半音：' + translate(all_musical_alphabet[answer2]))
    elif user == '2':
        while True:
            musical_alphabet = input('请输入音名：')
            if musical_alphabet == '0':
                break
            else:
                tmp = find(musical_alphabet)
                if tmp == -99:
                    print("没有此音名")
                    break
                answer1 = tmp - 2
                answer2 = tmp + 2
                print('降全音：' + translate(all_musical_alphabet[answer1]) + ' 升全音：' + translate(all_musical_alphabet[answer2]))
                
print('Goodbye!')