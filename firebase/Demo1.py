from firebase import firebase

firebase = firebase.FirebaseApplication('https://victor0816-b5ab4.firebaseio.com/', None)
result = firebase.get('/users', 1)
print(result)
