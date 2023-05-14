When Nginx Goes AWOL
On March 8, 2023, at 10:00 AM UTC, our website went down for an hour and a half. The culprit? A misconfigured Nginx web server.
We know what you're thinking: "Nginx? That's a pretty obscure web server. How did it even happen?"
Well, it all started with a simple change to our website's SSL certificate. An engineer made the change correctly, but they forgot to restart the Nginx web server after making the change. As a result, the Nginx web server was not listening on port 80 and users were unable to access the website.
We know, we know. It's a rookie mistake. But hey, we're all human. And at least we can laugh about it now.
Here's a few things we learned from this experience:
Always restart the Nginx web server after making any changes to the configuration file.
Don't let your guard down, even for simple changes.
Always test your changes before making them live.
We hope you learned a thing or two from our experience. And if you ever find yourself in a similar situation, just remember: it could always be worse. You could be the engineer who accidentally deleted the entire production database.
Call to Action:
If you have any questions about this post-mortem, please don't hesitate to contact us. We're always happy to help.
alx-system_engineering-devops
