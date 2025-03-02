import json
import requests

def get_dog_facts(json_string: str) -> list:
    d = json.loads(json_string)
    # for i in d['data']:
    #     print(i['attributes']['body'])
    return [i['attributes']['body'] for i in d['data']]

def download_dog_facts():
    url = 'https://dogapi.dog/api/v2/facts?limit=3'
    response = requests.get(url)
    response_content = response.content.decode('utf-8')
    return response_content


def test_get_dog_facts():
    arg = '''\
{
  "data": [
    {
      "id": "574c4504-250f-4743-9ff2-124e5c61e79e",
      "type": "fact",
      "attributes": {
        "body": "Dogs live an average of 15 years."
      }
    },
    {
      "id": "cd131ea1-3327-4c2c-93e6-488582a3e2e7",
      "type": "fact",
      "attributes": {
        "body": "Dogs have a wet nose to help them absorb scents."
      }
    },
    {
      "id": "58d82e49-0b2f-4911-bdde-0d686e092b72",
      "type": "fact",
      "attributes": {
        "body": "Dogs can see in color, but not as vividly as humans."
      }
    }
  ]
}
'''
    expected = [
        'Dogs live an average of 15 years.',
        'Dogs have a wet nose to help them absorb scents.',
        'Dogs can see in color, but not as vividly as humans.',
    ]
    actual = get_dog_facts(arg)
    assert expected == actual
    print('Tests passed!')

if __name__ == '__main__':
    test_get_dog_facts()
    json_string = download_dog_facts()
    facts = get_dog_facts(json_string)
    print('\n'.join(facts))