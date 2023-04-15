from ast import arg
from pydoc import text
import time
from errbot import BotPlugin, botcmd
from sys import exit
import requests, json, urllib3, os, re
import paramiko, socket
from tabulate import tabulate
import subprocess

from dotenv import load_dotenv
load_dotenv('.env')


class RCLONE(BotPlugin):
    """
    Help us to intergrate with rclone, syntax: /rclone <cmd>
    """
    
    @botcmd(split_args_with=None)
    def rclone_find_backup(self, msg, args):
        """_syntax: /rclone find backup <domain_name>"""
        if len(args) < 1 or len(args) > 1:
            text = "`invalid syntax, _syntax: /rclone find backup <domain_name>`"
            self._bot.send_simple_reply(msg, text, threaded=True)
            return
        domain_name = args[0]
        plugin_path = os.path.dirname(os.path.realpath(__file__))
        other_file_path = os.path.join(plugin_path, "rclone_check_backup.sh {0}".format(domain_name))
        output = subprocess.check_output(["/usr/bin/bash", other_file_path]).decode("utf-8")

        text = "Waiting search all onedrive..."
        self._bot.send_simple_reply(msg, text, threaded=True)
        self._bot.send_simple_reply(msg, output, threaded=True)

    