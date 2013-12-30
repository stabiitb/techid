"""
The activation key for the ``UserProfile`` will be a
SHA1 hash, generated from a combination of the ``User``'s
email and a random salt.
 
"""
import hashlib
import random
def activation_code(email): 
	salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
	if isinstance(email, unicode):
		email = email.encode('utf-8')
		activation_key = hashlib.sha1(salt+email).hexdigest()
		return activation_key
	else:
		return None
