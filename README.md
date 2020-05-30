# twiliowhatsapp

This is a simple project to get you setup with Whatsapp BOT.
Since Whatsapp API is limited to Medium and Large Scale organizations, we would be using the sandbox provided by Twilio.
We will be hosting our webapp in Heroku.

This project is made in Python.

Before starting up, please make sure that you have Python installed in your machine, and its PATH added to your environment.

For Mac users, you would already have Python2 installed, which is an older version. Mac supports multiple versions of Python simultaneously.
Download the latest Python in your machine and configure the environment variables.

Check https://www.architectryan.com/2012/10/02/add-to-the-path-on-mac-os-x-mountain-lion/ for configuring environment variables in Mac.

You would also need an account with Twilio(VAS Provider). 

Since, we would need to host our app in the web, we would need a cloud platform. We will be using Heroku for this, as its quite easy to setup.

Heroku is quite easy to setup. Go to Herkoku.com, and sign up for a free account. 
Create a new project in Heroku, and do install Heroku CLI(Command Line Interface) Tools. Find the steps in this link https://devcenter.heroku.com/articles/heroku-cli

After installing Heroku, using command line interface, login to Heroku from terminal using command "heroku login"
Enter command -> git clone https://github.com/deepankarboro/twiliowhatsapp.git for cloning this project to your local machine. Pls make sure you have GIT CLI installed in your machine. Get inside your project directory using "cd" command.

Enter command -> heroku git:clone -a <application name> to let heroku point to your cloud project.
Inside the project, use command -> source botenv/bin/activate to activate the virtual environment for your project. If you don't have "venv" installed, please make sure to install it.

All the required libraries will already be there in "requirements.txt" file.
Use command -> git add . 
Then -> git commit -m "commiting to web server"
Then -> git push heroku master (This is for pushing the project to heroku)
Check if there are any error by typing "heroku logs"

There is one more thing which you need to do before people can use whatsapp to interact with your BOT.
You will need to create an account with twilio.

Login to your twilio console, and go to "Programmable SMS"->"Whatsapp"->"sandbox"
Make sure to put your heroku project cloud link. (This can be found under settings in your particular project which would see like https://<project name>.heroku.com

Make sure to insert the link through which webhooks will sent via your web hosted app to whatsapp. Under sandbox configuration in Twilio, you will find a text box with "WHEN A MESSAGE COMES IN" In the cell value, enter https://<project name>.heroku.com/bot Make sure to keep the method as "HTTP Post"

For your BOT to work, you will have to send a joining keyword, which would be defined for that whatsapp number in twilio itself. It will be something like "join <keyword>". Pls send this to the sandbox number provided by twilio. You can now interact with your BOT.

Do let me know if you have any issues during deployment.
Voila! You're done with the project now. 
