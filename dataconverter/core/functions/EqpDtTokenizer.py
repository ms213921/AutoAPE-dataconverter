# -*- coding: utf-8 -*-
# Author : Manki Baek
# e-mail : bmg8551@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team

from __future__ import annotations

from dataconverter.core.ConvertAbstract import ConvertAbstract


class EqpDtTokenizer(ConvertAbstract):
    """
    장비 발생 시각에서 시간과 분을 추출한다.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_feat = 2

    # 토크나이징 하는곳
    def apply(self, data: str) -> list[float]:
        try:
            return [float(data[8:10]), float(data[10:12])]
        except Exception as e:
            # self.LOGGER.error(e)
            return [99.0, 99.0]


if __name__ == "__main__":
    payload = "201812062106001"
    tokenizer = EqpDtTokenizer(stat_dict=None, arg_list=None)
    print(tokenizer.apply(payload))
