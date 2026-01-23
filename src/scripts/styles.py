from enum import Enum


class Styles(Enum):
    button_style_1 = (
        'QPushButton {\nbackground-color: #07942d;\nwidth: 55px;\nheight: 55px;\n'
        'font-size: 22px;\nfont-weight: bold;\ncolor: _____;\nborder: none;\n'
        'border-radius: 5px;\n}'
        '\nQPushButton:hover {\nbackground-color: #068027;\n}'
        '\nQPushButton:disabled {\nbackground-color: #e2dede;\n}'
    )
    button_style_2 = (
        'QPushButton {\nbackground-color: #f01111;\nwidth: 55px;\nheight: 55px;\n'
        'font-size: 18px;\nfont-weight: bold;\ncolor: #000000;\nborder: none;\n'
        'border-radius: 5px;\n}'
        '\nQPushButton:disabled {\nbackground-color: #f01111;\n}'
    )
    main_window_style = 'background-color: #3d3b39;'
    value_styles = {
        '1': button_style_1.replace('_____', '#07c3f1'),
        '2': button_style_1.replace('_____', '#12e8ab'),
        '3': button_style_1.replace('_____', '#f6263f'),
        '4': button_style_1.replace('_____', '#ed26f6'),
        '5': button_style_1.replace('_____', '#ece72f'),
        '6': button_style_1.replace('_____', '#f48b23'),
        '7': button_style_1.replace('_____', '#f4238c'),
        '8': button_style_1.replace('_____', '#be23f4'),
    }