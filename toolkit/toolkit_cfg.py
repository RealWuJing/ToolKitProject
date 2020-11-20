def toolkit_cfg(toolkit_cfg ='ToolKit.cfg'):
    toolkit_cfg_dict = {}
    with open(toolkit_cfg, 'r', encoding='utf8') as f:
        content = f.read()  # .replace('\\', '/')
        content_list = content.strip().split('\n')
    for line in content_list:
        toolkit_cfg_dict[line.split('=')[0].strip().split('\n')[0]] = line.split('=')[-1].strip().split('\n')[0]
    return toolkit_cfg_dict
