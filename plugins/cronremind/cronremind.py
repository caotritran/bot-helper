from errbot import BotPlugin
from errcron import CrontabMixin
import os

TELE_GROUP_ID = os.environ['TELE_GROUP_ID']
class ErrcronDemo(CrontabMixin, BotPlugin):
    """
    Remind task daily
    """
    CRONTAB = [
        '0 8 * * * .remind_daily @pikabot',
        '10 8 * * 6 .remind_weekly @pikabot',
    ]

    def activate(self):
        super().activate()

    def remind_daily(self, polled_time, identity):
        identity = TELE_GROUP_ID
        user = self.build_identifier(identity)
        #return self.send(user, 'Currently {}'.format(polled_time.strftime('%H:%M')))
        text = "***Remind***\n" + "1. What are the issues today? - Check tele [Alert] 🤖 Sweb\n" +  "2. What are the complaints or renew payments today? - Check the email\n" + "cc @tritran14 @Cuong"
        return self.send(user, text)

    def remind_weekly(self, polled_time, identity):
        identity = TELE_GROUP_ID
        user = self.build_identifier(identity)
        #return self.send(user, 'Currently {}'.format(polled_time.strftime('%H:%M')))
        text = "***Remind***\n" + "Please check and clear history trash Onedrive !!!\n" + "cc @tritran14"
        return self.send(user, text)