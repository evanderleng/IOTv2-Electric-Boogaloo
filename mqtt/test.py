from receive import receive_messages
from publish import publish_messages
from google.oauth2 import service_account

#source_credentials = service_account.Credentials.from_service_account_file('credentials/credentials.json')


publish_messages("gungnir-249212", "data")

receive_messages()