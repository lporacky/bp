comb1 = ["Hedge Green","Cork","Raw Umber","Whitecap Gray","Gray Clouds","Cork"]
comb2 = ["Hedge Green","Cork","Raw Umber","Whitecap Gray","Gray Clouds","Whitecap Gray"]

min_area = 100000

lower_box = (10, 50, 0)
upper_box = (30, 150, 255)

lower_white = (50, 0, 160)
upper_white = (145, 40, 255)

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

hsv_limits_lab= [
    ["None", (0, 0, 0), (1, 1, 1)],
    ["Cork", (0, 55, 100), (20, 105, 170)],
    ["Whitecap Gray", (10, 35, 115), (30, 60, 200)],
    ["Gray Clouds", (140, 0, 80), (179, 35, 155)],
    # ["Almost Aqua", (40, 0, 130), (100, 30, 200)],
    ["Raw Umber", (0, 15, 75), (15, 60, 150)],
    ["Hedge Green", (50, 15, 80), (105, 55, 140)],
]