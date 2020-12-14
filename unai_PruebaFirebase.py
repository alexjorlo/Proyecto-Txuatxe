from firebase import firebase

firebase = firebase.FirebaseApplication("www.txuatxe.es ")
result = firebase.get('/usuarios_gym','')
print(result)