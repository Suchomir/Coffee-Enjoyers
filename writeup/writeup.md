# Coffee

In this task, you need to modify the cookie value in order to get a flag. Go to the "Contact" page on which you need to
send any email and feedback in order to gain a cookie with a discount coupon. Next, go to the shop page, turn on the burp in order to catch the HTTP request and click
"Buy now!" for any coffee you want. You will catch two HTTP requests, but you need to edit cookies only in the second request. When you set the value of the "discount" cookie
to "100" and submit the request you will get the flag.

> flag{c0ff3_m45t3r}
