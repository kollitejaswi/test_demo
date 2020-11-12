# test_demo 2

Step1 : We make a get call to  https://clarity.dexcom.com with username and password codechallenge / Password123

Step2: This makes a call Request URL: https://uam1.dexcom.com/identity/login?signin=191289949e66b5517b0fc7d7c3af01ad
Return status code : 302 
client_id: DAEC20AC-9626-4B0E-94B5-B674E298F51E
redirect_uri: https://clarity.dexcom.com/users/auth/dexcom_sts/callback
response_type: code
scope: openid profile offline_access
state: 09b94c281c2282fca5e7203024b327d8a115535bc2b9e588
ui_locales: en-US


Step 3:https://clarity.dexcom.com/users/auth/dexcom_sts/callback?code=00c39a0c4412353b73ea6c6df02f7968&state=4b966844132ad18cd8fe589ad50101217d1dfcd026c5d186&session_state=1V6DxFGHSoHwXm8TJ3QG0iYfDcghbZV4PJD4RJRTCCQ.7d510d56af4faff75c01112ccefc1f1e



Step 4:Request URL: https://clarity.dexcom.com/api/subject/1681277794575765504/analysis_session
Request Method: POST
Status Code: 200 OK



