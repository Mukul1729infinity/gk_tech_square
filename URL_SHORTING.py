from urllib.request import urlopen
from urllib.parse import urlencode
import contextlib
def make_sort_url(url):
    req_url="http://tinyurl.com/api-create.php?"+urlencode({'url':url})
    with contextlib.closing(urlopen(req_url)) as response:
        return response.read().decode('utf-8')
k=make_sort_url('ENTER YOUR URL')
print(k)
