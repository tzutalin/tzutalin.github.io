import requests
import simplejson
import json
r = requests.get('https://api.github.com/users/tzutalin/repos')
c = r.content
j = simplejson.loads(c)

num_stars_show = 10

for item in j:
     stars_count = int(item['stargazers_count'])
     name = item['name']
     url = item['url']
     description = item['description']
     if stars_count > num_stars_show:
        description_start_index = description.rfind(': ')
        description = description[description_start_index+1:]
        print description
        print url
