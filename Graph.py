import urllib2
import json

class Graph(object):
   
   url = 'https://www.cryptocompare.com/api/data/coinlist/'
   coins = ['btc', 'eth', 'ltc']


   def getDirtyData(self):
      dirtyCryptoData = urllib2.urlopen(self.url).read()      
      dirtyCryptoDataJson = json.loads(dirtyCryptoData)
      return dirtyCryptoDataJson

   def clint(self, dd):
     data = dd['Data']
     dat  = { key: data[key] for key in [x.upper() for x in self.coins] }

     for k, v in dat.items():
        print k
        print v

   def run(self):
      dirtyData = self.getDirtyData()
      self.clint(dirtyData)


if __name__== '__main__':
   Graph().run()
