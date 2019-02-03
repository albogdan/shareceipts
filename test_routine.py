from people import friend
from item import item
import requests

a = friend('Zach', 'LaPointe', 'zachary.lapointe@gmail.com')
b = friend('Sidd', 'Vijay', 'siddharth.vijay333@gmail.com')
c = friend('Alex', 'Bogdanal', 'pepperketchup@gmail.com')
d = friend('Karen', 'Zhao', 'karen.12345678@hotmail.com')

z = item('Bibimbap', 12.25, 13, 12)
y = item('Eggs Benedict', 9.90, 13, 13)
x = item('Peach Mimosa', 20.00, 15, 13)
w = item('Fully Loaded Poutine', 19.99, 13, 13)

print(w)
print(a)

z.add_friend(b)
y.add_friend([a,d])
x.add_friend([a,b,c,d])
w.add_friend([c,d,b])

w.remove_friend(a)
w.remove_friend(b)
#
# z.assign_prices()
# y.assign_prices()
# x.assign_prices()
# w.assign_prices()

# mass call for output
list(map(lambda x:x.assign_prices(), (w, x, y, z)))

print(a.out())
print(b.out())
print(c.out())
print(d.out())

url = "https://mchacks6.appspot.com/v1/request-money"

headers = {
   'Content-Type': "application/json",
   'cache-control': "no-cache",
   'Postman-Token': "d09e9d2c-cd69-429d-81b0-6669b3f7402e"
   }

# response = requests.request("POST", url, data=a.interac_request(), headers=headers)
#
# print(response.text)

#mass requests
response_list = list(map(lambda x:requests.request("POST", url, data=x.interac_request(), headers=headers),(a, b, c, d)))
list(map(lambda x:print(x.text), response_list))
