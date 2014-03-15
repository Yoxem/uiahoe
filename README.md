uiahoe
======

converting POJ (Pe̍h-ōe-jī, a Romanization of Min Nan (aka. Hokkien) Chinese) with tone numbers to the formal form.

English
----------
The program that is used to convert POJ with tone numbers to the formal form can solve the problem. In addition, there are so many types of Romanization for Min Nan (Hokkien dialect), the program may be able to converters one type to another.

Pe̍h-ōe-jī (abbr. POJ) is a kind of Romanizations of Min Nan Chinese (including Taiwanese Min Nan). It was created in 19th Century.
(for more information of it, visit:https://secure.wikimedia.org/wikipedia/en/wiki/Pe%CC%8Dh-%C5%8De-j%C4%AB)

However, because there are plenty of computers without any IME for POJ to key in the vowels with tone mark and special characters, it's common forthe users of them to replace the tone marks and special characters with tone numbers and other alphabets when typing Min Nan with POJ. Nevertheless, it's not official.

The program that is used to convert POJ with tone numbers to the formal form can solve the problem. In addition, there are so many types of Romanization for Min Nan (Hokkien dialect), the program may be able to converters one type to another.

In Taiwanese Min Nan, Ú-iā-hoe (Chinese Character: 雨夜花 ,literally "A flower in a rainy night") is an old Min Nan song that is famous in Taiwan.

For other imformation, please visit:

Forum (mailing list and bug tracker): https://groups.google.com/group/uiahoe
Moved from the Bazaar repo: http://tcirc.org/~yoxem/script/uiahoe/src

Written on 2011-09-04 (or later)
Modified on 2014-03-16

Min Nan Chinese
----------------

*關於*

Ú-iā-hoe (Uiahoe) 是 chi̍t ê kā 閩南語白話字（Pe̍h-ōe-jī，簡稱 POJ） ê 數字音調 kah 替代文字變作正港 ê 白話字 ê program。

因足多電腦 lāi-té bo5 白話字 ê 輸入法，bo5 法度 phah 調號和特殊 ê 文字（如鼻化音 ⁿ 、葫蘆點 ͘）。因此，足多使用者 kā 聲調換作數字，用替代方式來 phah POJ 。但是，che lóng m̄ 是正港 ê 白話字寫法，所以我 tioh8 寫 chit ê program。

閩南語 ê 拼音有夠 chhē，chit-ê program 未來可能支援其他 ê 拼音。Che mā 是伊 ê 名 bo5 POJ 三 ê 字 ê 原因。可惜心力不足，需要看有 bo5 時間 iah8 是 tàu saⁿ-kang ê 人。

Ú-iā-hoe 是白話字對「雨夜花」ê 轉寫，是一首 uí 日本時代唱 káu 今 a2 日 ê 台灣閩南語老歌。而去掉聲調 kap 連字號了後，tioh8 變 Uiahoe ah。
*需要 ê 軟體
電腦語言 Python（第 2 版）ê 直譯器 (interpreter)。因為 Python tī 足多作業系統 lóng ē-ta3ng 安裝，所以 Linux、BSD、Windows、Mac OS X  等 ē-sái iōng。Download ê 所在 tī 遮：http://www.python.org/getit

請 download Python 2，mái download Python 3！

*安裝、使用 ê 方法*
Beh download ê 人請看 chhi̍t 頁。

Chi̍t ê program 免安裝，kā 伊 khǹg tī chit8 ê 目錄 tioh 可以 loh。

Phah 開終端機 ia̍h 是命令提示字元，入去伊所 tiàm ê 目錄後，phah：

    python uiahoe.py 要輸入的文字

若汝是 Windows 使用者，上行的 python 請換作「kheng3 Python ê 所在/python」。 假使汝 kā Python 安裝 kau3 C:\Python27 ，tioh8 ài 換作 C:\Python27\python 。

Kā 類 UNIX 系統（比如 Linux、Mac OS X），若 kā uiahoe.py 變作可執行，著 ē 使 m̄ 免 phah hiah 長 ê 指令：

    chmod u+x uiahoe.py #對此 script 加上可執行權限
    ./uiahoe.py 要輸入的文字

*使用範例*
汝 ē 使 phah 全羅（全 lóng 用白話字）ê 語句，m̄-koh 請記得：聲調用數字（1、4聲 ē 使免 phah）、o͘  換作 oo ia̍h 是 ou 、ⁿ 換作 nn 。比如：

    python uiahoe.py Chit peng5 si7 Toa7-ou5-kau2, hit-beng5 si7 Tiong-heng-liann2.

Ē 出現: Chit pêng sī Tōa-ô͘-káu, hit-bêng sī Tiong-heng-liáⁿ. （漢羅：這 pêng 是大湖口、hit-bêng 是中興嶺）

Phah 漢羅（漢字、白話字） mā 可以，但是 phah 替代文字 kah 聲調 ê 規定 mā kâng 款：

    python uiahoe.py In beh 去 toh？

Ē 出現： In beh 去 toh？ 

*錯誤、建議回報*
Chit-ê program 是無 lōa 久前寫 ê，可能有 chi̍t-kóa bug 。若有 bug ia̍h 是 建議，歡迎用 chit-ê 專案 ê 郵件討論區（mailing list）予 goa2 知。

Mailing list 是 chit8 款用寄 email 來討論 ê 方法。使用方法 kah 學生 beh 共同寫報告 ê 時陣，用 email 討論 kâng 款。Beh 回覆別人 ê 文章 a2-sī 回響，只要對伊寫的回 phoe tioh 可以。
Beh 訂 chit-ê mailing list ká 別人開講，請對 uiahoe-subscribe@googlegroups.com 寄 email，然後依確認 ê phoe ê 指示作；寫文章請寄 kàu uiahoe@googlegroups.com ；bô͘ 想 beh 訂 chit-gê mailing list，請對 uiahoe+unsubscribe@googlegroups.com 寄 email，然後依確認 ê phoe ê 指示作。

若無 kah-ì 用 email 討論，汝 mā ē-ēng kàu Google Group ê 網頁介面 (https://groups.google.com/forum/#!forum/uiahoe) 瀏覽 kah 回帖。

*註*
Che ui3 chit-e5 Bazaar repo 搬來: http://tcirc.org/~yoxem/script/uiahoe/src

Trad. Mandarin Chinese
---------------------------
*關於*

Ú-iā-hoe (Uiahoe) 是一個將閩南語白 話字（Pe̍h-ōe-jī，簡稱 POJ） 的數字音調和替代字元轉為正規白話字的程式。

因為許多的電腦並未內建白話字的輸入法，無法輸入調號和特殊字元（如鼻化音 ⁿ 、葫蘆點 ͘）。因此，許多使用者將聲調用數字標記，並用替代方式來輸入 POJ 。然而，這些畢竟不是正規的白話字寫法。這個程式於焉誕生。

有鑑於閩南語的拉丁化方案甚多，這程式未來可能支援其他的拼音方案。這也是這軟體名字裡沒有 POJ 三字的原因。不過心力不足，還要看有無閒暇或接手的人。

Ú-iā-hoe 是白話字對「雨夜花」的轉寫，這是一首從日治時代傳唱至今的台灣閩南語老歌。而移除聲調同連字號後，就變 Uiahoe 了。

*相依軟體*
程式語言 Python （第 2 版）的直譯器。由於 Python 在許多種作業系統下都能灌，Linux、BSD、Windows、Mac OS X 皆然。下載點於此：http://www.python.org/getit

請下載 Python 2，切莫下載 Python 3！

*安裝、使用法*
下載資訊請參此 頁

這程式不用安裝，只要將之放在一個目錄裡邊即可。

打開終端機或命令提示字元，進到它所在的目錄後，輸入：

    python uiahoe.py 要輸入的文字

對於 Windows 使用者而言，上行的 python 請用「Python 的安裝位置/python」 置換。如果您將 Python 灌在 C:\Python27 的話，則要改為 C:\Python27\python 。

在類 UNIX 系統下（如 Linux、Mac OS X），若將 uiahoe.py 設為可執行，則可以不用輸入那麼長的指令：

    chmod u+x uiahoe.py #對此 script 加上可執行權限
    ./uiahoe.py 要輸入的文字

*使用範例*
您可以用來輸入全羅（全白話字）的語句，但請記得聲調用數字（1、4聲 可略）、o͘ 用 oo 或 ou 輸入、ⁿ 用 nn 輸入。如：

    python uiahoe.py Chit-peng5 si7 Toa7-ou5-kau2, hit-beng5 si7 Tiong-heng-liann2.

會得到 Chit-pêng sī Tōa-ô͘-káu, hit-bêng sī Tiong-heng-liáⁿ. （註：上句的現代標準漢語譯為：「這邊是大湖口、那邊是中興嶺。」）

輸入漢羅（漢字白話字混用）也可以，但替代字元和聲調撰寫的規定如上：

    python uiahoe.py In beh 去 toh？

會得到 In beh 去 toh？ （註：上句的現代標準漢語譯為：「她們要去哪裡？」。此處他可用他、它等詞替代）

*錯誤、建議回報*
這個程式草創不久，應該會有一些 bug 。如果您遇到 bug 或是建議，歡迎利用這專案的郵件論壇（mailing list）與我們聯繫。

郵件論壇是一種利用電子郵件互寄來討論訊息的論壇。使用方法和學生小組要作集體報告時，用電子郵件討論訊息一樣。要回一個人的文章或迴 響，只要對其 寫的信傳封回信即可。
欲訂閱此論壇和其他人討論，請對 uiahoe-subscribe@googlegroups.com 傳封 email，並遵確認信指示操作；發文請寄到 uiahoe@googlegroups.com ；不想看到其他人的討論串和回覆時，請對 uiahoe+unsubscribe@googlegroups.com 傳封 email，並依確認信指示操作。

若不習慣電郵的討論方式，您也可至 Google Group 的網頁介面瀏覽並發文。


*註*
這是從此 Bazaar repo 搬來: http://tcirc.org/~yoxem/script/uiahoe/src

