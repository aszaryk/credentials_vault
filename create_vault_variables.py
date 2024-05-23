import sys
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC
from veracode_api_py.dynamic import ScannerVariables



def update_variables():

    
   #CODE TO RETRIEVE SECRETS FROM YOUR CREDENTIALS VAULT HERE
   #
   #
   #
   ############################################





   #CODE TO CREATE CREDENTIAL VARIABLES IN VERACODE

    description = "Login Credentials for Application 1234"  #These should be assigned to variables being retrieved from your vault
    reference_key = "NEW_PASSWORD_KEY"
    value = "test_password_12345"

    print ('Creating Credentials Variables in Veracode')

    create_variables = ScannerVariables().create(reference_key,value,description)

def main():
    update_variables()

if __name__ == "__main__":

    main()