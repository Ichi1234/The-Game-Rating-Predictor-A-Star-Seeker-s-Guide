import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import Image


def k_destroyer(val):
    """Remove K in csv and *1000 to the value which have K"""
    val = val.replace('K', '')
    val = float(val)
    return val * 1000

df = pd.read_csv('backloggd_games.csv')
df.dropna(subset=df.columns.tolist(), how='any', inplace=True)
df['Plays'] = df['Plays'].apply(k_destroyer)
df['Plays'] = df['Plays'] = pd.to_numeric(df['Plays'], errors='coerce')


what = "Platforms"
all_value = ['Windows PC', 'PlayStation 4', 'Xbox One', 'PlayStation 5', 'Xbox Series', 'Wii U', 'Nintendo Switch', 'Mac', 'Linux', 'PlayStation Vita', 'Android', 'iOS', 'Xbox 360', 'PlayStation 3', 'Google Stadia', 'Wii', 'Nintendo 64', 'PlayStation', 'PlayStation Portable', 'Playstation VR2', 'PlayStation 2', 'Nintendo GameCube', 'Super Famicom', 'SNES', 'Satellaview', 'New Nintendo 3DS', 'PlayStation VR', 'Arcade', 'Family Computer Disk System', 'Nintendo 3DS', 'NES', 'Family Computer (FAMICOM)', 'Windows Phone', 'Xbox', 'Ouya', 'Game Boy Advance', 'OnLive Game System', 'Nintendo DS', 'Web browser', 'Sega Saturn', 'PC-98', 'PC DOS', 'Sega 32X', '3DO Interactive Multiplayer', 'Atari Jaguar', 'Sega Mega Drive/Genesis', 'Nintendo DSi', 'Amazon Fire TV', 'SteamVR', 'Oculus Rift', 'Dreamcast', 'Mobile', 'Amiga', 'Commodore C64/128', 'Game Boy', 'Sega CD', 'Turbografx-16/PC Engine CD', 'Game Boy Color', 'Zeebo', 'N-Gage', 'FM-7', 'Sharp X1', 'Texas Instruments TI-99', 'BlackBerry OS', 'Commodore VIC-20', 'Sharp MZ-2200', 'Palm OS', 'Windows Mixed Reality', 'Tapwave Zodiac', 'Neo Geo CD', 'Neo Geo MVS', 'Neo Geo AES', 'Oculus Quest', 'Oculus Quest 2', 'Blu-ray Player', 'WonderSwan Color', 'Oculus VR', 'MSX2', 'Atari 2600', 'Atari ST/STE', 'ZX Spectrum', 'Amstrad CPC', 'TurboGrafx-16/PC Engine', 'Commodore 16', 'Amiga CD32', 'Windows Mobile', 'Atari 7800', 'Sega Master System', 'SG-1000', 'MSX', 'Sega Game Gear', 'FM Towns', 'NEC PC-6000 Series', 'PC-8801', 'Sharp X68000', 'WonderSwan', 'Atari 5200', 'Atari Jaguar CD', 'Atari 8-bit', 'Apple II', 'Leapster Explorer/LeadPad Explorer', 'Daydream', 'Gear VR', 'Stadia', 'OOParts', 'Atari Lynx', 'Nintendo 64DD', 'Apple IIGS', 'Commodore CDTV', 'Acorn Archimedes', 'BBC Microcomputer System', 'TRS-80', 'ColecoVision', 'Intellivision', 'Commodore Plus/4', 'Acorn Electron', 'DVD Player', 'Philips CD-i', 'Neo Geo Pocket Color', 'Vectrex', 'PC Engine SuperGrafx', 'HP 2100', 'CDC Cyber 70', 'Philips Videopac G7000', 'PDP-10', 'Virtual Boy', 'TRS-80 Color Computer', 'Nintendo PlayStation', 'PC-FX', 'Amstrad PCW', 'Tatung Einstein', 'Playdate', 'Microcomputer', 'Leapster', 'Game & Watch', 'V.Smile', 'Neo Geo Pocket', 'PlayStation Network', 'AY-3-8606', 'EDSAC', 'Handheld Electronic LCD', 'Intellivision Amico', 'Fairchild Channel F', 'Plug & Play', 'Legacy Computer', 'Thomson MO5', 'Bally Astrocade', 'Gamate', 'Hyper Neo Geo 64', 'Commodore PET', 'Dragon 32/64', 'Game.com', 'Odyssey', 'Arduboy', 'VC 4000', '1292 Advanced Programmable Video System', 'Pokémon mini']
# all_value = []
dict_of_all_value = {}
# for i in df[what]:
#     for j in eval(i):
#         if j not in all_value:
#             all_value.append(j)
# print(all_value)

# dict_with_values = {value: [0, 0, 0] for value in all_value}
# print(dict_with_values)

# # Print the dictionary
# print(dict_with_values)

# for i in df.values:
#     for j in all_value:
#         if j in eval(i[5]):
#             dict_with_values[j][0] += i[7]
#             dict_with_values[j][1] += 1
#             dict_with_values[j][2] += i[8]
#
# print(dict_with_values)

result = {'Windows PC': [41789.20000000006, 13659, 1399187400.0], 'PlayStation 4': [13510.999999999993, 4369, 579235600.0], 'Xbox One': [11253.29999999999, 3648, 472943400.0], 'PlayStation 5': [3275.2, 1044, 129616700.0], 'Xbox Series': [3152.900000000003, 990, 129079600.0], 'Wii U': [2159.8999999999996, 697, 110743300.0], 'Nintendo Switch': [11558.099999999975, 3694, 441664100.0], 'Mac': [14368.700000000013, 4619, 505053500.0], 'Linux': [8439.600000000004, 2713, 298144300.0], 'PlayStation Vita': [2626.000000000005, 845, 118834700.0], 'Android': [6324.199999999999, 2119, 212937700.0], 'iOS': [7465.5000000000155, 2509, 261720600.0], 'Xbox 360': [5210.499999999996, 1695, 278384500.0], 'PlayStation 3': [6345.100000000002, 2003, 324427200.0], 'Google Stadia': [804.4999999999999, 257, 41117200.0], 'Wii': [3528.5000000000027, 1178, 180791800.0], 'Nintendo 64': [807.0999999999996, 272, 38525200.0], 'PlayStation': [2954.299999999998, 962, 126934600.0], 'PlayStation Portable': [2251.7000000000003, 706, 107849600.0], 'Playstation VR2': [148.8000000000001, 39, 4514200.0], 'PlayStation 2': [4608.000000000001, 1507, 234872800.0], 'Nintendo GameCube': [1430.1, 472, 83760400.0], 'Super Famicom': [1012.9, 315, 46120100.0], 'SNES': [1379.8000000000015, 483, 67703700.0], 'Satellaview': [183.20000000000002, 53, 10425500.0], 'New Nintendo 3DS': [151.9, 44, 8925600.0], 'PlayStation VR': [381.4000000000001, 122, 10788800.0], 'Arcade': [3430.2999999999965, 1129, 137570100.0], 'Family Computer Disk System': [180.70000000000007, 65, 9011600.0], 'Nintendo 3DS': [2385.800000000002, 760, 114581700.0], 'NES': [1415.6999999999991, 523, 62851600.0], 'Family Computer (FAMICOM)': [748.3000000000002, 265, 30293100.0], 'Windows Phone': [467.4, 166, 18951700.0], 'Xbox': [1909.7999999999995, 617, 109681700.0], 'Ouya': [93.70000000000003, 32, 4549400.0], 'Game Boy Advance': [1618.6000000000015, 568, 56363700.0], 'OnLive Game System': [14.0, 4, 24200.0], 'Nintendo DS': [2237.7999999999984, 755, 97363700.0], 'Web browser': [2596.7000000000007, 849, 56247100.0], 'Sega Saturn': [846.1999999999996, 264, 35822400.0], 'PC-98': [234.50000000000006, 77, 8372500.0], 'PC DOS': [2033.7999999999984, 665, 60708600.0], 'Sega 32X': [49.70000000000001, 21, 3429500.0], '3DO Interactive Multiplayer': [186.29999999999984, 66, 6008600.0], 'Atari Jaguar': [58.1, 23, 3592900.0], 'Sega Mega Drive/Genesis': [1389.900000000002, 490, 58489000.0], 'Nintendo DSi': [208.69999999999993, 70, 5484500.0], 'Amazon Fire TV': [91.19999999999999, 30, 647100.0], 'SteamVR': [460.5999999999998, 138, 10628200.0], 'Oculus Rift': [242.80000000000004, 71, 7905200.0], 'Dreamcast': [688.3999999999995, 216, 34895900.0], 'Mobile': [505.0999999999995, 167, 20174300.0], 'Amiga': [1019.6999999999997, 351, 35121200.0], 'Commodore C64/128': [899.5999999999998, 318, 29831900.0], 'Game Boy': [676.6999999999996, 241, 27107300.0], 'Sega CD': [225.59999999999997, 85, 7778600.0], 'Turbografx-16/PC Engine CD': [137.5, 43, 3482300.0], 'Game Boy Color': [618.5000000000006, 220, 14038300.0], 'Zeebo': [38.300000000000004, 12, 1252400.0], 'N-Gage': [40.6, 14, 1602100.0], 'FM-7': [83.5, 29, 5034900.0], 'Sharp X1': [173.70000000000005, 63, 9585700.0], 'Texas Instruments TI-99': [28.7, 10, 1554400.0], 'BlackBerry OS': [123.60000000000001, 43, 5199300.0], 'Commodore VIC-20': [52.900000000000006, 18, 2758400.0], 'Sharp MZ-2200': [3.4, 1, 5700.0], 'Palm OS': [13.5, 4, 863700.0], 'Windows Mixed Reality': [108.9, 31, 4002500.0], 'Tapwave Zodiac': [12.6, 4, 148600.0], 'Neo Geo CD': [188.1, 59, 11153900.0], 'Neo Geo MVS': [262.9999999999999, 80, 14085600.0], 'Neo Geo AES': [270.2, 83, 15044600.0], 'Oculus Quest': [332.2999999999999, 98, 6833600.0], 'Oculus Quest 2': [369.7999999999997, 107, 5613800.0], 'Blu-ray Player': [8.3, 3, 501900.0], 'WonderSwan Color': [37.8, 13, 1213100.0], 'Oculus VR': [288.1999999999999, 88, 3937700.0], 'MSX2': [77.6, 30, 2159400.0], 'Atari 2600': [348.19999999999976, 135, 9736800.0], 'Atari ST/STE': [644.3000000000004, 227, 22901900.0], 'ZX Spectrum': [526.3, 190, 19113700.0], 'Amstrad CPC': [491.40000000000003, 175, 17606300.0], 'TurboGrafx-16/PC Engine': [296.3, 104, 8658800.0], 'Commodore 16': [38.79999999999999, 13, 840300.0], 'Amiga CD32': [91.49999999999999, 33, 3397600.0], 'Windows Mobile': [13.6, 4, 458800.0], 'Atari 7800': [50.10000000000001, 17, 2290100.0], 'Sega Master System': [414.8999999999999, 160, 18666300.0], 'SG-1000': [68.2, 25, 2761300.0], 'MSX': [397.7999999999998, 142, 14965500.0], 'Sega Game Gear': [341.90000000000003, 126, 18802700.0], 'FM Towns': [172.89999999999995, 56, 7078700.0], 'NEC PC-6000 Series': [29.599999999999998, 11, 2812000.0], 'PC-8801': [185.50000000000003, 66, 8243000.0], 'Sharp X68000': [201.29999999999995, 67, 10037100.0], 'WonderSwan': [54.300000000000004, 17, 1261100.0], 'Atari 5200': [114.20000000000005, 40, 5988800.0], 'Atari Jaguar CD': [13.9, 5, 1019200.0], 'Atari 8-bit': [245.80000000000004, 84, 10916700.0], 'Apple II': [340.79999999999995, 117, 12925800.0], 'Leapster Explorer/LeadPad Explorer': [2.6, 1, 3300.0], 'Daydream': [7.7, 2, 777200.0], 'Gear VR': [18.7, 6, 85200.0], 'Stadia': [24.2, 7, 685000.0], 'OOParts': [38.800000000000004, 13, 2389000.0], 'Atari Lynx': [64.2, 23, 2850200.0], 'Nintendo 64DD': [24.0, 6, 136100.0], 'Apple IIGS': [84.70000000000003, 28, 3174000.0], 'Commodore CDTV': [17.1, 6, 1006000.0], 'Acorn Archimedes': [41.59999999999999, 14, 2704000.0], 'BBC Microcomputer System': [81.8, 28, 3186000.0], 'TRS-80': [40.0, 13, 2133000.0], 'ColecoVision': [108.10000000000004, 38, 5069000.0], 'Intellivision': [52.29999999999999, 19, 3218000.0], 'Commodore Plus/4': [31.099999999999994, 10, 583000.0], 'Acorn Electron': [33.99999999999999, 11, 1133000.0], 'DVD Player': [25.299999999999997, 9, 1722000.0], 'Philips CD-i': [38.699999999999996, 15, 1743000.0], 'Neo Geo Pocket Color': [44.29999999999999, 12, 1253000.0], 'Vectrex': [10.3, 5, 210000.0], 'PC Engine SuperGrafx': [6.5, 2, 121000.0], 'HP 2100': [3.2, 1, 475000.0], 'CDC Cyber 70': [5.7, 2, 494000.0], 'Philips Videopac G7000': [10.899999999999999, 4, 1175000.0], 'PDP-10': [6.4, 2, 118000.0], 'Virtual Boy': [31.9, 11, 1387000.0], 'TRS-80 Color Computer': [34.4, 11, 1021000.0], 'Nintendo PlayStation': [6.0, 2, 334000.0], 'PC-FX': [20.900000000000002, 6, 43000.0], 'Amstrad PCW': [18.6, 6, 517000.0], 'Tatung Einstein': [19.0, 6, 544000.0], 'Playdate': [69.09999999999998, 24, 368000.0], 'Microcomputer': [2.5, 1, 19000.0], 'Leapster': [8.8, 3, 64000.0], 'Game & Watch': [34.5, 12, 385000.0], 'V.Smile': [6.9, 3, 20000.0], 'Neo Geo Pocket': [3.1, 1, 62000.0], 'PlayStation Network': [4.5, 3, 15000.0], 'AY-3-8606': [3.1, 1, 381000.0], 'EDSAC': [3.5, 1, 27000.0], 'Handheld Electronic LCD': [33.3, 11, 146000.0], 'Intellivision Amico': [3.3, 1, 17000.0], 'Fairchild Channel F': [3.7, 1, 6000.0], 'Plug & Play': [8.2, 3, 28000.0], 'Legacy Computer': [4.2, 1, 89000.0], 'Thomson MO5': [5.8, 2, 28000.0], 'Bally Astrocade': [2.9, 1, 60000.0], 'Gamate': [3.2, 1, 8000.0], 'Hyper Neo Geo 64': [2.9, 1, 11000.0], 'Commodore PET': [3.2, 1, 9000.0], 'Dragon 32/64': [3.4, 1, 32000.0], 'Game.com': [1.5, 1, 81000.0], 'Odyssey': [6.2, 2, 34000.0], 'Arduboy': [2.2, 1, 4000.0], 'VC 4000': [2.4, 1, 40000.0], '1292 Advanced Programmable Video System': [2.4, 1, 40000.0], 'Pokémon mini': [2.7, 1, 11000.0]}

for key, var in result.items():
    result[key] = [var[0]/var[1], var[2]]

print(result)
sorted_result = dict(sorted(result.items(), key=lambda x: x[1][1] / x[1][0], reverse=True))
print(sorted_result)

for key, var in sorted_result.items():
    sorted_result[key] = var[0]

print(sorted_result)

data = pd.DataFrame({'Platform': list(sorted_result.keys()), 'Rating': list(sorted_result.values())})


plt.figure(figsize=(10, 6))
s = sns.barplot(x='Platform', y='Rating', data=data)
s.set_xticklabels(s.get_xticklabels(), rotation=50, horizontalalignment="right")
s.set_xlim(right=20)  # Set the x-axis limit
plt.xlabel('Platform')
plt.ylabel('Rating')
plt.title('Top 20 Platforms Based on Rating and Popularity Ratio')
plt.show()


class Model:
    def __init__(self):
        self.df = pd.read_csv('backloggd_games.csv')
        # drop none and unused column
        self.df.dropna(subset=self.df.columns.tolist(), how='any', inplace=True)
        self.string_to_number()

    def game_title(self):
        return self.df["Title"].values.tolist()

    @staticmethod
    def k_destroyer(val):
        """Remove K in csv and *1000 to the value which have K"""
        val = val.replace('K', '')
        val = float(val)
        return val * 1000

    def string_to_number(self):
        """Convert K (1,000) in csv to be integer"""
        for change in self.df.columns.tolist():
            if change in ['Plays', 'Playing', 'Backlogs', 'Wishlist', 'Lists', 'Reviews']:
                self.df[change] = self.df[change].apply(self.k_destroyer)
                self.df[change] = pd.to_numeric(self.df[change], errors='coerce')

    def stats(self, column):
        """Send statistic datas to controller"""
        return {"mean": round(self.df[column].mean(), 3), "median": round(self.df[column].median(), 3),
                "sd": round(self.df[column].std(), 3), "type": self.df[column].dtypes,
                "min": self.df[column].min(), "max": self.df[column].max(), "var": round(self.df[column].var(), 3)}

    def find_game_data(self, name_of_the_game):
        """Send datas of the game to controller"""
        return self.df[self.df['Title'] == name_of_the_game].iloc[0].to_dict()

    @staticmethod
    def pull_image(img_name):
        """sent image to controller"""
        img = Image.open(f"img/{img_name}.png")
        return img

    def create_figure(self, master, x, y) -> FigureCanvasTkAgg:
        # plot the data
        figure = Figure(figsize=(4, 4))
        ax = figure.subplots()

        if x == "empty_x" and y == "empty_y":
            empty_df = pd.DataFrame()
            empty_df[x], empty_df[y] = [], []
            s = sns.barplot(x=x, y=y, data=empty_df, errorbar=None, ax=ax)
        else:
            s = sns.barplot(x=x, y=y, data=self.df, errorbar=None, ax=ax)

        s.set_xticklabels([])
        s.set_yticklabels([])

        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_title(f"Relationship between {x} and {y}")

        canvas = FigureCanvasTkAgg(figure, master=master)
        return canvas
