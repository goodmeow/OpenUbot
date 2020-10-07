# We're using Focal Fossa
FROM aarunalr/openubot:userbot

#
# Clone repo and prepare working directory
#
RUN git clone -b sql-extended https://github.com/goodmeow/OpenUbot /root/userbot
RUN mkdir /root/userbot/bin/
WORKDIR /root/userbot/

#
# start userbot
#
CMD ["python3","-m","userbot"]
