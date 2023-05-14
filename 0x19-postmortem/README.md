# When Nginx Goes AWOL

On March 8, 2023, at 10:00 AM UTC, our website went down for an hour and a half. The culprit? A misconfigured Nginx web server.

## What happened?

We know what you're thinking: "Nginx? That's a pretty obscure web server. How did it even happen?"

Well, it all started with a simple change to our website's SSL certificate. An engineer made the change correctly, but they forgot to restart the Nginx web server after making the change. As a result, the Nginx web server was not listening on port 80 and users were unable to access the website.

## What did we learn?

We learned a few things from this experience:

* **Always restart the Nginx web server after making any changes to the configuration file.**
* **Don't let your guard down, even for simple changes.**
* **Always test your changes before making them live.**

## What can you do to avoid this?

If you're managing an Nginx web server, here are a few things you can do to avoid a similar outage:

* **Create a checklist for making changes to the Nginx configuration file.** This checklist should include steps for restarting the web server after making changes.
* **Use a version control system to track changes to the Nginx configuration file.** This will allow you to easily revert to a previous version of the file if something goes wrong.
* **Test your changes before making them live.** This can be done by using a staging environment or by testing the changes on a local machine.

## Contact us

If you have any questions about this post-mortem, please don't hesitate to contact us. We're always happy to help.

