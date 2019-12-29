
from urllib.request import urlopen
from xml.etree.ElementTree import parse

var_url = urlopen('http://py4e-data.dr-chuck.net/comments_347827.xml')
xmldoc = parse(var_url)
all_number = []
for item in xmldoc.iterfind('comments/comment'):
    # name = item.findtext('name')
    count = item.findtext('count')
    all_number.append(count)

allsum = sum([int(i) for i in all_number])

print(allsum)
