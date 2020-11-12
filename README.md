# test_demo 2
Step 1: when a user goes to clarity site   https://clarity.dexcom.com 
Step 2: clarity makes login req “ https://uam1.dexcom.com/identity/login?signin=191289949e66b5517b0fc7d7c3af01ad"
Step 3: it has a redirect 302 sign in url
Step 4: user lands on uam login page and enters credentials and login
Step 5: user goes back to clarity site and has a code in it “:https://clarity.dexcom.com/users/auth/dexcom_sts/callback?code=00c39a0c4412353b73ea6c6df02f7968&state=4b966844132ad18cd8fe589ad50101217d1dfcd026c5d186&session_state=1V6DxFGHSoHwXm8TJ3QG0iYfDcghbZV4PJD4RJRTCCQ.7d510d56af4faff75c01112ccefc1f1e”
Step 6: according to auth code flow, using above code client makes a call to token endpoint to get a token
Step 7: that token is used to make Post call to session url
Request URL: https://clarity.dexcom.com/api/subject/1681277794575765504/analysis_session
Request Method: POST
Status Code: 200 OK

Note: i could not see the /token call in network tab. Hence i cannot put that step in code challenge







