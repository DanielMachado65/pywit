from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
from wit import Wit

# if len(sys.argv) != 2:
#     print('usage: python ' + sys.argv[0] + ' <wit-token>')
#     exit(1)
# access_token = sys.argv[1]
# acess server KVK4NH345RMGO4FW7U7U3PBYWPTOY2XS
# client acess token 4MIYOOWP2X6552JH5CPPYIS6CLT63AEW

if __name__ == '__main__':
    print("start")
    try:
        client = Wit(access_token="KVK4NH345RMGO4FW7U7U3PBYWPTOY2XS")
        resp = client.message("ola meu consagrado")
        print(resp)
    except Exception as error:
        repr(error)
