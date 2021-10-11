

def getRidOfTag(name):
  index = name.find('#')
  return name[:index]

def campquote(talker):

  campquotes = ['name is so idiot!', 'why are you even typing, name','OMEGALUL imagine being in here, name!']
  new_campquotes = []

  for quote in campquotes:
    new_quote = quote.replace('name', getRidOfTag(str(talker)))

    new_campquotes.append(new_quote)
  return new_campquotes