import boto3
import csv
from io import StringIO
import os
import json
import codecs

import pandas as pd
import transformation

dynamodb = boto3.resource('dynamodb')
s3 = boto3.resource('s3')
tableName = os.environ['table']
bucket = os.environ['bucket']
key = 'us.csv'
#key2 = 'jh.csv'


def extract():
   urlNYT = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv'
   urlJH = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv'

   transformation()

   

#def lambda_handler(event, context):
#   s3.Bucket(bucket).put_object(Key = 'us.csv', Body=dataNYT)
#   s3.Bucket(bucket).put_object(Key = 'jh.csv', Body=dataJH)

#   begin_load()




#def main():
#    lambda_handler()


#if __name__ == '__main__':
#    main()




#if upload to s3 == 200 continue to transform module 
#else throw error

#when transform is complete load data

