# send-command-from-aws-to-iot


`git clone https://github.com/gauravshremayee/aws-iot-device-sdk-js.git`

`cd aws-iot-device-sdk-js/examples`

`node device-example.js --client-id=1234 --protocol=mqtts --private-key=9ab1e9e3bf.private.key --client-certificate=9ab1e9e3bf.cert.pem --ca-certificate=root-CA.crt --reconnect-period-ms=3000ms --thing-name=AlishaIoT --delay-ms=250 --host-name=XXXXXXXX-ats.iot.ap-south-1.amazonaws.com`

`crontab -l`

* * * * * /home/pi/runLatestAWSCommand.py

copy your command to /usr/bin

`cp sendHomeStatus.sh /usr/bin/sendHomeStatus`

`chmod a+x /usr/bin/sendHomeStatus`

subscribe to topic_1 in AWS Console and send command in below format

{
  "message": "Command:sendHomeStatus"
}

Your Command will be executed
