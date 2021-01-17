def madlib1():
    Place = input('A Place: ')
    Adjective1 = input('A Adjective: ')
    Adjective2 = input('A Adjective: ')
    FemaleCelebrity = input('A Female Celebrity: ')
    MaleCelebrity = input('A Male Celebrity: ')
    Noun1 = input('A Noun: ')
    Noun2 = input('A Noun: ')
    Noun3 = input('A Noun: ')
    PluralNoun1 = input('A Plural Noun: ')
    PluralNoun2 = input('A Plural Noun: ')
    PluralNoun3 = input('A Plural Noun: ')
    PluralNoun4 = input('A Plural Noun: ')
    PluralProfession = input('A Plural Profession: ')

    text = 'Albert Einstein, the son of ' + MaleCelebrity + ' and ' + FemaleCelebrity + ', was born in Ulm, Germany, in 1879. In 1902, he had a job as assistant ' + Noun1 + ' in the Swiss patent office and attended the University of Zurich. There he began studying atoms, molecules, and ' + PluralNoun1 + '. He developed the theory of ' + Adjective1 + ' relativity, which expanded the phenomena of sub-atomic ' + PluralNoun2 + ' and ' + Adjective2 + ' magnetism. In 1921, he won the Nobel prize for ' + PluralNoun3 + ' and was director of theoretical physics at the Kaiser Wilhelm ' + Noun2 + ' in Berlin. In 1933, when Hitler became Chancellor of ' + Place + ', Einstein came to America to take a post at Princeton Institute for ' + PluralNoun4 + ', where his theories helped America devise the first atomic ' + Noun3 + '. There is no question about it: Einstein was one of the most brilliant ' + PluralProfession + ' of our time.'
    return text


print('===========')
print('| Mad Lib |')
print('===========')
print()
print('Inputs: ')
print('---------')
print()
result = madlib1()
print()
print(result)
