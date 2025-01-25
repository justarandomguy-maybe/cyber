import hashlib
from cryptography.fernet import Fernet
import base64
letters_order = [4,5,3,6,2,7,1,8]

bUsername_trial = b"FRASER"

hashed  =  hashlib.sha256(bUsername_trial).hexdigest()
flag = ""
for position in letters_order:
    flag +=hashed[position]


key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = flag
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
print(key_full_template_trial)
