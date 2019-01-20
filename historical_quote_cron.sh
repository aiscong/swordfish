
EMAIL="aiscong@gmail.com,jiwen.you.94@gmail.com"
HOME_PATH='/Users/j0y01rf/PycharmProjects/swordfish'


if python ${HOME_PATH}/historical_quote_cron.py; then
    mail -s "SUCCESS: Pull historical quote" ${EMAIL} < /dev/null
else
    mail -s "FAILED: Pull historical quote" ${P13N_EMAIL} < /dev/null
fi
