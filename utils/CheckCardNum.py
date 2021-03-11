# 验证邮政卡卡号有效性方法文件


def check_card_num(card_num):
    # 邮政卡卡号开头们
    card_num_heads = (
        '622150', '622151', '622181', '622188', '955100', '621095', '620062', '621285', '621798', '621799', '621797',
        '622199', '621096', '62215049', '62215050', '62215051', '62218849', '62218850', '62218851', '621622', '623219',
        '621674', '623218', '621599', '623698', '623699', '623686', '622182', '625586', '621098', '620529', '622180',
        '622187', '622189', '622812', '622810', '622811', '628310', '625919', '625368', '625367', '518905', '622835',
        '625603', '621582', '623676', '623677', '625605'
    )

    # 没有按规定开头，返回False
    if not card_num.startswith(card_num_heads):
        return False

    # 长度不为19，返回False
    if len(card_num) != 19:
        return False

    # 没问题了，返回True
    return True