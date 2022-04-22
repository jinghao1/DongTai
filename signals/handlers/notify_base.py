from dongtai.models.notify_config import IastNotifyConfig


def create_vul_data_from_model(vul):
    """

    :param vul:
    :return:{
        http_url: 漏洞所在url
        http_uri: 漏洞所在uri
        context_path: HTTP请求上下文
        http_method: HTTP请求方法
        http_scheme: HTTP请求协议
        http_protocol: HTTP请求协议
        req_header: HTTP请求头
        req_data: HTTP请求体
        res_header: HTTP响应头
        res_body: HTTP响应体
        vul_type: 漏洞类型
        vul_level: 漏洞等级
        full_stack: 漏洞对应的调用链数据
        top_stack: 漏洞对应污点调用链的链首
        bottom_stack: 漏洞对应污点调用链的链尾
        taint_value: 污点值
        taint_position: 污点所在位置
        agent_token: Agent的token
        project: 所在的项目
        counts: 漏洞出现次数
        client_ip: 客户端IP
        username: 漏洞所在用户的用户名
    }
    """
    agent = vul.agent
    vul_data = {}
    vul_data['vul_type'] = vul.hook_type.name
    vul_data['vul_level'] = vul.level.name_value
    vul_data['http_url'] = vul.url
    vul_data['http_uri'] = vul.uri
    vul_data['http_method'] = vul.http_method
    vul_data['http_scheme'] = vul.http_scheme
    vul_data['http_protocol'] = vul.http_protocol
    vul_data['req_header'] = vul.req_header
    vul_data['req_data'] = vul.req_data
    vul_data['res_header'] = vul.res_header
    vul_data['res_body'] = vul.res_body
    vul_data['full_stack'] = vul.full_stack
    vul_data['top_stack'] = vul.top_stack
    vul_data['bottom_stack'] = vul.bottom_stack
    vul_data['taint_value'] = vul.taint_value
    vul_data['taint_position'] = vul.taint_position
    vul_data['agent_token'] = agent.token
    vul_data['project'] = agent.project_name
    vul_data['context_path'] = vul.context_path
    vul_data['counts'] = vul.counts
    vul_data['client_ip'] = vul.client_ip
    vul_data['username'] = vul.agent.user.get_username()
    return vul_data


def read_notify_config(user):
    # 从云端读取通知信息
    notify_config_models = IastNotifyConfig.objects.values('notify_type', 'notify_metadata').filter(user=user)
    return (True, notify_config_models) if notify_config_models else (False, None)
