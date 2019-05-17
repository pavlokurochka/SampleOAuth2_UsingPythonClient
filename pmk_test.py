#%%
from app.models import Token
token1 = Token(access_token = 'AT', refresh_token= 'RT', realm_id = 'RI')
token1.save()

#%%
