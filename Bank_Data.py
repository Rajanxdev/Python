# Subscribe my youtube channel 
 import requests

 Ifsc_code = 'PUNB0102010'  #Change IFSC Code as per your requirement

 API_fatch = 'https://ifsc.razorpay.com/'

 Bank_data = requests.get(API_fatch + Ifsc_code).json()

 print(Bank_data)

