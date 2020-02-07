
import requests
from ApiExceptions import ApiException

def _url(path):
    return 'http://api.open-notify.org/' + path


def get_astros():
    return requests.get(_url('astros.json/'))

if __name__ == '__main__':

    try:
        resp = get_astros()
        if resp.status_code is None:
            raise ApiException('nothing returned')
        elif resp.status_code != 200:
            raise ApiException('200 not returned')
        #else:
        #    raise ApiException('{} returned instead'.format(resp.status_code))

    except ApiException as e:
        print(e.code, end=", ")
    finally:
        if resp is not None:
            print(resp.json())
        else:
            print('No response')
