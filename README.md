# WhatsappGroupCreator
A python project that automatically fetches contacts from a google sheet and creates a whatsapp group with that contacts list

# How it works
  The GetContacts script uses the gspread api to access the google sheet with the contacts list which must be 
  shared with the api's service account's email address. It then produces a list of phone numbers and names.
  
  The CreateContact script takes the lists from GetContacts, using selenium, adds all the contacts to your google contacts
  via and automated chrome tab.
  
  Then once the contacts are synced with whatsapp on your phone, the CreateGroup script uses another chrome instance to
  create a whatsapp group via whatsapp web.
  
# How to Use
  1. Create a google service account via GCP console.
  2. Download it's credentials json file, and place it in the venv directory along with other python scripts.
  3. Rename the credentials file to 'client-secret.json'.
  4. Open the client-secret, copy the email address, go to the google sheet where contact info is stored, and
      share it with the copied email.
  5. Run the CreateContact script, it will ask you to login to google, do that, and wait till all contacts are added.
  6. Check your phone, wait till everything syncs and all the added contacts are shown in the whatsapp contacts list.
  7. Run the CreateGroup script and login to whatsapp web.
  8. Relax and let python do the work.
  
# Limitations
  This script currently doesn't handle duplication of contacts, so if there exists a dupicate contact, it won't
  successfully create the group and some human correction would be required. 
  Also, this script doesn't delete the added contacts but it makes it easy for the user to delete it if he chooses to.
 
Happy texting :)
