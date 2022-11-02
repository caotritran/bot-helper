from errbot import BotPlugin
from errcron import CrontabMixin
import os

TELE_GROUP_ID = os.environ['TELE_GROUP_ID']
class ErrcronDemo(CrontabMixin, BotPlugin):
    """
    Remind task daily
    """
    CRONTAB = [
        '* * * * * .remind_daily @pikabot',
    ]

    def activate(self):
        super().activate()

    def remind_daily(self, polled_time, identity):
        #identity = "1019630113"
        identity = TELE_GROUP_ID
        user = self.build_identifier(identity)
        return self.send(user, 'Currently {}'.format(polled_time.strftime('%H:%M')))
        #text = "***Remind***\n" + "1. What are the issues today? - Check tele [Alert] 🤖 Sweb\n" +  "2. What are the complaints or renew payment today? - Check the email\n" + "cc @tritran14"
        #return self.send(user, text)