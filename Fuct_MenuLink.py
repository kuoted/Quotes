# -*- coding: utf-8 -*-

"""
菜单与功能函数字典映射关系
"""


def UI_Menu(UI):
    Menu = [
        {"title": "龙虎榜",
        "Button":UI.QToolButton_mRankList,
        "pages":[{"id": 1, "title": "龙虎榜列表", "FuctLink": UI.QPushButton_cRankListStocks, "Avgs": "1"},
                ]
        },
        # {"title": "次新股",
        #  "Button": UI.QToolButton_mNews,
        #  "pages": [
        #      {"id": 1, "title": "今日开板", "FuctLink": "Cixin", "Avgs": "1"},
        #      {"id": 2, "title": "近7日开板", "FuctLink": "Cixin", "Avgs": "7"},
        #      {"id": 3, "title": "近30日开板", "FuctLink": "Cixin", "Avgs": "30"}
        #  ]
        #  },
        # {"title": "板块追踪",
        #  "Button": UI.QToolButton_mNews,
        #  "pages": [
        #      {"id": 1, "title": "今日开板", "FuctLink": "Cixin", "Avgs": "1"},
        #      {"id": 2, "title": "近7日开板", "FuctLink": "Cixin", "Avgs": "7"},
        #      {"id": 3, "title": "近30日开板", "FuctLink": "Cixin", "Avgs": "30"}
        #  ]
        #  },
        # {"title": "涨停预测",
        #  "Button": UI.QToolButton_mNews,
        #  "pages": [
        #      {"id": 1, "title": "今日开板", "FuctLink": "Cixin", "Avgs": "1"},
        #      {"id": 2, "title": "近7日开板", "FuctLink": "Cixin", "Avgs": "7"},
        #      {"id": 3, "title": "近30日开板", "FuctLink": "Cixin", "Avgs": "30"}
        #  ]
        #  },
        # {"title": "资讯",
        #  "Button": UI.QToolButton_mNews,
        #  "pages": [
        #      {"id": 1, "title": "今日开板", "FuctLink": "Cixin", "Avgs": "1"},
        #      {"id": 2, "title": "近7日开板", "FuctLink": "Cixin", "Avgs": "7"},
        #      {"id": 3, "title": "近30日开板", "FuctLink": "Cixin", "Avgs": "30"}
        #  ]
        #  },
    ]
    return Menu
if __name__ == '__main__':
    pass