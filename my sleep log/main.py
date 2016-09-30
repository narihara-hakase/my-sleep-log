import fitbit
import gather_keys_oauth2 as Oauth2
import datetime
import numpy as np


"""for OAuth2.0"""
USER_ID = "227ZJZ"
CLIENT_SECRET = "2a0beb31d81a1b6a85e17c6be3bb1bd9"

"""for obtaining Access-token and Refresh-token"""
server = Oauth2.OAuth2Server(USER_ID, CLIENT_SECRET)
server.browser_authorize()
print('FULL RESULTS = %s' % server.oauth.token)
print('ACCESS_TOKEN = %s' % server.oauth.token['access_token'])

ACCESS_TOKEN = server.oauth.token['access_token']
REFRESH_TOKEN = server.oauth.token['refresh_token']

"""Authorization"""
auth2_client = fitbit.Fitbit(USER_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

"""Getting data"""
date=datetime.date(2016,9,27)
fitbit_stats = auth2_client.get_sleep(date)

"""Getting only 'heartrate' and 'time'"""
#stats = fitbit_stats['activities-heart-intraday']['dataset']
print(fitbit_stats)
"""Timeseries data of Heartrate
f1 = open('dataHR-timeseries.txt', 'w')
HR = []
for var in range(0, len(stats)):
    f1.write(stats[var]['time'])
    f1.write("\t")
    f1.write(str(stats[var]['value']))
    f1.write("\n")
    HR = HR + [stats[var]['value']]

f1.close()
HRmax = np.max(HR)
HRmin = np.min(HR)
plt.hist(HR, bins=len(stats), range=(HRmin,HRmax))
plt.show()"""