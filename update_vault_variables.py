import sys
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC
from veracode_api_py.dynamic import ScannerVariables



def update_variables():

    
   #CODE TO RETRIEVE SECRETS FROM YOUR CREDENTIALS VAULT HERE
   #
   #
   #
   ############################################



   #CODE TO UPDATE CREDENTIAL VARIABLES IN VERACODE
    all_variables = ScannerVariables().get_all()
    reference_key = "NEW_MY_PASSWORD_KEY" # This is the name of the variable you wish to update 
    new_password = "Newpassword1" # The value of your new variable (ie, username, password etc.)

    for variable in all_variables:
        if variable['reference_key'] == reference_key:
            description = variable['description']
            guid = variable['scanner_variable_id']
            update_variable = ScannerVariables().update(guid,reference_key,new_password,description)
            print("Successfully updated variable: " + variable['reference_key'] + " with guid: " + variable['scanner_variable_id'])
            return
    else:
        print("Scanner Variable with Reference Key " + reference_key + " not found.")

def main():
    update_variables()

if __name__ == "__main__":

    main()