from twilio.rest import Client 
 
account_sid = 'account_sid' 
auth_token = 'auth_token' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+12028732337',  
                              body='Hey! It\'s working!',      
                              to='+4*********' 
                          ) 
 
print(message.sid)  