# Email-hell
Are you tired of Getting spam from a specific email address?  Use this Python script to email them back in an automated fashion

# step 1

edit the config.py.  Add in the addresses of your ~~victims~~ -er recipients wrapped in quotes, one per line, separated by a comma.

# step 2

Add in your own AUTH credentials - if you don't understand what this is or have never setup a client email reader like thunderbird or outlook **stop**, you probably don't know what you're doing anyway.


# step 3

Run it!  visit your Charlie Michael Davis prompt or Terminal: `python emailHell.py` and watch the sparks fly as your ~~victim's~~ recipient's email address is flooded.


# Notes

I did this becuase I was pissed off and didn't see the shiny little opt-out link on the bottom of an email I get sometimes from the same group.  I figured, why not have some fun and wrote this as a word of warning against spamming me.  This was all made in good fun and as such I'm sharing it here on github.  Mitigate damage from this script by blocking or blacklisting the sender.  The script has a limiter of 2 seconds so that your email provider does not timeout and reject messages - conceivably that equates to approximately just under 1200 emails per hour give or take processing speed out of the equation: You do the math...no?....okay well that's just under ~~29 THOUSAND~~ emails per day...imagine the fun we could have if we simply added on a padded 6MB file for each send?  One hour of sending messages would equal 7.2 GB of email.  How large are the free gmail accounts again?  Last time I checked, most email provisioning services impose a limit of about 500 MB on autoconfigured boxes.

# 1337 notes

This is really just a baseline template to what *could* be created if you have the time and imagination.  For instance, if you could provision accounts on will, then conceivably you could create a list of authentication credentials and iterate through the credentials for each email listed in the config.  If you wanted, you could rotate a list of messages and iterate through a random message each time so that each email receives a different message on each pass - making it harder to blacklist based on custom email rules like message and address filters.
