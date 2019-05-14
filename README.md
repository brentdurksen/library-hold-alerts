# Calgary Public Library Hold Alerts

The Calgary Public Library allows patrons to pause a hold on a book.

This is great, because sometimes books I've been waiting for on hold for months come due when I'm not able to read them.

Unfortunately, they give you no warning that you're next on the list.

This little Python script scrapes hold data from the CPL website and sends email alerts any time you are next in line to receive a book on hold.

Run it on a very infrequent cron script - DON'T ABUSE THE LIBRARY WEBSITE by over-polling.
