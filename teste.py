import re
string = 'lalal lalal abc [] (teste).nes'
string2 = 'Boogerman.nes'
string3 = 'LA - ga.to(teste).ses'

teste = re.findall('^.[.\w\s-]+', string3)

print(teste)

