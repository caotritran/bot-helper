import time
from errbot import BotPlugin, botcmd
from sys import exit
import requests, json, urllib3, os
from tabulate import tabulate

from dotenv import load_dotenv
load_dotenv('.env')

JENKINS_API_TOKEN = os.environ['JENKINS_API_TOKEN']

class JENKINS(BotPlugin):
    """
    Help us to intergrate with CF API, syntax: /jenkins <cmd>
    """
    
    @botcmd(split_args_with=None)
    def jenkins_findrootip_offshore(self, msg, args):
        ip_offshore = args[0]
        URL = "http://jenkins.sweb.vn/job/sweb/job/Check_IP_From_Offshore"

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = 'json={"parameter": [{"name":"hosts", "value":"%s"}]}' % (ip_offshore)

        response = requests.post(URL+"/build", headers=headers, data=data, auth=('admin', '{}'.format(JENKINS_API_TOKEN)))

        output_url = URL + "/lastBuild/consoleText"

        if response.status_code == 201:
            text = "Send trigger build to jenkins success\nGenarating output - please wait ..."
            self._bot.send_simple_reply(msg, text, threaded=True)
            time.sleep(40)
            console_output = requests.get(output_url, auth=('admin', '{}'.format(JENKINS_API_TOKEN)))
            output_text = console_output.text
            self._bot.send_simple_reply(msg, output_text, threaded=True)
            

        else:
            text = "Send trigger build to jenkins fail\n @tritran14 oi vao check ne` !!!"
            self._bot.send_simple_reply(msg, text, threaded=True)
            time.sleep(40)
            console_output = requests.get(output_url, auth=('admin', '{}'.format(JENKINS_API_TOKEN)))
            output_text = console_output.text
            self._bot.send_simple_reply(msg, output_text, threaded=True)
