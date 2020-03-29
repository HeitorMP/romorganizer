from flashtext import KeywordProcessor

key_word = KeywordProcessor()

dict = {'teste': ['teste.nes', 'teste1.nes' , 'teste teste.nes']}
arq = 'teste'



print(key_word.get_all_keywords(dict))


