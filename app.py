import requests

cookies = {
    '_gcl_au': '1.1.1034163336.1762854750',
    '_ga': 'GA1.1.1798007406.1762854751',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-11-11%2009%3A52%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
    'sbjs_first_add': 'fd%3D2025-11-11%2009%3A52%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
    'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    '__stripe_mid': '22f5e4d9-5717-4dfc-989a-e2d5d34b8d6b6f9d69',
    'cookiehub': 'eyJhbnN3ZXJlZCI6dHJ1ZSwicmV2aXNpb24iOjEsImRudCI6ZmFsc2UsImFsbG93U2FsZSI6dHJ1ZSwiaW1wbGljdCI6ZmFsc2UsInJlZ2lvbiI6IiIsInRva2VuIjoiIiwidGltZXN0YW1wIjoiMjAyNS0xMS0xMVQxMDowMDowOS42MDhaIiwiYWxsQWxsb3dlZCI6dHJ1ZSwiY2F0ZWdvcmllcyI6W10sInZlbmRvcnMiOltdLCJzZXJ2aWNlcyI6W119',
    'sbjs_udata': 'vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Safari%2F537.36%20OPR%2F123.0.0.0',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fdonate%2F',
    '__stripe_sid': '6b543948-3f44-4fc2-b630-d9250c8f40aa14c6f9',
    '_ga_JY5DRMF51J': 'GS2.1.s1762858608$o2$g1$t1762858861$j60$l0$h0',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,id;q=0.5,fr;q=0.4,es;q=0.3,tr;q=0.2',
    'content-type': 'application/json',
    'origin': 'https://www.suffolkmind.org.uk',
    'priority': 'u=1, i',
    'referer': 'https://www.suffolkmind.org.uk/donate/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Opera";v="123", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 OPR/123.0.0.0',
    # 'cookie': '_gcl_au=1.1.1034163336.1762854750; _ga=GA1.1.1798007406.1762854751; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-11-11%2009%3A52%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2025-11-11%2009%3A52%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; __stripe_mid=22f5e4d9-5717-4dfc-989a-e2d5d34b8d6b6f9d69; cookiehub=eyJhbnN3ZXJlZCI6dHJ1ZSwicmV2aXNpb24iOjEsImRudCI6ZmFsc2UsImFsbG93U2FsZSI6dHJ1ZSwiaW1wbGljdCI6ZmFsc2UsInJlZ2lvbiI6IiIsInRva2VuIjoiIiwidGltZXN0YW1wIjoiMjAyNS0xMS0xMVQxMDowMDowOS42MDhaIiwiYWxsQWxsb3dlZCI6dHJ1ZSwiY2F0ZWdvcmllcyI6W10sInZlbmRvcnMiOltdLCJzZXJ2aWNlcyI6W119; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Safari%2F537.36%20OPR%2F123.0.0.0; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fdonate%2F; __stripe_sid=6b543948-3f44-4fc2-b630-d9250c8f40aa14c6f9; _ga_JY5DRMF51J=GS2.1.s1762858608$o2$g1$t1762858861$j60$l0$h0',
}

json_data = {
    'user_id': 0,
    'donationtype': '2',
    'donationamount': 5,
    'paymentmethod': 1,
    'donationmessage': None,
    'inmemoryof': None,
    'donationamountgiftaid': None,
    'giftaid': False,
    'forename': 'Spider Buoy',
    'surname': 'Lau Mnaree',
    'email': 'premiumwebs66@gmail.com',
    'title': 'Mr',
    'telephone': '6666666666',
    'address1': 'New York',
    'address2': 'NY',
    'town': 'NY',
    'county': 'US',
    'country': 'United State',
    'postcode': '10080',
    'marketing_optin_email': False,
    'marketing_optin_post': False,
    'marketing_optin_telephone': False,
    'marketing_optin_sms': False,
    'marketing_optin_privacy': True,
    'marketing_optin_newsletter': False,
    'user_age_range': None,
    'user_gender': None,
    'tribute_id': None,
    'giving_id': None,
    'newsletters_subscribe_array': [],
    'grecaptcha': '0cAFcWeA68Y97nx_J49cnCk9Ivd46yZxmzPHLyWk6_x6HVFyKBtZw2efUS1AaesJUDv-htGoIMWQ23hSeA4oiHQ_bFsJkx7OZ90jwIFL5tKCs25ZhNQImBP_o3TAznp9rVTLEUiONjl0RpmXmmP4yvM10bqe9UGU907eW8kqcY5G_lIbGarnNkktXxtKjOZe2gbFEEh6-stVL4DnUWjwkKuHWERMiWO5uOag8tMvUAymXdfHNYuZRZErWI0LN9SJdGgBuYDWMfy8oTuLMlhbXqE2LmPvCjip6Zi_HUvmWplXOHPYXR432HR6Cl-ZxuYltPz1Bu_Jb5EN-qkgOd2i3nRgouQL8KfoAmp_V5iAmlVHv1mmZGTxu9dwTTUMZg9EIi9zAaTO4P8DR9JGBzVSiJ8T-rWIM7URpRcGKQanXf55iNruN2G2BlMBVjQryfydKFuc22t2wyRV5b4Kj9fiXosDCWlv7DgBRbxdhDkLLSuyr1QtBVFv5h6Ah0ZXVX8PO8MtiXiCIQhyB8F0SU9szXnyG6P_rIh7CH4pZdnUmExy2MNItji4mJ63M3WRCqKkSwmyjKF_eGNNG0ZyAyVQlrNK9XPkEQbci-XMFChxLHbpY244wOD1aGtYUIPYzQai-9P7U7Ffe49Or5p6PZ8UgAZ7wRgrjfgvfwhNkhbsoAo5gUi55aq7fIFrKXUNtlISxFfzbwvj5NyNep4M0J5Kn0HtxBjaJ7JPvzMrmGUJySC5BCanjN36Ywl0qLuJ_3iTF1timBsEhEGltx1wX2WXsp7eb39wOJxuTJYzrWfebGi-uB4ABy3QiRsdvjQ587EpKWHEX6JP5GDDu6Hfnz12pEK2-D_0BakcJ9618GVtTYLMPwVF0zIyB6I57JlqwZix-_7N51c19qbqXjcGO2NtXA76gqF-BTjXhMn6UHVgCow-M93bj7F2q10m6lOeStwUMGyJ-XBIAVIWDDfLhzHn8VlRaXFVd5gPN1zPIOurflwaaHevp0nCXw4dOOWc8jngCF3VxVBykwhot_rm5EdjfrxQ9BhY5GiFEDsg2ctOEOU8stOvmkFoCsJ5UQhm9Cs7Ge5WihuHckg1pmtEynrSWEXvCHiqpNLdO4syp_aWIYPzeWN5lzX6Sds_04yHrMyXxVMjPtRST23DHnT2viwG5PBTOSreSHiX6XeAGul2G9SZlWZWtlB9wJLsStuaKHH8VNMA2E8P7Gl5s7qj6Y9Sa1QloRKV9RIYBfyRjK7GFSOrD5_sHMbD_f1VLm196ZjCYixOeTU9YCmhbmreIgB8rhpk5cJHRsj4grUcdv60JqvEnsiPzqdUNRzBluLVkLtg3vUaMb-e1FIfy7G_0sirqD7WojpdkKKd8yRED1YrGbIusNqmKTeJQD8VCCxLB6Q0laFYZb4EEKUtBvl3WXFz1cAI1ueS_CUo8xnJJ3iErUymnCCsaeu2lIDmt033CDo64es-qKBqhVSkZlnZNacl-L7Sv16Ww80iGuzij-cxydPHD9SErKG4leGw9629bxzCYWFsYA81X_u7jZ-NDQTL1ss4H1h9T_WrJ3lJKoB4qg1pvjoXy0duY4aCKW91CEECAbGTPSvn1FQppN9ByMYz3rJmMUlUwPnVNPkA',
    'ip_address': '185.244.9.104',
    'donation_error': False,
    'customdonationamount': '5',
}

response = requests.post(
    'https://www.suffolkmind.org.uk/wp-json/donation/v1/save/',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"user_id":0,"donationtype":"2","donationamount":5,"paymentmethod":1,"donationmessage":null,"inmemoryof":null,"donationamountgiftaid":null,"giftaid":false,"forename":"Spider Buoy","surname":"Lau Mnaree","email":"premiumwebs66@gmail.com","title":"Mr","telephone":"6666666666","address1":"New York","address2":"NY","town":"NY","county":"US","country":"United State","postcode":"10080","marketing_optin_email":false,"marketing_optin_post":false,"marketing_optin_telephone":false,"marketing_optin_sms":false,"marketing_optin_privacy":true,"marketing_optin_newsletter":false,"user_age_range":null,"user_gender":null,"tribute_id":null,"giving_id":null,"newsletters_subscribe_array":[],"grecaptcha":"0cAFcWeA68Y97nx_J49cnCk9Ivd46yZxmzPHLyWk6_x6HVFyKBtZw2efUS1AaesJUDv-htGoIMWQ23hSeA4oiHQ_bFsJkx7OZ90jwIFL5tKCs25ZhNQImBP_o3TAznp9rVTLEUiONjl0RpmXmmP4yvM10bqe9UGU907eW8kqcY5G_lIbGarnNkktXxtKjOZe2gbFEEh6-stVL4DnUWjwkKuHWERMiWO5uOag8tMvUAymXdfHNYuZRZErWI0LN9SJdGgBuYDWMfy8oTuLMlhbXqE2LmPvCjip6Zi_HUvmWplXOHPYXR432HR6Cl-ZxuYltPz1Bu_Jb5EN-qkgOd2i3nRgouQL8KfoAmp_V5iAmlVHv1mmZGTxu9dwTTUMZg9EIi9zAaTO4P8DR9JGBzVSiJ8T-rWIM7URpRcGKQanXf55iNruN2G2BlMBVjQryfydKFuc22t2wyRV5b4Kj9fiXosDCWlv7DgBRbxdhDkLLSuyr1QtBVFv5h6Ah0ZXVX8PO8MtiXiCIQhyB8F0SU9szXnyG6P_rIh7CH4pZdnUmExy2MNItji4mJ63M3WRCqKkSwmyjKF_eGNNG0ZyAyVQlrNK9XPkEQbci-XMFChxLHbpY244wOD1aGtYUIPYzQai-9P7U7Ffe49Or5p6PZ8UgAZ7wRgrjfgvfwhNkhbsoAo5gUi55aq7fIFrKXUNtlISxFfzbwvj5NyNep4M0J5Kn0HtxBjaJ7JPvzMrmGUJySC5BCanjN36Ywl0qLuJ_3iTF1timBsEhEGltx1wX2WXsp7eb39wOJxuTJYzrWfebGi-uB4ABy3QiRsdvjQ587EpKWHEX6JP5GDDu6Hfnz12pEK2-D_0BakcJ9618GVtTYLMPwVF0zIyB6I57JlqwZix-_7N51c19qbqXjcGO2NtXA76gqF-BTjXhMn6UHVgCow-M93bj7F2q10m6lOeStwUMGyJ-XBIAVIWDDfLhzHn8VlRaXFVd5gPN1zPIOurflwaaHevp0nCXw4dOOWc8jngCF3VxVBykwhot_rm5EdjfrxQ9BhY5GiFEDsg2ctOEOU8stOvmkFoCsJ5UQhm9Cs7Ge5WihuHckg1pmtEynrSWEXvCHiqpNLdO4syp_aWIYPzeWN5lzX6Sds_04yHrMyXxVMjPtRST23DHnT2viwG5PBTOSreSHiX6XeAGul2G9SZlWZWtlB9wJLsStuaKHH8VNMA2E8P7Gl5s7qj6Y9Sa1QloRKV9RIYBfyRjK7GFSOrD5_sHMbD_f1VLm196ZjCYixOeTU9YCmhbmreIgB8rhpk5cJHRsj4grUcdv60JqvEnsiPzqdUNRzBluLVkLtg3vUaMb-e1FIfy7G_0sirqD7WojpdkKKd8yRED1YrGbIusNqmKTeJQD8VCCxLB6Q0laFYZb4EEKUtBvl3WXFz1cAI1ueS_CUo8xnJJ3iErUymnCCsaeu2lIDmt033CDo64es-qKBqhVSkZlnZNacl-L7Sv16Ww80iGuzij-cxydPHD9SErKG4leGw9629bxzCYWFsYA81X_u7jZ-NDQTL1ss4H1h9T_WrJ3lJKoB4qg1pvjoXy0duY4aCKW91CEECAbGTPSvn1FQppN9ByMYz3rJmMUlUwPnVNPkA","ip_address":"185.244.9.104","donation_error":false,"customdonationamount":"5"}'
#response = requests.post('https://www.suffolkmind.org.uk/wp-json/donation/v1/save/', cookies=cookies, headers=headers, data=data)

print(response.json[id])

import requests

cookies = {
    '_gcl_au': '1.1.1034163336.1762854750',
    '_ga': 'GA1.1.1798007406.1762854751',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-11-11%2009%3A52%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
    'sbjs_first_add': 'fd%3D2025-11-11%2009%3A52%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
    'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    '__stripe_mid': '22f5e4d9-5717-4dfc-989a-e2d5d34b8d6b6f9d69',
    'cookiehub': 'eyJhbnN3ZXJlZCI6dHJ1ZSwicmV2aXNpb24iOjEsImRudCI6ZmFsc2UsImFsbG93U2FsZSI6dHJ1ZSwiaW1wbGljdCI6ZmFsc2UsInJlZ2lvbiI6IiIsInRva2VuIjoiIiwidGltZXN0YW1wIjoiMjAyNS0xMS0xMVQxMDowMDowOS42MDhaIiwiYWxsQWxsb3dlZCI6dHJ1ZSwiY2F0ZWdvcmllcyI6W10sInZlbmRvcnMiOltdLCJzZXJ2aWNlcyI6W119',
    'sbjs_udata': 'vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Safari%2F537.36%20OPR%2F123.0.0.0',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fdonate%2F',
    '__stripe_sid': '6b543948-3f44-4fc2-b630-d9250c8f40aa14c6f9',
    '_ga_JY5DRMF51J': 'GS2.1.s1762858608$o2$g1$t1762858861$j60$l0$h0',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,id;q=0.5,fr;q=0.4,es;q=0.3,tr;q=0.2',
    'content-type': 'application/json',
    'origin': 'https://www.suffolkmind.org.uk',
    'priority': 'u=1, i',
    'referer': 'https://www.suffolkmind.org.uk/donate/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Opera";v="123", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 OPR/123.0.0.0',
    # 'cookie': '_gcl_au=1.1.1034163336.1762854750; _ga=GA1.1.1798007406.1762854751; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-11-11%2009%3A52%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2025-11-11%2009%3A52%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; __stripe_mid=22f5e4d9-5717-4dfc-989a-e2d5d34b8d6b6f9d69; cookiehub=eyJhbnN3ZXJlZCI6dHJ1ZSwicmV2aXNpb24iOjEsImRudCI6ZmFsc2UsImFsbG93U2FsZSI6dHJ1ZSwiaW1wbGljdCI6ZmFsc2UsInJlZ2lvbiI6IiIsInRva2VuIjoiIiwidGltZXN0YW1wIjoiMjAyNS0xMS0xMVQxMDowMDowOS42MDhaIiwiYWxsQWxsb3dlZCI6dHJ1ZSwiY2F0ZWdvcmllcyI6W10sInZlbmRvcnMiOltdLCJzZXJ2aWNlcyI6W119; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Safari%2F537.36%20OPR%2F123.0.0.0; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fdonate%2F; __stripe_sid=6b543948-3f44-4fc2-b630-d9250c8f40aa14c6f9; _ga_JY5DRMF51J=GS2.1.s1762858608$o2$g1$t1762858861$j60$l0$h0',
}

json_data = {
    'amount': 5,
    'donation_id': 35273,
    'description': 'Suffolk Mind Donation',
    'email': 'premiumwebs66@gmail.com',
    'forename': 'Spider Buoy',
    'surname': 'Lau Mnaree',
}

response = requests.post(
    'https://www.suffolkmind.org.uk/wp-json/donation/v1/setup_stripe/',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"amount":5,"donation_id":35273,"description":"Suffolk Mind Donation","email":"premiumwebs66@gmail.com","forename":"Spider Buoy","surname":"Lau Mnaree"}'
#response = requests.post(
#    'https://www.suffolkmind.org.uk/wp-json/donation/v1/setup_stripe/',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)

yummy = [id]
print(yummy)

import requests

headers = {
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,id;q=0.5,fr;q=0.4,es;q=0.3,tr;q=0.2',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Opera";v="123", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 OPR/123.0.0.0',
}

data = 'payment_method_data[type]=card&payment_method_data[card][number]=4537702265573191&payment_method_data[card][cvc]=781&payment_method_data[card][exp_month]=07&payment_method_data[card][exp_year]=29&payment_method_data[guid]=0467659c-1673-43f1-b48b-084a40f1c9f7c9b535&payment_method_data[muid]=22f5e4d9-5717-4dfc-989a-e2d5d34b8d6b6f9d69&payment_method_data[sid]=6b543948-3f44-4fc2-b630-d9250c8f40aa14c6f9&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2F1253171c37%3B+stripe-js-v3%2F1253171c37%3B+split-card-element&payment_method_data[referrer]=https%3A%2F%2Fwww.suffolkmind.org.uk&payment_method_data[time_on_page]=280024&payment_method_data[client_attribution_metadata][client_session_id]=31c2b144-5a65-41fc-8b56-e08628518394&payment_method_data[client_attribution_metadata][merchant_integration_source]=elements&payment_method_data[client_attribution_metadata][merchant_integration_subtype]=split-card-element&payment_method_data[client_attribution_metadata][merchant_integration_version]=2017&expected_payment_method_type=card&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZCI6MCwiZXhwIjoxNzYyODU4ODU3LCJjZGF0YSI6IjBneDQ2R0NIOHVka1ZadmxjWjdyYm9sdWJPV1dkN09WbWl3Q1dGc1Fad2t0KzRFNXc2MTRYbUw4WDByWklmelBBZlg0QkR5U256cjczTmVNRUZGZ0VldDhVcTBUdmczM3QvczFYVUJjTlA4Q3M3aCs2c3BNK0ZlZXhkOG40OGhvWkJ3RlZnVk0zZmp5Y0l6MTQ4cXV6NEdEUll2K2l3ejdITGpqaVY2T3BXa2FWRlRGZ1ZMNEdyNnRqdHJqcmlRdU5ib2ltUzBMMkY0cXB3dnYiLCJwYXNza2V5IjoiK0x2TElmTGlza0FBTTREb2lFdlpmdFpzMi9zMk5hdm1IRC9HbnQ4Mi82d3BkRjlKczRQdXdtSWpnNzBBNDNWWUxldnNUa0V0cXQzSXl4YXUrRXk5OWEzaUVPMTU2N0FUcmFwZk5DNU9QZGxCVlhoMmN5bTVxU3pUL0NjYVhtWEdJVmZyNW1jOUQ5NDRvaVpBOUVFWTAzdTQ0SVlVUDlLQVdjWjUySXhKUXRCTDEvdzNjOXlZKzZNSEZOcmVGSG5oV1lydzdVNEpWSHRFb1lUWHZKYTcrZWllUHdDVHdiY0JoSGlaZldJdmF1V1VjK1U1TTg2Vjd2OVBOL3E4WW8yM3ljVVNUV1EzSUxnSzQrbEIyK0N6RUlJNW94T2FmQkRMNU13czcrQ2VsNG10eGd1YVVLZWdDYzNOdmt0UHZYMjkyQm5WUjRUMUI2S3BzVmNUYnl3aHRNdHRRcDRKRm5qd1h5WVRXWjZvRzg2OWlicks2dysxczNLa1lBaWh5eFpzaXp4MmRIOVFESU1zQjZrSGxwOGtKL2xGSFR6NGdQQ3NjcjVXSzdaQzZTdWxyNG1TazllazdMTy9vb1czL0xERlRGbEljeXBuaGo0eU5yNkJxVmpad0wvZGg0cGhPWm5NYng2S2ZacmhFc2Fpb25CR2pTZW5yR04zRnJLbm1YaWhzQlZwY3VZRTQ0Z3IreTQyUDQ0Z1ZMMmhpZGs4MHl6VmFoM0Q5RURzUXh5Zit6cGtJN1FpNzFxWmdrQzZDZWFoSW1ic2R4YlRPTEloVlFXdDJ5cEUxbGxIL0IzeHpseTFJVzJOeU4zbUNxUXRWT1g5RHo5RjlLaXpuQUh0d2l6bzlGZ3FVVUpLM2RLUTkrMG15R3FtVmFZUWdDY1NTUVRIU1VhNlVIRTBXOXMxQlNQN05nRDMwQ0NwSVdGZ2E4QXE5T0NoTmVCb05XWkhoZHVoM09vNUw1YUJvdTkrT3VvL0pYWUtHNXJROTUyRlpaWFZtbW5sR3ZyWkg4SFh5aWN5UjBJcTYvbjI1Vk9oVTJkZ3M1UFdmOEhlK0tUZlNrL0V1dkU0WWhmc1NSVjBJNUVweUhZMCszblNoa1JDR0ZIWldLcWdyOTNsUnpuZW1iNi91WGNEcXpwYlQ5blJOcFBrc2V2bHFXRkl5STFYZFQ3Vy9Fb1lxVEVhb3R0cXFSOFUrVFg2b3lQaEplRUlpTDM5cG5ncEZLS294L0hXQm9Ebk5udEZ1THFWTXl4d0U5eTh5TXFiV2QrWHlsUURuUHUxeG55VEd3YzN6MWk3RURtRmZyWWdrWjFBUjQ0SXZsVGhSTmkrQ0ZGWjkwVDBBZ05aT29KbnBsQUZzdGQ5RkRHYjdjVjA5RHFIODQ4VUlWWWZyUGVhRWxsUWE2VWh3S2c1UDhPR0ErL0lZdXVHM1RTaUpMa0x3UDZXM01zWFcwUWJoSmdjZjhNSUxacjQ0MjJyc2Y1WWFXNW1vWDdzQmh3VzVsWlcyc01ZN3l3UDhpYWV3alZtSEE5TFl1elM2cUY4RmZJR0ppcEJmN0JFMzJjNGt6a3RyNGEzUXY1TldaL00rN04xcGVSdzdLMFJ4VUtGeHdQTDloS3hpd1c3dVhEOW41QXJFY2ZZZjFCK290NllKWVA4ZlJlYWprOFhXcDZyWURMeTRFQS90YkZObjBUeVlvMTRwckZ3ZmVuOHpLb3FPajZNOTkxWEoxOThuS01OWWZTa0FJb1NwY1EzZHlZNlpYTmk4R21GOWhFRUswRFpBeVhYVTRnV201QzRiNExPMWk4MWl1S1NlMW9iSDVnblBENGhybEdhYlBWK3B4bEFKbmhoRlh4MkRLbDVyVjAvTWV3U0t3S2lxbm03RW9vU2VuV21SRXNhdHA1TkxlR0o4ZEhhUUNIRUxHdGp1ZWRGeUlPYS8zUDBPNUEyNU1POHRpeFFUeHI4cHpMWVNRQzRMSWdQMGxBZFRteXJwd1drellOaU5RWDZLc1VXYWhwRmZ6TWZtWUVWa2Q5Q0ErRW1LNExEc0ZxYjNNNTUyWVo1MTVMdEdleDd0clQ3YVlvNTA2WXVZTkNSRmRvc3dYVWhUUTZiZHB6K3JsVEdKeUM3aDVPZ1NJNFRyQU90Z25QT2p1d2hQRG1oTnhwdCtTcFNBQTg0L2IyQlg1SjVuSzJLaXdETFVxZ3FQSk8yL3NhaGJsdEF1Wkgwc0xOcDYwamlYakN4M0N5SHg5ZGw1NzgrL1pnYnk2T1d0bWMwdlFDK3lDTGFRRFVlVVNLSTlxQ0lmWW4zZ3Y4YmNVdnBkQzh0emJHQzlVeWJ6dVU1RlNOQmVhTEZ4ay8zMWxWQmYvZm5DVG8wSDdNcG5TQ21tdW1rK1hZWVczRzNmUzNkSGhvUklTWDRmWmxkbnFoUHpBTXlGTkhtWDJNQkdhY0hMTEZremhwZnJFOUNPVkhabVVHWE16dkNlRnhoNTJTZEJDendVOTF0RGVHaXdFZUZkdDBRVXhiN0V4RE1icTMvY3hBUGtXMUt5UWF2aDdxaXNvN2xjVHVEWnRRVGcvYU9ra1R0Si8zcDFTek0vVTFPb1drZGVlTDBtUGx1eklkaUhwV3JQZUV5UzRnQk4xbkQvQ29JRDFZWDJtRFdaWldCdXNvY1ErRUZPaWk2OXhpOGN1ckZwUHpzUUkxTGIzZjNtZDRSIiwia3IiOiIzYTcwYmJjMCIsInNoYXJkX2lkIjozMzk1MTAzMDN9.8a-uzJB9SPhKllCpRSBZpt1f6UYRiv0ragVeUxMkICw&use_stripe_sdk=true&key=pk_live_O45qBcmyO7GC7KkMKzPtpRsl&client_attribution_metadata[client_session_id]=31c2b144-5a65-41fc-8b56-e08628518394&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=split-card-element&client_attribution_metadata[merchant_integration_version]=2017&client_secret=pi_3SSFJuBI46WJQGRa0aPwRFkJ_secret_MZbuL7bSLNnGv3MCaiJxCLZWP'

response = requests.post(
    'https://api.stripe.com/v1/payment_intents/pi_3SSFJuBI46WJQGRa0aPwRFkJ/confirm',
    headers=headers,
    data=data,
)

print(yummy[id])
