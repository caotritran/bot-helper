# bot-helper

- compatible with `python 3.8`

```
python -m venv venv
source venv/bin/active
pip install -r requirements.txt
errbot --init
```
- Next, copy file config `config.py.telegram` if you want to using bot intergrate with telegram.
using `config.py.slack` if you want to using bot intergrate with slack.

`cp config.py.[telegram|slack] config.py`

- Decrypt file with ansible-vault (Optional, my personal purpose for more security)

`ansible-vault --vault-password-file=~/.secret config.py`

- Create file `.env` at current folder and add 2 varibales as below:
```
X_Auth_Key=<API_KEY_CLOUDFLARE>
ACCOUNT_ID=<ACCOUNT_ID_CLOUDFLARE>
JENKINS_API_TOKEN=<CREATE_ON_JENKINS>
```

- Run error bot as daemon, and happy coding with modify, custom your code in folder `plugin`.

- Create user `errbot` to run daemon
`useradd --no-create-home --no-user-group -g nobody -s /bin/false errbot`

ref: https://errbot.readthedocs.io/en/latest/
