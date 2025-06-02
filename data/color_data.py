min_area = 100000

lower_box = (10, 50, 0)
upper_box = (30, 150, 255)

lower_white = (40, 0, 150)
upper_white = (145, 50, 255)

#TEST
#HSV limits for mobile phone pictures
hsv_limits = [
    ["None", (0,0,0),(1,1,1)],
    ["Cork", (0, 70, 65), (15, 105, 155)],
    ["Whitecap Gray", (0, 35, 120), (30, 65, 185)],
    ["Gray Clouds", (0, 0, 85), (179, 30, 175)],
    ["Almost Aqua", (90, 40, 155), (100, 50, 200)],
    ["Raw Umber", (0, 25, 85), (15, 60, 120)],
    ["Hedge Green", (50, 20, 90), (100, 50, 130)],
]

#HSV limits for live recording in laboratory
hsv_limits_lab= [
    ["None", (0, 0, 0), (1, 1, 1)],
    ["Cork", (0, 75, 0), (15, 120, 255)],
    ["Whitecap Gray", (10, 35, 110), (30, 65, 185)],
    ["Gray Clouds", (135, 0, 80), (170, 40, 125)],
    ["Almost Aqua", (55, 0, 160), (100, 30, 190)],
    ["Raw Umber", (0, 20, 95), (15, 55, 120)],
    ["Hedge Green", (55, 15, 95), (105, 50, 135)],
]

hsv_limits_doma= [
    ["None", (0, 0, 0), (1, 1, 1)],
    ["Cork", (0, 55, 100), (20, 105, 170)],
    ["Whitecap Gray", (10, 35, 115), (30, 60, 200)],
    ["Gray Clouds", (140, 0, 80), (179, 35, 155)],
    # ["Almost Aqua", (40, 0, 130), (100, 30, 200)],
    ["Raw Umber", (0, 15, 75), (15, 60, 115)],
    ["Hedge Green", (50, 15, 80), (105, 55, 140)],
]