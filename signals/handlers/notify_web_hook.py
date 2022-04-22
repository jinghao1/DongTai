import requests,json


def send_to_web_hook(web_hook_url, template, vul_data):
    """
    发送漏洞通知到webhook
    """
    notify_text = template \
        .replace("{{url}}", vul_data['http_url']) \
        .replace("{{uri}}", vul_data['http_uri']) \
        .replace("{{context_path}}", vul_data['context_path']) \
        .replace("{{http_method}}", vul_data['http_method']) \
        .replace("{{http_scheme}}", vul_data['http_scheme']) \
        .replace("{{http_protocol}}", vul_data['http_protocol']) \
        .replace("{{req_header}}", vul_data['req_header']) \
        .replace("{{vul_type}}", vul_data['vul_type']) \
        .replace("{{vul_level}}", vul_data['vul_level']) \
        .replace("{{full_stack}}", vul_data['full_stack']) \
        .replace("{{top_stack}}", vul_data['top_stack']) \
        .replace("{{bottom_stack}}", vul_data['bottom_stack']) \
        .replace('{{taint_value}}', vul_data['taint_value']) \
        .replace('{{taint_position}}', vul_data['taint_position']) \
        .replace('{{agent_token}}', vul_data['agent_token']) \
        .replace('{{project}}', vul_data['project']) \
        .replace('{{counts}}', str(vul_data['counts'])) \
        .replace('{{client_ip}}', vul_data['client_ip']) \
        .replace('{{username}}', vul_data['username'])

    resp = requests.post(url=web_hook_url, json=json.loads(notify_text))
    if resp.status_code == 200:
        pass
