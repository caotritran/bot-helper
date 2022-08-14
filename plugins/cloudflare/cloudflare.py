from errbot import BotPlugin, botcmd
from sys import exit
import requests, json, urllib3, os
from tabulate import tabulate

from dotenv import load_dotenv
load_dotenv('.env')

X_Auth_Key = os.environ['X_Auth_Key']
ACCOUNT_ID = os.environ['ACCOUNT_ID']

def get_zoneid(domain):
    headers = {
    'X-Auth-Email': 'caotritran.14@gmail.com',
    'X-Auth-Key': '{}'.format(X_Auth_Key),
    'Content-Type': 'application/json',
    }

    params = {
        'name': '{}'.format(domain),
        'status': 'active',
        'account.id': '{}'.format(ACCOUNT_ID),
        'page': '1',
        'per_page': '20',
        'order': 'status',
        'direction': 'desc',
        'match': 'all',
    }

    response = requests.get('https://api.cloudflare.com/client/v4/zones', params=params, headers=headers)
    data = json.loads(response.text)
    zoneid = data['result'][0].get('id')
    return zoneid

def get_dns_recordid(domain):
    zoneid = get_zoneid(domain)

    headers = {
        'X-Auth-Email': 'caotritran.14@gmail.com',
        'X-Auth-Key': '{}'.format(X_Auth_Key),
        'Content-Type': 'application/json',
    }

    params = {
        'type': 'A',
        'name': '{}'.format(domain),
        'page': '1',
        'per_page': '100',
        'order': 'type',
        'direction': 'desc',
        'match': 'all',
    }

    response = requests.get('https://api.cloudflare.com/client/v4/zones/{}/dns_records'.format(zoneid), params=params, headers=headers)
    data = json.loads(response.text)
    dns_recordid = data['result'][0].get('id')
    return dns_recordid

def update_dns_recordA(domain, ip):
    zoneid = get_zoneid(domain)
    dns_recordid = get_dns_recordid(domain)
    headers = {
        'X-Auth-Email': 'caotritran.14@gmail.com',
        'X-Auth-Key': '{}'.format(X_Auth_Key),
    
    }

    json_data = {
        'type': 'A',
        'name': '{}'.format(domain),
        'content': '{}'.format(ip),
        'ttl': 1,
        'proxied': False,
}

    response = requests.put('https://api.cloudflare.com/client/v4/zones/{0}/dns_records/{1}'.format(zoneid,dns_recordid), headers=headers, json=json_data)
    return response.status_code

def update_dns_recordCNAME(domain, ip):
    zoneid = get_zoneid(domain)
    dns_recordid = get_dns_recordid(domain)
    headers = {
        'X-Auth-Email': 'caotritran.14@gmail.com',
        'X-Auth-Key': '{}'.format(X_Auth_Key),
    
    }

    json_data = {
        'type': 'CNAME',
        'name': '{}'.format(ip),
        'content': '{}'.format(domain),
        'ttl': 1,
        'proxied': False,
}

    response = requests.put('https://api.cloudflare.com/client/v4/zones/{0}/dns_records/{1}'.format(zoneid,dns_recordid), headers=headers, json=json_data)
    return response.status_code

def create_subdomain(subname, domain, ip):
    zoneid = get_zoneid(domain)
    headers = {
        'X-Auth-Email': 'caotritran.14@gmail.com',
        'X-Auth-Key': '{}'.format(X_Auth_Key),
    
    }

    json_data = {
        'type': 'A',
        'name': '{}'.format(subname),
        'content': '{}'.format(ip),
        'ttl': 1,
        'proxied': False,
}

    response = requests.post('https://api.cloudflare.com/client/v4/zones/{0}/dns_records'.format(zoneid), headers=headers, json=json_data)
    return response

def update_subdomain(subname, domain, ip):
    zoneid = get_zoneid(domain)
    dns_recordid = get_dns_recordid(domain)
    headers = {
        'X-Auth-Email': 'caotritran.14@gmail.com',
        'X-Auth-Key': '{}'.format(X_Auth_Key),
    
    }

    json_data = {
        'type': 'A',
        'name': '{}'.format(subname),
        'content': '{}'.format(ip),
        'ttl': 1,
        'proxied': False,
}

    response = requests.put('https://api.cloudflare.com/client/v4/zones/{0}/dns_records/{1}'.format(zoneid, dns_recordid), headers=headers, json=json_data)
    return response

def get_dns_record(domain):
    zoneid = get_zoneid(domain)

    headers = {
    'X-Auth-Email': 'caotritran.14@gmail.com',
    'X-Auth-Key': '{}'.format(X_Auth_Key)
    }

    #params = {
    #    'name': '{}'.format(domain),
    #    'page': '1',
    #    'per_page': '900',
    #    'order': 'type',
    #    'direction': 'desc',
    #    'match': 'all',
    #}

    response = requests.get('https://api.cloudflare.com/client/v4/zones/{}/dns_records'.format(zoneid), headers=headers)
    return response


class CLOUDFLARE(BotPlugin):
    """
    Help us to intergrate with CF API, syntax: /cloudflare <cmd>
    """
    
    @botcmd(split_args_with=None)
    def cloudflare_updatedns(self, msg, args):
        """_syntax: /cloudflare updatedns <A|CNAME> <fqdn> <ip|www>"""
        type = args[0]
        domain_name = args[1].lower().strip()
        ip = args[2].strip()

        if len(args) < 2 or len(args) > 3:
            text = "`invalid syntax, _syntax: /cloudflare updatedns <A|CNAME> <fqdn> <ip>`"
            self._bot.send_simple_reply(msg, text, threaded=True)
            return

        if type == "A":
            state = update_dns_recordA(domain_name,ip)
            if state == 200:
                text = "`update record success, status code {}`".format(state)
                self._bot.send_simple_reply(msg, text, threaded=True)
            else:
                text = "`somethings went wrong, status code {}`".format(state)
                self._bot.send_simple_reply(msg, text, threaded=True)
            return

        elif type == "CNAME":
            state = update_dns_recordCNAME(domain_name,ip)
            if state == 200:
                text = "`update record success, status code {}`".format(state)
                self._bot.send_simple_reply(msg, text, threaded=True)
            else:
                text = "`somethings went wrong, status code {}`".format(state)
                self._bot.send_simple_reply(msg, text, threaded=True)
            return
        else:
            text = "`invalid syntax, _syntax: /cloudflare updatedns <A|CNAME> <fqdn> <ip>`"
            self._bot.send_simple_reply(msg, text, threaded=True)
            return

    @botcmd(split_args_with=None)
    def cloudflare_dnswatch(self, msg, args):
        """_syntax: /cloudflare dnswatch <fqdn>"""
        domain_name = args[0].lower().strip()

        if len(args) < 1 or len(args) > 2:
            text = "`invalid syntax, _syntax: .cloudflare dnswatch <fqdn>"
            self._bot.send_simple_reply(msg, text, threaded=True)
            return

        table = []
        headers = ["Type", "Content", "Name"]
        text = ""
        
        data = get_dns_record(domain_name)
        if data.status_code == 200:
            data = json.loads(data.text)
            leng = len(data['result'])

            for i in range(0, leng):
                #print(data['result'][i].get('content'))
                table.append([
                    data['result'][i].get('type'),
                    data['result'][i].get('content'),
                    data['result'][i].get('name')
                ])

            text = tabulate(table, headers=headers, tablefmt="simple")
            self._bot.send_simple_reply(msg, text, threaded=True)
            return
        else:
            text = "`somethings went wrong, status code {}`".format(data.status_code)
            self._bot.send_simple_reply(msg, text, threaded=True)
            return

    @botcmd(split_args_with=None)
    def cloudflare_create_subdomain(self, msg, args):
        """_syntax: /cloudflare create subdomain <sub_name> <fqdn> <ip>"""
        sub_name = args[0].lower().strip()
        domain_name = args[1].lower().strip()
        ip = args[2].strip()

        table = []
        headers = ["Type", "Name", "Content"]
        text = ""

        if len(args) < 3 or len(args) > 4:
            text = "`invalid syntax, _syntax: /cloudflare create subdomain <sub_name> <fqdn> <ip>`"
            self._bot.send_simple_reply(msg, text, threaded=True)
            return
        state = create_subdomain(sub_name, domain_name, ip)
        if state.status_code == 200:
            text = "`create subdomain success, status code {}`".format(state.status_code)
            self._bot.send_simple_reply(msg, text, threaded=True)
            data = json.loads(state.text)
            table.append([
                data['result'].get('type'),
                data['result'].get('name'),
                data['result'].get('content')
            ])
            text = tabulate(table, headers=headers, tablefmt="pretty")
            self._bot.send_simple_reply(msg, text, threaded=True)
        else:
            text = "`something went wrong\n@tritran14 oi, check nha`"
            self._bot.send_simple_reply(msg, text, threaded=True)
            

    @botcmd(split_args_with=None)
    def cloudflare_update_subdomain(self, msg, args):
        """_syntax: /cloudflare update subdomain <sub_name> <fqdn> <ip>"""
        sub_name = args[0].lower().strip()
        domain_name = args[1].lower().strip()
        ip = args[2].strip()

        table = []
        headers = ["Type", "Name", "Content"]
        text = ""

        if len(args) < 3 or len(args) > 4:
            text = "`invalid syntax, _syntax: /cloudflare update subdomain <sub_name> <fqdn> <ip>`"
            self._bot.send_simple_reply(msg, text, threaded=True)
            return
        state = update_subdomain(sub_name, domain_name, ip)
        if state.status_code == 200:
            text = "`update subdomain success, status code {}`".format(state.status_code)
            self._bot.send_simple_reply(msg, text, threaded=True)
            data = json.loads(state.text)
            table.append([
                data['result'].get('type'),
                data['result'].get('name'),
                data['result'].get('content')
            ])
            text = tabulate(table, headers=headers, tablefmt="pretty")
            self._bot.send_simple_reply(msg, text, threaded=True)
        else:
            text = "`something went wrong\n@tritran14 oi, check nha`"
            self._bot.send_simple_reply(msg, text, threaded=True)