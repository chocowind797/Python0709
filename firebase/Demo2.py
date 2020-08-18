from firebase import firebase

firebase = firebase.FirebaseApplication('https://victor0816-b5ab4.firebaseio.com/', None)
result = firebase.patch('/users2', {3: 'anita'})
print(result)
