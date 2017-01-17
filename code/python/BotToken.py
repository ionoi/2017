# coding:utf-8

import json
import pickle
import time

class BotToken:
    def __init__(self, app_id, app_key):
        """
        Bot 令牌

        尽量不要直接使用这个类，而是用 :meth:`BotToken.from_str` 或
        :meth:`BotToken.form_dict` 或
        :meth:`BotToken.from_file` 方法来构造。

        ..  note::

            本类仅在 :class:`.BotClient` 类内使用，一般用户不需要了解。

        :param str app_id:  leancloud app id
        :param str app_key: leancloud app key
        """
        self._create_at = time.time()
        self._app_id = app_id
        self._app_key = app_key

    @staticmethod
    def from_str(json_str):
        """
        从字符串读取 token。

        :param str|unicode json_str: 一个合法的代表Bot Token 的 JSON 字符串
        :rtype: :class:`BotToken`
        :raise ValueError: 提供的参数不合法时
        """
        try:
            return BotToken.from_dict(json.loads(json_str))
        except Exception:
            raise ValueError(
                '"{json_str}" is NOT a valid json token string.'.format(
                    json_str=json_str
                ))

    @staticmethod
    def from_dict(json_dict):
        """
        从字典读取 token。

        :param dict json_dict: 一个代表Bot Token 的字典
        :rtype: :class:`BotToken`
        :raise ValueError: 提供的参数不合法时
        """
        try:
            return BotToken(**json_dict)
        except TypeError:
            raise ValueError(
                '"{json_dict}" is NOT a valid zhihu token json.'.format(
                    json_dict=json_dict
                ))

    @staticmethod
    def from_file(filename):
        """
        从文件读取 token。

        :param str|unicode filename: 文件名
        :rtype: json
        """
        with open(filename, 'r') as f:
            return json.load(f)

    def save(self, filename):
        """
        将 token 保存成文件。

        :param str|unicode filename: 文件名
        :return: 无返回值
        """
        dct = dict(app_id=self._app_id,
                   app_key=self._app_key)
        with open(filename, 'w') as f:
             json.dump(dct, f, indent=4)

if __name__ == '__main__':
    btoken = BotToken('aaa','bbbb')
    btoken.save('config.json')

    js = BotToken.from_file('config.json')
    print(js)
