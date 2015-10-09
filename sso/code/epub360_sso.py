from Crypto.Cipher import AES
import base64
import hashlib
import urllib
import operator
import array
import simplejson as json

message = {
    'expires':'2019-05-30 21:01:43',
    'email':'rich@acme.com',
    'avatar_url':'http://acme.com/users/1234/avatar.png',
    'display_name':'Richard White',
    'guid':'1234'
}
block_size = 16
mode = AES.MODE_CBC


domain = 'FILL IN'

sso_key = "FILL IN"

iv = "OpenSSL for Ruby"

json = json.dumps(message, separators=(',',':'))
print "JSON: " + json

salted = sso_key+domain
saltedHash = hashlib.sha1(salted).digest()[:16]
print "SaltedHash: " + base64.encodestring(saltedHash)

json_bytes = array.array('b', json[0 : len(json)]) 
iv_bytes = array.array('b', iv[0 : len(iv)])

# # xor the iv into the first 16 bytes.
for i in range(0, 16):
	json_bytes[i] = operator.xor(json_bytes[i], iv_bytes[i])
print "XOR'ed data: " + json_bytes.tostring()

pad = block_size - len(json_bytes.tostring()) % block_size
data = json_bytes.tostring() + pad * chr(pad)
aes = AES.new(saltedHash, mode, iv)
encrypted_bytes = aes.encrypt(data)
token_for_epub360_sso = urllib.quote(base64.b64encode(encrypted_bytes))

print "TOKEN: " + token_for_epub360_sso
