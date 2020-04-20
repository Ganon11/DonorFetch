import argparse
import requests

def get_access_token():
  """Reads the access token from .accesstoken"""
  token = None
  with open('.accesstoken', 'r') as file:
    token = file.read().rstrip()
  return token

def make_tiltify_request(query_string):
  """Makes a request to tiltify"""
  url = make_tiltify_request.BASE_URL + query_string
  headers = { 'Authorization': f'Bearer {get_access_token()}' }
  return requests.get(url=url, headers=headers)

make_tiltify_request.BASE_URL = 'https://tiltify.com/api/v3/'

def get_campaign(campaign_id):
  query_string = f'campaigns/{campaign_id}'
  request = make_tiltify_request(query_string)
  print(request)

def get_donations(campaign_id):
  query_string = f'campaigns/{campaign_id}/donations'
  request = make_tiltify_request(query_string)
  print(request)

def main():
  parser = argparse.ArgumentParser()
  args = parser.parse_args()
  get_campaign('metroid_marathon')

if __name__ == "__main__":
  main()
