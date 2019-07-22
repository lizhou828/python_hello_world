import urllib.request
print ("downloading with urllib")
url = 'http://www.landchina.com/styles/fonts/vcWMpM88o1GOYCKCpDtZpdu9PwXUDNJM.woff'
f = urllib.request.urlopen(url)
data = f.read()
with open(r"C:\Users\lizhou\Downloads\vcWMpM88o1GOYCKCpDtZpdu9PwXUDNJM.woff", "wb") as code:
 code.write(data)