import json
from dongtai.models.notify_config import IastNotifyConfig
from signals.handlers.notify_web_hook import send_to_web_hook
from signals.handlers.notify_base import read_notify_config,create_vul_data_from_model


# 根据用户配置，发送响应的服务通知
def send_vul_notify(vul):
    """
    :param vul_data:
    :return:
    """
    support_notify, notify_configs = read_notify_config(vul.agent.user)
    if support_notify:
        vul_data = create_vul_data_from_model(vul=vul)
        for notify_config in notify_configs:
            notify_type = notify_config.get('notify_type')
            if notify_type == IastNotifyConfig.WEB_HOOK:
                metadata = json.loads(notify_config.get('notify_metadata'))
                send_to_web_hook(vul_data=vul_data, web_hook_url=metadata['url'], template=metadata['template'])
            elif notify_type == IastNotifyConfig.JIRA:
                # todo 补充JIRA的通知
                pass
            elif notify_type == IastNotifyConfig.DING_DING:
                # todo 补充钉钉通知
                pass
            elif notify_type == IastNotifyConfig.EMAIL:
                # todo 补充邮件通知
                pass
            else:
                pass





