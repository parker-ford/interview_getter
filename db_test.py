from tinydb import TinyDB, where

db = TinyDB('db_test.json')

title = 'test title'
company = 'test company'
url = 'test.com'
url2 = 'test2.com'
db.truncate()
job = {
    'title' : title,
    'company' : company,
    'description' : '',
    'URL' : url
}
#db.insert(job)
#db.insert({'title' : title, 'company' : company , 'URL' : url})
#print(len(db.search(where('URL') == url)))
