import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import Image

# df = pd.read_csv('backloggd_games.csv')
# df.dropna(subset=df.columns.tolist(), how='any', inplace=True)
#
# what = "Platforms"
# all_value = ['Windows PC', 'PlayStation 4', 'Xbox One', 'PlayStation 5', 'Xbox Series', 'Wii U', 'Nintendo Switch', 'Mac', 'Linux', 'PlayStation Vita', 'Android', 'iOS', 'Xbox 360', 'PlayStation 3', 'Google Stadia', 'Wii', 'Nintendo 64', 'PlayStation', 'PlayStation Portable', 'Playstation VR2', 'PlayStation 2', 'Nintendo GameCube', 'Super Famicom', 'SNES', 'Satellaview', 'New Nintendo 3DS', 'PlayStation VR', 'Arcade', 'Family Computer Disk System', 'Nintendo 3DS', 'NES', 'Family Computer (FAMICOM)', 'Windows Phone', 'Xbox', 'Ouya', 'Game Boy Advance', 'OnLive Game System', 'Nintendo DS', 'Web browser', 'Sega Saturn', 'PC-98', 'PC DOS', 'Sega 32X', '3DO Interactive Multiplayer', 'Atari Jaguar', 'Sega Mega Drive/Genesis', 'Nintendo DSi', 'Amazon Fire TV', 'SteamVR', 'Oculus Rift', 'Dreamcast', 'Mobile', 'Amiga', 'Commodore C64/128', 'Game Boy', 'Sega CD', 'Turbografx-16/PC Engine CD', 'Game Boy Color', 'Zeebo', 'N-Gage', 'FM-7', 'Sharp X1', 'Texas Instruments TI-99', 'BlackBerry OS', 'Commodore VIC-20', 'Sharp MZ-2200', 'Palm OS', 'Windows Mixed Reality', 'Tapwave Zodiac', 'Neo Geo CD', 'Neo Geo MVS', 'Neo Geo AES', 'Oculus Quest', 'Oculus Quest 2', 'Blu-ray Player', 'WonderSwan Color', 'Oculus VR', 'MSX2', 'Atari 2600', 'Atari ST/STE', 'ZX Spectrum', 'Amstrad CPC', 'TurboGrafx-16/PC Engine', 'Commodore 16', 'Amiga CD32', 'Windows Mobile', 'Atari 7800', 'Sega Master System', 'SG-1000', 'MSX', 'Sega Game Gear', 'FM Towns', 'NEC PC-6000 Series', 'PC-8801', 'Sharp X68000', 'WonderSwan', 'Atari 5200', 'Atari Jaguar CD', 'Atari 8-bit', 'Apple II', 'Leapster Explorer/LeadPad Explorer', 'Daydream', 'Gear VR', 'Stadia', 'OOParts', 'Atari Lynx', 'Nintendo 64DD', 'Apple IIGS', 'Commodore CDTV', 'Acorn Archimedes', 'BBC Microcomputer System', 'TRS-80', 'ColecoVision', 'Intellivision', 'Commodore Plus/4', 'Acorn Electron', 'DVD Player', 'Philips CD-i', 'Neo Geo Pocket Color', 'Vectrex', 'PC Engine SuperGrafx', 'HP 2100', 'CDC Cyber 70', 'Philips Videopac G7000', 'PDP-10', 'Virtual Boy', 'TRS-80 Color Computer', 'Nintendo PlayStation', 'PC-FX', 'Amstrad PCW', 'Tatung Einstein', 'Playdate', 'Microcomputer', 'Leapster', 'Game & Watch', 'V.Smile', 'Neo Geo Pocket', 'PlayStation Network', 'AY-3-8606', 'EDSAC', 'Handheld Electronic LCD', 'Intellivision Amico', 'Fairchild Channel F', 'Plug & Play', 'Legacy Computer', 'Thomson MO5', 'Bally Astrocade', 'Gamate', 'Hyper Neo Geo 64', 'Commodore PET', 'Dragon 32/64', 'Game.com', 'Odyssey', 'Arduboy', 'VC 4000', '1292 Advanced Programmable Video System', 'Pokémon mini']
# # all_value = []
# dict_of_all_value = {}
# # for i in df[what]:
# #     for j in eval(i):
# #         if j not in all_value:
# #             all_value.append(j)
# # print(all_value)
#
# # dict_with_values = {value: [0, 0] for value in all_value}
# # print(dict_with_values)
# dict_with_values = {'Windows PC': [0, 0], 'PlayStation 4': [0, 0], 'Xbox One': [0, 0], 'PlayStation 5': [0, 0], 'Xbox Series': [0, 0], 'Wii U': [0, 0], 'Nintendo Switch': [0, 0], 'Mac': [0, 0], 'Linux': [0, 0], 'PlayStation Vita': [0, 0], 'Android': [0, 0], 'iOS': [0, 0], 'Xbox 360': [0, 0], 'PlayStation 3': [0, 0], 'Google Stadia': [0, 0], 'Wii': [0, 0], 'Nintendo 64': [0, 0], 'PlayStation': [0, 0], 'PlayStation Portable': [0, 0], 'Playstation VR2': [0, 0], 'PlayStation 2': [0, 0], 'Nintendo GameCube': [0, 0], 'Super Famicom': [0, 0], 'SNES': [0, 0], 'Satellaview': [0, 0], 'New Nintendo 3DS': [0, 0], 'PlayStation VR': [0, 0], 'Arcade': [0, 0], 'Family Computer Disk System': [0, 0], 'Nintendo 3DS': [0, 0], 'NES': [0, 0], 'Family Computer (FAMICOM)': [0, 0], 'Windows Phone': [0, 0], 'Xbox': [0, 0], 'Ouya': [0, 0], 'Game Boy Advance': [0, 0], 'OnLive Game System': [0, 0], 'Nintendo DS': [0, 0], 'Web browser': [0, 0], 'Sega Saturn': [0, 0], 'PC-98': [0, 0], 'PC DOS': [0, 0], 'Sega 32X': [0, 0], '3DO Interactive Multiplayer': [0, 0], 'Atari Jaguar': [0, 0], 'Sega Mega Drive/Genesis': [0, 0], 'Nintendo DSi': [0, 0], 'Amazon Fire TV': [0, 0], 'SteamVR': [0, 0], 'Oculus Rift': [0, 0], 'Dreamcast': [0, 0], 'Mobile': [0, 0], 'Amiga': [0, 0], 'Commodore C64/128': [0, 0], 'Game Boy': [0, 0], 'Sega CD': [0, 0], 'Turbografx-16/PC Engine CD': [0, 0], 'Game Boy Color': [0, 0], 'Zeebo': [0, 0], 'N-Gage': [0, 0], 'FM-7': [0, 0], 'Sharp X1': [0, 0], 'Texas Instruments TI-99': [0, 0], 'BlackBerry OS': [0, 0], 'Commodore VIC-20': [0, 0], 'Sharp MZ-2200': [0, 0], 'Palm OS': [0, 0], 'Windows Mixed Reality': [0, 0], 'Tapwave Zodiac': [0, 0], 'Neo Geo CD': [0, 0], 'Neo Geo MVS': [0, 0], 'Neo Geo AES': [0, 0], 'Oculus Quest': [0, 0], 'Oculus Quest 2': [0, 0], 'Blu-ray Player': [0, 0], 'WonderSwan Color': [0, 0], 'Oculus VR': [0, 0], 'MSX2': [0, 0], 'Atari 2600': [0, 0], 'Atari ST/STE': [0, 0], 'ZX Spectrum': [0, 0], 'Amstrad CPC': [0, 0], 'TurboGrafx-16/PC Engine': [0, 0], 'Commodore 16': [0, 0], 'Amiga CD32': [0, 0], 'Windows Mobile': [0, 0], 'Atari 7800': [0, 0], 'Sega Master System': [0, 0], 'SG-1000': [0, 0], 'MSX': [0, 0], 'Sega Game Gear': [0, 0], 'FM Towns': [0, 0], 'NEC PC-6000 Series': [0, 0], 'PC-8801': [0, 0], 'Sharp X68000': [0, 0], 'WonderSwan': [0, 0], 'Atari 5200': [0, 0], 'Atari Jaguar CD': [0, 0], 'Atari 8-bit': [0, 0], 'Apple II': [0, 0], 'Leapster Explorer/LeadPad Explorer': [0, 0], 'Daydream': [0, 0], 'Gear VR': [0, 0], 'Stadia': [0, 0], 'OOParts': [0, 0], 'Atari Lynx': [0, 0], 'Nintendo 64DD': [0, 0], 'Apple IIGS': [0, 0], 'Commodore CDTV': [0, 0], 'Acorn Archimedes': [0, 0], 'BBC Microcomputer System': [0, 0], 'TRS-80': [0, 0], 'ColecoVision': [0, 0], 'Intellivision': [0, 0], 'Commodore Plus/4': [0, 0], 'Acorn Electron': [0, 0], 'DVD Player': [0, 0], 'Philips CD-i': [0, 0], 'Neo Geo Pocket Color': [0, 0], 'Vectrex': [0, 0], 'PC Engine SuperGrafx': [0, 0], 'HP 2100': [0, 0], 'CDC Cyber 70': [0, 0], 'Philips Videopac G7000': [0, 0], 'PDP-10': [0, 0], 'Virtual Boy': [0, 0], 'TRS-80 Color Computer': [0, 0], 'Nintendo PlayStation': [0, 0], 'PC-FX': [0, 0], 'Amstrad PCW': [0, 0], 'Tatung Einstein': [0, 0], 'Playdate': [0, 0], 'Microcomputer': [0, 0], 'Leapster': [0, 0], 'Game & Watch': [0, 0], 'V.Smile': [0, 0], 'Neo Geo Pocket': [0, 0], 'PlayStation Network': [0, 0], 'AY-3-8606': [0, 0], 'EDSAC': [0, 0], 'Handheld Electronic LCD': [0, 0], 'Intellivision Amico': [0, 0], 'Fairchild Channel F': [0, 0], 'Plug & Play': [0, 0], 'Legacy Computer': [0, 0], 'Thomson MO5': [0, 0], 'Bally Astrocade': [0, 0], 'Gamate': [0, 0], 'Hyper Neo Geo 64': [0, 0], 'Commodore PET': [0, 0], 'Dragon 32/64': [0, 0], 'Game.com': [0, 0], 'Odyssey': [0, 0], 'Arduboy': [0, 0], 'VC 4000': [0, 0], '1292 Advanced Programmable Video System': [0, 0], 'Pokémon mini': [0, 0]}
#
# # # Print the dictionary
# # print(dict_with_values)
# #
# for i in df.values:
#     for j in all_value:
#         if j in eval(i[5]):
#             dict_with_values[j][0] += i[7]
#             dict_with_values[j][1] += 1
#
# print(dict_with_values)

result = {'Windows PC': [41789.20000000006, 13659], 'PlayStation 4': [13510.999999999993, 4369], 'Xbox One': [11253.29999999999, 3648], 'PlayStation 5': [3275.2, 1044], 'Xbox Series': [3152.900000000003, 990], 'Wii U': [2159.8999999999996, 697], 'Nintendo Switch': [11558.099999999975, 3694], 'Mac': [14368.700000000013, 4619], 'Linux': [8439.600000000004, 2713], 'PlayStation Vita': [2626.000000000005, 845], 'Android': [6324.199999999999, 2119], 'iOS': [7465.5000000000155, 2509], 'Xbox 360': [5210.499999999996, 1695], 'PlayStation 3': [6345.100000000002, 2003], 'Google Stadia': [804.4999999999999, 257], 'Wii': [3528.5000000000027, 1178], 'Nintendo 64': [807.0999999999996, 272], 'PlayStation': [2954.299999999998, 962], 'PlayStation Portable': [2251.7000000000003, 706], 'Playstation VR2': [148.8000000000001, 39], 'PlayStation 2': [4608.000000000001, 1507], 'Nintendo GameCube': [1430.1, 472], 'Super Famicom': [1012.9, 315], 'SNES': [1379.8000000000015, 483], 'Satellaview': [183.20000000000002, 53], 'New Nintendo 3DS': [151.9, 44], 'PlayStation VR': [381.4000000000001, 122], 'Arcade': [3430.2999999999965, 1129], 'Family Computer Disk System': [180.70000000000007, 65], 'Nintendo 3DS': [2385.800000000002, 760], 'NES': [1415.6999999999991, 523], 'Family Computer (FAMICOM)': [748.3000000000002, 265], 'Windows Phone': [467.4, 166], 'Xbox': [1909.7999999999995, 617], 'Ouya': [93.70000000000003, 32], 'Game Boy Advance': [1618.6000000000015, 568], 'OnLive Game System': [14.0, 4], 'Nintendo DS': [2237.7999999999984, 755], 'Web browser': [2596.7000000000007, 849], 'Sega Saturn': [846.1999999999996, 264], 'PC-98': [234.50000000000006, 77], 'PC DOS': [2033.7999999999984, 665], 'Sega 32X': [49.70000000000001, 21], '3DO Interactive Multiplayer': [186.29999999999984, 66], 'Atari Jaguar': [58.1, 23], 'Sega Mega Drive/Genesis': [1389.900000000002, 490], 'Nintendo DSi': [208.69999999999993, 70], 'Amazon Fire TV': [91.19999999999999, 30], 'SteamVR': [460.5999999999998, 138], 'Oculus Rift': [242.80000000000004, 71], 'Dreamcast': [688.3999999999995, 216], 'Mobile': [505.0999999999995, 167], 'Amiga': [1019.6999999999997, 351], 'Commodore C64/128': [899.5999999999998, 318], 'Game Boy': [676.6999999999996, 241], 'Sega CD': [225.59999999999997, 85], 'Turbografx-16/PC Engine CD': [137.5, 43], 'Game Boy Color': [618.5000000000006, 220], 'Zeebo': [38.300000000000004, 12], 'N-Gage': [40.6, 14], 'FM-7': [83.5, 29], 'Sharp X1': [173.70000000000005, 63], 'Texas Instruments TI-99': [28.7, 10], 'BlackBerry OS': [123.60000000000001, 43], 'Commodore VIC-20': [52.900000000000006, 18], 'Sharp MZ-2200': [3.4, 1], 'Palm OS': [13.5, 4], 'Windows Mixed Reality': [108.9, 31], 'Tapwave Zodiac': [12.6, 4], 'Neo Geo CD': [188.1, 59], 'Neo Geo MVS': [262.9999999999999, 80], 'Neo Geo AES': [270.2, 83], 'Oculus Quest': [332.2999999999999, 98], 'Oculus Quest 2': [369.7999999999997, 107], 'Blu-ray Player': [8.3, 3], 'WonderSwan Color': [37.8, 13], 'Oculus VR': [288.1999999999999, 88], 'MSX2': [77.6, 30], 'Atari 2600': [348.19999999999976, 135], 'Atari ST/STE': [644.3000000000004, 227], 'ZX Spectrum': [526.3, 190], 'Amstrad CPC': [491.40000000000003, 175], 'TurboGrafx-16/PC Engine': [296.3, 104], 'Commodore 16': [38.79999999999999, 13], 'Amiga CD32': [91.49999999999999, 33], 'Windows Mobile': [13.6, 4], 'Atari 7800': [50.10000000000001, 17], 'Sega Master System': [414.8999999999999, 160], 'SG-1000': [68.2, 25], 'MSX': [397.7999999999998, 142], 'Sega Game Gear': [341.90000000000003, 126], 'FM Towns': [172.89999999999995, 56], 'NEC PC-6000 Series': [29.599999999999998, 11], 'PC-8801': [185.50000000000003, 66], 'Sharp X68000': [201.29999999999995, 67], 'WonderSwan': [54.300000000000004, 17], 'Atari 5200': [114.20000000000005, 40], 'Atari Jaguar CD': [13.9, 5], 'Atari 8-bit': [245.80000000000004, 84], 'Apple II': [340.79999999999995, 117], 'Leapster Explorer/LeadPad Explorer': [2.6, 1], 'Daydream': [7.7, 2], 'Gear VR': [18.7, 6], 'Stadia': [24.2, 7], 'OOParts': [38.800000000000004, 13], 'Atari Lynx': [64.2, 23], 'Nintendo 64DD': [24.0, 6], 'Apple IIGS': [84.70000000000003, 28], 'Commodore CDTV': [17.1, 6], 'Acorn Archimedes': [41.59999999999999, 14], 'BBC Microcomputer System': [81.8, 28], 'TRS-80': [40.0, 13], 'ColecoVision': [108.10000000000004, 38], 'Intellivision': [52.29999999999999, 19], 'Commodore Plus/4': [31.099999999999994, 10], 'Acorn Electron': [33.99999999999999, 11], 'DVD Player': [25.299999999999997, 9], 'Philips CD-i': [38.699999999999996, 15], 'Neo Geo Pocket Color': [44.29999999999999, 12], 'Vectrex': [10.3, 5], 'PC Engine SuperGrafx': [6.5, 2], 'HP 2100': [3.2, 1], 'CDC Cyber 70': [5.7, 2], 'Philips Videopac G7000': [10.899999999999999, 4], 'PDP-10': [6.4, 2], 'Virtual Boy': [31.9, 11], 'TRS-80 Color Computer': [34.4, 11], 'Nintendo PlayStation': [6.0, 2], 'PC-FX': [20.900000000000002, 6], 'Amstrad PCW': [18.6, 6], 'Tatung Einstein': [19.0, 6], 'Playdate': [69.09999999999998, 24], 'Microcomputer': [2.5, 1], 'Leapster': [8.8, 3], 'Game & Watch': [34.5, 12], 'V.Smile': [6.9, 3], 'Neo Geo Pocket': [3.1, 1], 'PlayStation Network': [4.5, 3], 'AY-3-8606': [3.1, 1], 'EDSAC': [3.5, 1], 'Handheld Electronic LCD': [33.3, 11], 'Intellivision Amico': [3.3, 1], 'Fairchild Channel F': [3.7, 1], 'Plug & Play': [8.2, 3], 'Legacy Computer': [4.2, 1], 'Thomson MO5': [5.8, 2], 'Bally Astrocade': [2.9, 1], 'Gamate': [3.2, 1], 'Hyper Neo Geo 64': [2.9, 1], 'Commodore PET': [3.2, 1], 'Dragon 32/64': [3.4, 1], 'Game.com': [1.5, 1], 'Odyssey': [6.2, 2], 'Arduboy': [2.2, 1], 'VC 4000': [2.4, 1], '1292 Advanced Programmable Video System': [2.4, 1], 'Pokémon mini': [2.7, 1]}
sorted_result = dict(sorted(result.items(), key=lambda x: x[1][0], reverse=True))
print(sorted_result)
for key, var in result.items():
    sorted_result[key] = var[0]/var[1]
print(sorted_result)

data = pd.DataFrame({'Platform': list(sorted_result.keys()), 'Rating': list(sorted_result.values())})
data = data.sort_values(by=['Rating'], ascending=False)

plt.figure(figsize=(10, 6))
s = sns.barplot(x='Platform', y='Rating', data=data)
s.set_xticklabels(s.get_xticklabels(), rotation=50, horizontalalignment="right")
s.set_xlim(right=20)  # Set the x-axis limit
plt.xlabel('Platform')
plt.ylabel('Rating')
plt.title('Top 20 Platforms with the highest Rating')
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
