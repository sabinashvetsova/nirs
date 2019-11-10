import random

from utils import Config


if __name__ == '__main__':
    peggy_config = Config('peggy_config.json')
    x = peggy_config.get_value('x')

    common_config = Config('common_config.json')
    g = common_config.get_value('g')
    p = common_config.get_value('p')

    y = pow(g, x, p)
    victor_config = Config('victor_config.json')
    victor_config.update_value('y', y)

    r = random.randint(1, 10040134676)
    C = pow(g, r, p)
    victor_config.update_value('C', C)

    victor_config.update_value('r', r)

    request2 = (x + r) % (p - 1)
    victor_config.update_value('request2', request2)
