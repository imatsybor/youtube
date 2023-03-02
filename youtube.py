import pyautogui
import webbrowser
import time
import random


lst = ['https://youtu.be/VaRrVMtDvr8', 'https://youtu.be/NxdJAT1TZBY',
       'https://youtu.be/amAJTqH_Kcw', 'https://youtu.be/zEtfDxRuw00',
       'https://youtu.be/uj74-JJyMvI', 'https://youtu.be/SsldnbqaskA',
       'https://youtu.be/VtOmbv93kdE', 'https://youtu.be/dGzpf8svGb0',
       'https://youtu.be/0zUBD6I6aIE', 'https://youtu.be/jWC-_OsXp-A',
       'https://youtu.be/5_PW6nJ3K88', 'https://youtu.be/WmI437oqZWM',
       'https://youtu.be/l4MSUyEgtOw', 'https://youtu.be/R891n9fDrkc',
       'https://youtu.be/2BT6ratLGiU', 'https://youtu.be/gNiurhl25cM',
       'https://youtu.be/ziMFFtE5UsU', 'https://youtu.be/dqv3nWnrSHo',
       'https://youtu.be/du6OK11VqrM', 'https://youtu.be/0n_NfHICJ2Y',
       'https://youtu.be/87AcIf1gxzk', 'https://youtu.be/UnZILAAaarM',
       'https://youtu.be/jInq9GJrcWQ', 'https://youtu.be/LI02kDGJfwc',
       'https://youtu.be/YNHCx0vCMgk', 'https://youtu.be/2GhUXh0HVco',
       'https://youtu.be/4piILHMMbDo', 'https://youtu.be/VQruupTNqmY',
       'https://youtu.be/C9YOpnS6jS0', 'https://youtu.be/1nJgQuHbqWE',
       'https://youtu.be/8W7eZsZg8KU', 'https://youtu.be/ledchHNXzfo',
       'https://youtu.be/xl28XD0Gm-0', 'https://youtu.be/dw3KXhb3DU4',
       'https://youtu.be/Q9dtF8tUfVM', 'https://youtu.be/0suitxrg0fw',
       'https://youtu.be/G5oPmAz4emI', 'https://youtu.be/MlIWVuEqa1s',
       'https://youtu.be/zJzGJUEvjKw', 'https://youtu.be/Y54qBg-gUwc',
       'https://youtu.be/CUsMJWC2KaM', 'https://youtu.be/3pamQhxG73c',
       'https://youtu.be/bixwXTj-3FU', 'https://youtu.be/Rjo059IYxGs',
       'https://youtu.be/g0a7VkokcTc', 'https://youtu.be/cAzhxEi19M0',
       'https://youtu.be/lVJWXkGedD8', 'https://youtu.be/-3Jjmr33v7U',
       'https://youtu.be/yBv007E18Zg', 'https://youtu.be/BHV2qzn74mY',
       'https://youtu.be/dfcebIIuEwc', 'https://youtu.be/Bz0bjIbszlA',
       'https://youtu.be/hjKzCATv1UQ', 'https://youtu.be/y4tvJzkhyrc',
       'https://youtu.be/njIUQ6_N-rI', 'https://youtu.be/t7_YduGZrcM',
       'https://youtu.be/TnfoAuNFDCQ', 'https://youtu.be/DuZinxxwG04',
       'https://youtu.be/e7gOBrqNDxI', 'https://youtu.be/Asq-7ZN-8fM',
       'https://youtu.be/InaAEJvcLCw', 'https://youtu.be/0390dWJUZsg',
       'https://youtu.be/3Nyv7yQFpmw', 'https://youtu.be/F3AE5gNOx_g',
       'https://youtu.be/iZnZyxr4L5Y', 'https://youtu.be/I-Rkx1n1xrA',
       'https://youtu.be/kqcorDJe2SU', 'https://youtu.be/8p0x3ckrY6k',
       'https://youtu.be/xIsLLFJkzMc', 'https://youtu.be/GX5dxklNJsM',
       'https://youtu.be/8dWKZCy_8l4', 'https://youtu.be/b_9ODqIwHoU',
       'https://youtu.be/R1RCyTxlAo4', 'https://youtu.be/OVYNHfIW06Q',
       'https://youtu.be/1CaKg4gc5HI', 'https://youtu.be/yAEVYigYyA0',
       'https://youtu.be/IKgecHtBKBk', 'https://youtu.be/ZDVOxaLZs0Y',
       'https://youtu.be/G3gqmEB1Z2c', 'https://youtu.be/Igw3iIG_Kvg',
       'https://youtu.be/KMFCiPdOjgc', 'https://youtu.be/jokPOw4gGB8',
       'https://youtu.be/BLH3lbrTA4s', 'https://youtu.be/3U064pz-DEY',
       'https://youtu.be/FCqSTWjsqlQ', 'https://youtu.be/vRIvyveFulQ',
       'https://youtu.be/L8b23vihwL8', 'https://youtu.be/2wTkqi2LBcU',
       'https://youtu.be/ksTUsXfOoYk', 'https://youtu.be/JF7YSyPt790',
       'https://youtu.be/ucI4ghcyBbw', 'https://youtu.be/l7Lr5xJ9Z_E',
       'https://youtu.be/2dY3rjIAqoI', 'https://youtu.be/ow-Xp8K-4aA',
       'https://youtu.be/itnjGSqoPx8', 'https://youtu.be/0fyJzbgGiCM',
       'https://youtu.be/2ixC3GiRbEo', 'https://youtu.be/WO9dMbTILXk',
       'https://youtu.be/P8UAnNw269Y', 'https://youtu.be/I0pz_QOHNbg',
       'https://youtu.be/Z2-U3rDsq-I', 'https://youtu.be/OxmvnQR_DKA',
       'https://youtu.be/OBIj2KfxloI', 'https://youtu.be/tzP_lkSlFPg',
       'https://youtu.be/2Euc5uZPSSI', 'https://youtu.be/6S1AWVCm8e4',
       'https://youtu.be/UbuSNIoyNkQ', 'https://youtu.be/QkfCIalN3og']

# for i in range кол-во видео
while len(lst) > 0:
    s = lst.pop(random.randint(0, len(lst)-1))
    webbrowser.open(s)
    print(len(lst))
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'shift', 'tab')
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(random.randint(190, 305))
