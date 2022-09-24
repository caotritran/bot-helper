from ast import arg
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
        """_syntax: /jenkins findrootip offshore <ip>"""
        if len(args) < 1 or len(args) > 1:
            text = "`invalid syntax, _syntax:  /jenkins findrootip offshore <ip>`"
            self._bot.send_simple_reply(msg, text, threaded=True)
            return
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


    @botcmd(split_args_with=None)
    def jenkins_coverip_offshore(self, msg, args):
        """_syntax: /jenkins coverip offshore <domain_name> <root_ip> <offshore_ip>"""
        if len(args) < 3 or len(args) > 3:
            text = "`invalid syntax, _syntax: /jenkins coverip offshore <domain_name> <root_ip>`"
            self._bot.send_simple_reply(msg, text, threaded=True)
            return

        domain_name = args[0]
        root_ip = args[1]
        offshore_ip = args[2]

        URL = "http://jenkins.sweb.vn/job/sweb/job/Offshore_Cover/"

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = 'json={"parameter": [{"name":"HOSTS", "value":"%s"}, {"name":"Domain", "value":"%s"}, {"name":"RootIP", "value":"%s"}]}' % (offshore_ip, domain_name, root_ip)

        response = requests.post(URL+"/build", headers=headers, data=data, auth=('admin', '{}'.format(JENKINS_API_TOKEN)))

        output_url = URL + "/lastBuild/consoleText"

        if response.status_code == 201:
            text = "Send trigger build to jenkins success\nGenarating output - please wait ..."
            self._bot.send_simple_reply(msg, text, threaded=True)
            time.sleep(150)
            console_output = requests.get(output_url, auth=('admin', '{}'.format(JENKINS_API_TOKEN)))
            output_text = console_output.text
            self._bot.send_simple_reply(msg, output_text, threaded=True)
            

        else:
            text = "Send trigger build to jenkins fail\n @tritran14 oi vao check ne` !!!"
            self._bot.send_simple_reply(msg, text, threaded=True)
            time.sleep(150)
            console_output = requests.get(output_url, auth=('admin', '{}'.format(JENKINS_API_TOKEN)))
            output_text = console_output.text
            self._bot.send_simple_reply(msg, output_text, threaded=True)


    @botcmd(split_args_with=None)
    def jenkins_createssl(self, msg, args):
        """_syntax: /jenkins createssl <root_ip> <domain_name>"""
        if len(args) < 3 or len(args) > 3:
            text = "`invalid syntax, _syntax: /jenkins createssl <root_ip> <domain_name>`"
            self._bot.send_simple_reply(msg, text, threaded=True)
            return

        root_ip = args[0]
        domain_name = args[1]

        URL = "http://jenkins.sweb.vn/job/sweb/job/Create_SSL/"

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = 'json={"parameter": [{"name":"HOSTS", "value":"%s"}, {"name":"Domain", "value":"%s"}' % (root_ip, domain_name)

        response = requests.post(URL+"/build", headers=headers, data=data, auth=('admin', '{}'.format(JENKINS_API_TOKEN)))

        output_url = URL + "/lastBuild/consoleText"

        if response.status_code == 201:
            text = "Send trigger build to jenkins success\nGenarating output - please wait ..."
            self._bot.send_simple_reply(msg, text, threaded=True)
            time.sleep(50)
            console_output = requests.get(output_url, auth=('admin', '{}'.format(JENKINS_API_TOKEN)))
            output_text = console_output.text
            self._bot.send_simple_reply(msg, output_text, threaded=True)
            

        else:
            text = "Send trigger build to jenkins fail\n @tritran14 oi vao check ne` !!!"
            self._bot.send_simple_reply(msg, text, threaded=True)
            time.sleep(50)
            console_output = requests.get(output_url, auth=('admin', '{}'.format(JENKINS_API_TOKEN)))
            output_text = console_output.text
            self._bot.send_simple_reply(msg, output_text, threaded=True)


    @botcmd(split_args_with=None)
    def jenkins_createssl(self, msg, args):
        """_syntax: /jenkins createssl <root_ip> <domain_name>"""
        if len(args) < 2 or len(args) > 2:
            text = "`invalid syntax, _syntax: /jenkins createssl <root_ip> <domain_name>`"
            self._bot.send_simple_reply(msg, text, threaded=True)
            return

        root_ip = args[0]
        domain_name = args[1]

        URL = "http://jenkins.sweb.vn/job/sweb/job/Create_SSL/"

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = 'json={"parameter": [{"name":"HOSTS", "value":"%s"}, {"name":"Domain", "value":"%s"}]}' % (root_ip, domain_name)

        response = requests.post(URL+"/build", headers=headers, data=data, auth=('admin', '{}'.format(JENKINS_API_TOKEN)))

        output_url = URL + "/lastBuild/consoleText"

        if response.status_code == 201:
            text = "Send trigger build to jenkins success\nGenarating output - please wait ..."
            self._bot.send_simple_reply(msg, text, threaded=True)
            time.sleep(50)
            console_output = requests.get(output_url, auth=('admin', '{}'.format(JENKINS_API_TOKEN)))
            output_text = console_output.text
            if re.search("SUCCESS", output_text):
                self._bot.send_simple_reply(msg, output_text, threaded=True)
            else:
                text = "Build fail roi @tritran14 oi!!!"
                self._bot.send_simple_reply(msg, text, threaded=True)
            

        else:
            text = "Send trigger build to jenkins fail\n @tritran14 oi vao check ne` {}!!!".format(response.status_code)
            self._bot.send_simple_reply(msg, text, threaded=True)

    @botcmd(split_args_with=None)
    def jenkins_createvhost(self, msg, args):
        """_syntax: /jenkins createvhost <root_ip> <domain_name>"""
        if len(args) < 2 or len(args) > 2:
            text = "`invalid syntax, _syntax: /jenkins createvhost <root_ip> <domain_name>`"
            self._bot.send_simple_reply(msg, text, threaded=True)
            return

        root_ip = args[0]
        domain_name = args[1]

        URL = "http://jenkins.sweb.vn/job/sweb/job/Create_vhost/"

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = 'json={"parameter": [{"name":"HOSTS", "value":"%s"}, {"name":"Domain", "value":"%s"}]}' % (root_ip, domain_name)

        response = requests.post(URL+"/build", headers=headers, data=data, auth=('admin', '{}'.format(JENKINS_API_TOKEN)))

        output_url = URL + "/lastBuild/consoleText"

        if response.status_code == 201:
            text = "Send trigger build to jenkins success\nGenarating output - please wait ..."
            self._bot.send_simple_reply(msg, text, threaded=True)
            time.sleep(60)
            console_output = requests.get(output_url, auth=('admin', '{}'.format(JENKINS_API_TOKEN)))
            output_text = console_output.text
            if re.search("SUCCESS", output_text):
                self._bot.send_simple_reply(msg, output_text, threaded=True)
            else:
                text = "Build fail roi @tritran14 oi!!!"
                self._bot.send_simple_reply(msg, text, threaded=True)
            

        else:
            text = "Send trigger build to jenkins fail\n @tritran14 oi vao check ne` {}!!!".format(response.status_code)
            self._bot.send_simple_reply(msg, text, threaded=True)

    @botcmd(split_args_with=None)
    def jenkins_backupweb(self, msg, args):
        """_syntax: /jenkins backupweb <root_ip> <domain_name>"""
        if len(args) < 2 or len(args) > 2:
            text = "`invalid syntax, _syntax: /jenkins backupweb <root_ip> <domain_name>`"
            self._bot.send_simple_reply(msg, text, threaded=True)
            return

        root_ip = args[0]
        domain_name = args[1]

        URL = "http://jenkins.sweb.vn/job/sweb/job/Create_vhost/"

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = 'json={"parameter": [{"name":"HOSTS", "value":"%s"}, {"name":"Domain", "value":"%s"}]}' % (root_ip, domain_name)

        response = requests.post(URL+"/build", headers=headers, data=data, auth=('admin', '{}'.format(JENKINS_API_TOKEN)))

        output_url = URL + "/lastBuild/consoleText"

        if response.status_code == 201:
            text = "Send trigger build to jenkins success\nGenarating output - please wait ..."
            self._bot.send_simple_reply(msg, text, threaded=True)
            time.sleep(60)
            console_output = requests.get(output_url, auth=('admin', '{}'.format(JENKINS_API_TOKEN)))
            output_text = console_output.text
            if re.search("SUCCESS", output_text):
                self._bot.send_simple_reply(msg, output_text, threaded=True)
            else:
                text = "Build fail roi @tritran14 oi!!!"
                self._bot.send_simple_reply(msg, text, threaded=True)
        else:
            text = "Send trigger build to jenkins fail\n @tritran14 oi vao check ne` {}!!!".format(response.status_code)
            self._bot.send_simple_reply(msg, text, threaded=True)



    @botcmd(split_args_with=None)
    def jenkins_banip(self, msg, args):
        """_syntax: /jenkins banip <vps_ip> <ip_want_to_ban>"""
        if len(args) != 1:
            text = "`invalid syntax, _syntax: /jenkins banip <vps_ip> <ip_want_to_ban>`"
            self._bot.send_simple_reply(msg, text, threaded=True)
            return

        vps_ip = args[0]
        ban_ip = args[1]

        URL = "http://jenkins.sweb.vn/job/sweb/job/BanIP/"

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = 'json={"parameter": [{"name":"VPS_IP", "value":"%s"}, {"name":"BAN_IP", "value":"%s"}]}' % (vps_ip, ban_ip)

        response = requests.post(URL+"/build", headers=headers, data=data, auth=('admin', '{}'.format(JENKINS_API_TOKEN)))

        output_url = URL + "/lastBuild/consoleText"

        if response.status_code == 201:
            text = "Send trigger build to jenkins success\nGenarating output - please wait ..."
            self._bot.send_simple_reply(msg, text, threaded=True)
            time.sleep(20)
            console_output = requests.get(output_url, auth=('admin', '{}'.format(JENKINS_API_TOKEN)))
            output_text = console_output.text
            if re.search("SUCCESS", output_text):
                self._bot.send_simple_reply(msg, output_text, threaded=True)
            else:
                text = "Build fail roi @tritran14 oi!!!"
                self._bot.send_simple_reply(msg, text, threaded=True)
        else:
            text = "Send trigger build to jenkins fail\n @tritran14 oi vao check ne` {}!!!".format(response.status_code)
            self._bot.send_simple_reply(msg, text, threaded=True)

    @botcmd(split_args_with=None)
    def jenkins_unbanip(self, msg, args):
        """_syntax: /jenkins unbanip <vps_ip> <ip_want_to_unban>"""
        if len(args) != 1:
            text = "`invalid syntax, _syntax: /jenkins unbanip <vps_ip> <ip_want_to_unban>`"
            self._bot.send_simple_reply(msg, text, threaded=True)
            return

        vps_ip = args[0]
        unban_ip = args[1]

        URL = "http://jenkins.sweb.vn/job/sweb/job/UnBanIP/"

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = 'json={"parameter": [{"name":"VPS_IP", "value":"%s"}, {"name":"UNBAN_IP", "value":"%s"}]}' % (vps_ip, unban_ip)

        response = requests.post(URL+"/build", headers=headers, data=data, auth=('admin', '{}'.format(JENKINS_API_TOKEN)))

        output_url = URL + "/lastBuild/consoleText"

        if response.status_code == 201:
            text = "Send trigger build to jenkins success\nGenarating output - please wait ..."
            self._bot.send_simple_reply(msg, text, threaded=True)
            time.sleep(20)
            console_output = requests.get(output_url, auth=('admin', '{}'.format(JENKINS_API_TOKEN)))
            output_text = console_output.text
            if re.search("SUCCESS", output_text):
                self._bot.send_simple_reply(msg, output_text, threaded=True)
            else:
                text = "Build fail roi @tritran14 oi!!!"
                self._bot.send_simple_reply(msg, text, threaded=True)
        else:
            text = "Send trigger build to jenkins fail\n @tritran14 oi vao check ne` {}!!!".format(response.status_code)
            self._bot.send_simple_reply(msg, text, threaded=True)