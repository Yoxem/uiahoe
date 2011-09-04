#!/usr/bin/env python
#-*-coding:utf-8-*-
#uiahoe - 將POJ的數字標記轉成調號。N,nn ~ -> 小n，ou、oo -> 葫蘆點。
#Author: Chen, Chien-ting <chenjt30@gmail.com>
#version:0.1.0（務必和下行一致）
#LICENSE:GPL v3 (https://www.gnu.org/copyleft/gpl.html)

version = '0.1.0' #版本號，字串，得和上行一致

import sys, re
import string
#import argparse #參數析出器（以後加參數時用）

'''略合POJ規範的音節。存成 list。格式[聲母,母音,韻尾,數字音調]。如：['chh','e','ng','1']。
因子函數需要，故設為全域變數。'''
global anal_syllable

'''單一母音加調號'''
def vowel_add_mark(vowel):
    #附調號小寫字母 dictionary
    marked_lit_vowel_lst = \
        {'2': ('á', 'é', 'í', 'ó', 'ú'),
        '3': ('à', 'è' ,'ì' ,'ò'  ,'ù'),
        '5': ('â', 'ê' ,'î' ,'ô'  ,'û'),
        '7': ('ā' ,'ē' ,'ī' ,'ō'  ,'ū'),
        '8': ('a̍', 'e̍', 'i̍', 'o̍', 'u̍')
         }
    
    #附調號大寫字母 dictionary
    marked_cap_vowel_lst = \
        {'2': ('Á', 'É', 'Í', 'Ó' , 'Ú'),
        '3': ('À' ,'È' ,'Ì', 'Ò'  ,'Ù'),
        '5': ('Â', 'Ê' ,'Î' ,'Ô' ,'Û'),
        '7': ('Ā', 'Ē' ,'Ī' ,'Ō' ,'Ū'),
        '8': ('A̍' ,'E̍' ,'I̍' ,'O̍' ,'U̍')
         }
     
    vowel_order = None #母音序。a = 0, e = 1, i = 2, o = 3, u = 4。預設為 None
    
    #母音列表（依正規表示式語法寫，vowel_order 註解列之序）
    vowel_list = ['[aA]', '[eE]', '[iI]', '[oO]', '[uU]'] 
    
    for i in range(len(vowel_list)):
        vowel_order = i
        
        if re.match(vowel_list[i], vowel): #欲加調號母音符合哪個母音

            #平聲不用加調號，故pass，因陽上已經變去，故不理該調值。 
            if anal_syllable[3] == '1' or anal_syllable[3] == '4':
                pass
            
            else:
                #print "enter line 48"
                if vowel in string.ascii_lowercase: #確認欲加號母音是小寫或否
                    vowel = marked_lit_vowel_lst[anal_syllable[3]][vowel_order]
                else: #大寫
                    vowel = marked_cap_vowel_lst[anal_syllable[3]][vowel_order]
            
            break #以後的不用比較是哪個母音了，為省時，離迴圈
    
        else:
            pass
    
    return vowel

'''主程式'''

if len(sys.argv) == 1:
    print "請輸入欲轉換的POJ數字符號。"
    exit()

orig_content  = "" #原來的POJ數字表記

for i in  range(len(sys.argv)-1):
    orig_content = orig_content + " " + sys.argv[i+1] #整併待轉換文字（含空白）

orig_content = orig_content[1:] #刪除頭一個字（空白）

'''處理調號'''

#i.e. punctuation_list，符合符號定義的字元 list。用 regexp 語法
punctu_list = '([' + string.punctuation +\
    "、，。？！（）「」『』《》〈〉【】〔〕；：…－　\s" + '])'

#音節list（），包含符號、標點、其他文字
syllable_list = re.split(punctu_list, orig_content) 

result = "" #輸出的結果（預設為空）

'''對各音節進行處理'''
for i in range(len(syllable_list)):
    syllable = syllable_list[i] #待處理音節
    
    '''試將音節拆成各個組成成份，存成 anal_syllable。不行則跳過'''
    anal_pattern = re.compile(r"^([^aeiouAEIOU1-9]{0,2}?[hH]??)([aeiouAEIOU]{0,3})([ptkhmPTKHM]?|[nN][gnGN]?)([1-8]?)$") #分拆的方式。
    
    #matching pattern，即略合POJ規範的音節
    match_pattern  = anal_pattern.match(syllable) 

    #重新檢核音節格式。不合白話字規定的音節視為不合 match_pattern。
    if re.match('^[^a-zA-Z0-9]+$', syllable): 
        match_pattern = None
    else:
        pass

    #不符合則不進行轉換動作（包含空白、連字號），只將它附加到輸出結果
    if not match_pattern:
        result = result + syllable
    
    #符合則替代基本字元
    else:
        #分拆略合POJ規範的音節。存成 list。
        #格式[聲母,母音,韻尾,數字音調]。如：['chh','e','ng','1']
        anal_syllable = list(match_pattern.groups())
        
        '''補上省略後的數字音調、或修改符號格式。'''
        if anal_syllable[3] == "":
            if re.match("[ptkhPTKH]",anal_syllable[2]): #陰入聲
                anal_syllable[3] = "4"
                
            else :#陰平聲
                anal_syllable[3] = "1"

        #因泉州方言的第六聲目前無統一的撰寫方式，故直接轉為第七聲。是為「陽上變去」。
        if anal_syllable[3] == '6':
            anal_syllable[3] = "7"
        
        if re.match("[nN]{2}",anal_syllable[2]): #鼻化音
            anal_syllable[2] = "ⁿ"

        '''將調號轉換為正常格式'''   
        
        '''無韻母（如 hng mng ）'''
        if anal_syllable[1] == "" : 
           if anal_syllable[3] == "2": #陰上
               
               #i.e. nasal_consonant_list。鼻音子音（不含ng）列表。
               nasal_cons_list = ['m', 'n', 'M', 'N']
               #轉換第二聲調值的鼻子音列表（ng不列）。
               converted_nasal_cons_list = ['ḿ', 'ń', 'Ḿ', 'Ń']
               
               for i in nasal_cons_list:
                   if re.match(i, anal_syllable[2][0]): #比對頭子音
                       if len(anal_syllable) == 1: #m2, n2
                           anal_syllable[2] = i
                       
                       else: #ng2
                           anal_syllable[2] = i + anal_syllable[2][1]
                       
                       break #以後的字母因為一定不合，不比了。
           
           elif anal_syllable[3] == '3': #陰去
               if len(anal_syllable[2]) == 1: #m3 or n3
                   anal_syllable[2] = anal_syllable[2] + '\xcc\x80'
               else: #ng3
                   anal_syllable[2] = anal_syllable[2][0] + '\xcc\x80' +\
                       anal_syllable[2][1]
                        
           elif anal_syllable[3] == '5': #陽平
               if len(anal_syllable[2]) == 1: #m5 or n5
                   anal_syllable[2] = anal_syllable[2] + '\xcc\x82'
               else: #ng5
                   anal_syllable[2] = anal_syllablep[2][0] + '\xcc\x82' +\
                       anal_syllable[2][1]
           
           #陽去和陽上（數字編號已轉換為7）
           elif anal_syllable[3] == '7' :
               if len(anal_syllable[2]) == 1: #m7 or n7
                   anal_syllable[2] = anal_syllable[2][0] + '\xcc\x84'
               else: #ng7
                   anal_syllable[2] = anal_syllable[2][0] + '\xcc\x84' +\
                       anal_syllable[2][1]                    
                
           elif anal_syllable[3] == '8': #陽入
               if len(anal_syllable[2]) == 1: #m7 or n7
                   anal_syllable[2] = anal_syllable[2][0] + '\xcc\x8d'
               else: #ng7
                   anal_syllable[2] = anal_syllable[2][0] + '\xcc\x8d' +\
                       anal_syllable[2][1]
                
           else: #陰平、陰入
               pass

        else: #有母音型
            '''轉寫規則（優先次序先到後排）：
            i- ,u- 雙母音，i u 不記調號。但 iu 則記調號於 u上。(IÚ)
            三母音或兩個母音後面加塞爆音或鼻音，則記於第二母音。 (koān, huâi)
            其餘標於第一母音。
            '''
            if len(anal_syllable[1]) == 1: #單母音
                anal_syllable[1] = vowel_add_mark(anal_syllable[1])  #加母音
                
            elif len(anal_syllable[1]) == 2: #雙母音
                if re.match('[iI][uU]',anal_syllable[1]): #iu
                    anal_syllable[1] = anal_syllable[1][0] + \
                        vowel_add_mark(anal_syllable[1][1])
                
                #oo, ou-> 加調號並加右上角小點（葫蘆點） 
                elif re.match('[oO][ouOU]',anal_syllable[1]): 
                    anal_syllable[1] = vowel_add_mark(anal_syllable[1][0])+\
                        '\xcd\x98'
                
                #i- & u- ,except iu-            
                elif re.match('^[iuIU].$', anal_syllable[1]): 
                    anal_syllable[1] = anal_syllable[1][0] + \
                        vowel_add_mark(anal_syllable[1][1])
                
                #韻母（母音加韻尾）字數不小於 3。
                #對雙母音而言，即有韻尾（但不考慮鼻化音）
                elif anal_syllable[2] != '' and anal_syllable[2] != 'ⁿ': 
                    anal_syllable[1] = anal_syllable[1][0] + \
                        vowel_add_mark(anal_syllable[1][1])
                            
                else:  #oa, oe ->調號標於o
                    anal_syllable[1] = vowel_add_mark(anal_syllable[1][0])+\
                        anal_syllable[1][1]
            
            else: #三母音
                anal_syllable[1] = anal_syllable[1][0] +\
                    vowel_add_mark(anal_syllable[1][1]) +\
                    anal_syllable[1][2]
                        
    #將聲母、母音、韻尾加入result。
        result = result + anal_syllable[0] + anal_syllable[1] +\
            anal_syllable[2]
    
print result
