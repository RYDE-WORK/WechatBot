import itchat


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text


def main():
    itchat.auto_login(
        hotReload=True,
        # enableCmdQR=2
    )
    itchat.send(
        msg="Hello World.",
        toUserName='filehelper'
    )


if __name__ == '__main__':
    main()
