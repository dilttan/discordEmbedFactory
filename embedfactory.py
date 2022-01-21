import discord

def message_factory(form_name, *arg, **kwarg):
    
    #이 부분 조심하기
    output = eval(form_name)(*arg, **kwarg)
    return output

class formBase:
  def __init__(self, *arg, **kwarg):
    self.embed = discord.Embed()
    self.init_make()
    if arg is not None or kwarg is not None:
      self.insert(*arg, **kwarg)
      
  def init_make(self):
    pass
    
  def insert(self, *arg, **kwarg):
    pass
    
  @property
  def get(self):
    return self.embed
    
class embedExample(formBase):
  def init_make(self):
    self.embed.title = "📚 만든이 뒬탕#4842"
    self.embed.url = "https://discordbot.tistory.com/"
  def insert(self, message, *arg, **kwarg):
    self.embed.description = message
