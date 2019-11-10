from utils import Config


if __name__ == '__main__':
    common_config = Config('common_config.json')
    g = common_config.get_value('g')
    p = common_config.get_value('p')

    victor_config = Config('victor_config.json')
    r = victor_config.get_value('r')
    C = victor_config.get_value('C')

    print(pow(g, r, p) == C)

    request2 = victor_config.get_value('request2')
    y = victor_config.get_value('y')

    print(pow(g, request2, p) == C * y % p)