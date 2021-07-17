import json
import httpx
class FR24Request(object):


    def __init__(self, url, params = {}, headers = {}):

        self.url = url
        self.params = params
        self.headers = headers

    async def __send_request(self, url, params, headers):
        async with httpx.AsyncClient() as client:
            resp = await client.get(url,headers=headers,params=params)
        return  resp
         
    async def get_content(self):
        content = await self.__send_request(self.url,self.params,self.headers)
        return content

    # def get_content_type(self):