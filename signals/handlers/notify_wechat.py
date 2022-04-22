
def send_to_wechat(vul):
    """
    todo 发送漏洞通知到企业微信
    :return:
    """
    return

    wechat = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxx"
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }

    message = {
        "msgtype": "text",
        "text": {
            "content": "IAST漏洞扫描告警通知，请相关同事及时处理！！！\n漏洞类型：{}\n危害等级：{}\n漏洞URL：{}\n业务线名称：{}\n探针agent：{}".format(vul.strategy.vul_type, vul.level.name_value,
                                                                                                            vul.url, vul.agent.project_name, vul.agent.token),
            "mentioned_list": ["@all"],
            "mentioned_mobile_list": ["@all"]
        },
    }

    resp = requests.post(url=wechat, headers=header, data=json.dumps(message))
    if resp.status_code == 200:
        pass
