from errbot import BotPlugin, botcmd, arg_botcmd, re_botcmd
import urllib.request
import json
import requests

class Count(BotPlugin):
    """Count things using http://countapi.xyz"""

    @arg_botcmd('key',type=str)
    def count_hit(self,msg,key=None):
        count=self.backend('hit',key)
        return key+' has now been accessed '+count+' times.'

    @arg_botcmd('key',type=str)
    def count_get(self,msg,key=None):
        count=self.backend('get',key)
        return key+' has been accessed '+count+' times.'

    def backend(self,type,key):
        url='https://api.countapi.xyz/'+type+'/wsoula/'+key
        page = urllib.request.Request(url)
        response = json.loads(urllib.request.urlopen(page).read().decode('utf-8'))
        return response['value']
