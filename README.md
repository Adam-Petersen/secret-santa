# secret-santa
A python app I wrote to help organize the yearly Secret Santa game I participate in with friends.

## About
Every year my friends and I do a Secret Santa gift exchange. Secret Santa is a game between a group of people where every person is assigned another person in the group that they will get a personalized gift. When someone opens a gift, they try and guess the person that gifted it to them. I wanted to help out with the assignments by writing a script to algorithmically determine a random set of gift assignments. I also wanted the script to email every person in the group informing them of who they are assigned. I'm well aware there are several apps and websites that already handle this functionality and more, but I thought this would be a fun project to just do myself. Below is a list of functionality requirements that I wanted this app to satisfy.

1. Include an easy to set up configuration file that describes the following:
  * Encrypted address and password of the Gmail account that will be sending out the assignment emails.
  * The email subject and body of the email that will get sent out to all the group members when assignments are made
  * A list of all the people in the group and their corresponding email addresses.
  * Along with emails, there should be a list for each person that describes who they can't be assigned. This functionality is needed because we do Secret Santa every year, and it's nice to ensure that you will get a new person every year, and likewise the gift you receive will be from a new person every year.
2. Randomly generate a set of assignments
  * Every person must be assigned one other person
  * Every person must have one person assigned to them.
  * Essentially you can't have a scenario where both person A and person B are assigned person C because then someone in the group won't receive a gift and person C will receive two gifts.
  * A person can't be assigned themselves.
  * A person cannot be assigned someone in their "can't have" list.
  * Two people can't be assigned each other. In other words, the person you get a gift for can't get a gift for you.
  * If it's impossible to create a set of assignments meeting these criteria, the script should fail out.
3. Once the assignments are generated, login to the email account described in the configuration and send out an email to every person in the group informing them who they should get a gift for.
  * Look for the generic tags ```{person}``` and ```{target}```, then replace them with the email recipient’s name and who their target is.

## Usage
1. Clone the repo and cd into the newly created directory.
1. IMPORTANT: In order for the python script to sign into the sender's Gmail account, you must change some settings on the account to allow less secure apps (i.e. this script) to be allowed to sign in. You can change this setting here: https://support.google.com/accounts/answer/6010255?hl=en. Make sure "Less secure app access" is enabled for the account that will be sending the emails. After you're done using the app and everyone has their assignments, I'd recommend turning less secure app access off again.
1. Rename ```cfg.example.json``` to ```cfg.json```
1. Edit ```cfg.json``` and change the ```email_subject```, ```email_body```, and ```people``` fields as you see fit. The people field has some pre-populated examples to illustrate the required format. Don't worry about the ```sender_address``` and ```sender_password``` fields just yet.
1. Run the ```encrypt_email.py``` script. This script will encrypt your email address and password, output the encrypted results, and write the encryption key to the ```key.txt``` file in your current directory. Note that this app currently can only sign into Gmail accounts. Copy the outputted encrypted values of your email and password to the clipboard.
1. Edit ```cfg.json``` again by populating the previously empty fields ```sender_address``` and ```sender_password``` with the encrypted values you generated and copied in the previous step. The ```secret_santa.py``` script will automatically decrypt the values using the contents of ```key.txt``` as a key.
1. When ready, run ```secret_santa.py```. It will randomly create a set of assignments and prompt you when done if you are ready to send out the emails. Make sure everyone's email is entered into the cfg file correctly because you only want to run this script once.
1. If everything goes correctly, the emails should send out and everyone will be able to discreetly learn who they've been assigned for Secret Santa!

## Security
This app wasn't designed to be used by anyone other than myself, and I only uploaded this to Github because I'm happy with how it turned out. As such, if you decide to run this app yourself make sure to look through all the code and consider the risk involved around entering your email account information into a 3rd party app such as this. It may be a good (and fun!) idea to create a new gmail account dedicated to secret santa that you don't use for anything else. This is an especailly good idea considering the security settings you have to disable within google itself that could add potential risk to your email account. The email account and password encryption is all done client side and the login is done through a secure SMTP SSL connection, but don't take my word for it! Take a look at the code and see for yourself.
