
EMAIL="aiscong@gmail.com,jiwen.you.94@gmail.com"
HOME_PATH="$PWD"
TODAY=`date +"%Y%m%d"`
TIMESTAMP_FOLDER=`date +"%Y%m%d%H%M%S"`

cd $HOME_PATH

if [[ "$TODAY" =~ ^(20190101|20190121|20190218|20190419|20190524|20190704|20190902|20191128|20191225)$ ]]; then
    mail -s 'Stock market closed today' ${EMAIL} < /dev/null
else
    if python3 ${HOME_PATH}/historical_quote_cron.py; then
        echo 'Pull historical quote finished successfully at '$TIMESTAMP_FOLDER''
        mail -s "SUCCESS: Pull historical quote" ${EMAIL} < /dev/null
    else
        echo 'Pull historical quote exited with error at '$TIMESTAMP_FOLDER''
        mail -s "FAILED: Pull historical quote" ${EMAIL} < /dev/null
    fi
fi



