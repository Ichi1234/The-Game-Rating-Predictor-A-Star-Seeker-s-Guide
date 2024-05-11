from CTkMessagebox import CTkMessagebox
import customtkinter as tk


class Controller:
    """MVC Controller"""

    def __init__(self, model=None, view=None):
        self.model = model
        self.view = view
        self.menu = {"login": LoginController, "game": GameController, "stat": StatController,
                     "forum": ForumController, "credit": CreditController}

    def dark_mode(self):
        """Switch to dark mode or light mode"""
        if self.view.dark_mode.get():
            tk.set_appearance_mode("dark")
        else:
            tk.set_appearance_mode("light")

    def start_program(self):
        """Start the Program"""
        self.view.switch_menu("login", LoginController(self.view, self.model))
        self.view.main_loop()

    def menu_button(self, menu_name, event):
        """method for bind menu button"""
        self.view.menu_window.destroy()
        self.view.app.columnconfigure(1, weight=0)
        self.view.current_menu.grid(row=1, column=0, sticky="news", rowspan=2)
        self.view.menu_window = None
        self.view.switch_menu(menu_name, self.menu[menu_name](self.view, self.model))

    def menu_title_button(self):
        """method for bind menu button"""
        if not self.view.menu_window:
            self.view.app.columnconfigure(0, weight=1)
            self.view.app.columnconfigure(1, weight=10)
            self.view.current_menu.grid(row=1, column=1, sticky="news", rowspan=2)
            self.view.menu_window_creation()
        else:
            self.view.menu_window.destroy()
            self.view.app.columnconfigure(1, weight=0)
            self.view.current_menu.grid(row=1, column=0, sticky="news", rowspan=2)
            self.view.menu_window = None


class LoginController(Controller):
    """Controller class for login class"""

    def __init__(self, view, model):
        """Initialize for LoginController"""
        super().__init__()
        self.view = view
        self.model = model

    def signin(self, user, password, event):
        """This method use for login button in Login class"""
        if not user or not password:
            CTkMessagebox(title="Error", message="Invalid Username or Password.", icon="cancel")
        else:
            if self.model.check_password(user, password):
                self.view.controller = self
                self.view.switch_menu("game", GameController(self.view, self.model))
                self.view.menu_button.configure(command=self.menu_title_button)
            else:
                CTkMessagebox(title="Error", message="Your Username or Password is wrong.", icon="cancel")

    def signup(self, master, event):
        """This method use for signup button in Login class"""
        self.view.menu['up'](master, self)

    def add_new_people(self, user, password):
        """add new user to csv file"""
        if not user or not password:
            CTkMessagebox(title="Error", message="Invalid Username or Password.", icon="cancel")
        else:
            update = self.model.update_csv("pass", {'Username': user, 'Password': password})
            if not update:
                CTkMessagebox(title="Error", message="Please close csv file that you are opening.", icon="cancel")
            elif update == "exist":
                CTkMessagebox(title="Error", message="This Username already taken.", icon="cancel")

            else:
                CTkMessagebox(title="Success",
                              message="Congratulations, your account has been successfully created."
                                      "\nPlease close this window.", icon="check")


class GameController:
    """Controller class for game data class"""

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def get_game_title(self):
        """Get game title from model then send it to view"""
        return self.model.game_title()

    def get_data_of_the_game(self, game_name):
        """Get data of the game from model"""
        data = self.model.find_game_data(game_name)

        # add new line if summary is too long
        data['Summary'] = "\n".join([data['Summary'][i:i + 45] for i in range(0, len(data['Summary']), 45)])

        # if data is list turn it to str
        data['Genres'] = self.fix_toolong_text(",".join(eval(data['Genres'])))
        data['Platforms'] = self.fix_toolong_text(",".join(eval(data['Platforms'])))

        # make numerical data look better to present
        if data['Plays'] > 999:
            data['Plays'] = str(data['Plays'] / 1000) + "K"

        self.view.current_menu.game_title.configure(text=f"{data['Title']}: Datas")
        self.view.current_menu.summary.configure(text=f"{data['Summary']}")
        self.view.current_menu.player.configure(text=f"Totals Players: {data['Plays']}")
        self.view.current_menu.rating.configure(text=f"Rating: {data['Rating']}")
        self.view.current_menu.genres.configure(text=f"Genres: {data['Genres']}")
        self.view.current_menu.platform.configure(text=f"Platforms: {data['Platforms']}")

    @staticmethod
    def fix_toolong_text(data: str):
        """If the data is too long frame will extend and my layout will broke
        This method is use to create a new line if the data is too long"""
        split_data = data.split(",")
        new_str = []
        for i in range(len(split_data)):
            if i % 3 == 0 and i != 0 and len(data) > 38:
                new_str.append(f"\n{split_data[i]}")
            else:
                new_str.append(split_data[i])
        return ",".join(new_str)


class StatController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def change_statistic_menu(self, statistic_menu: str):
        """This method is use for change statistic menu"""
        self.view.app.columnconfigure(1, weight=0)
        self.view.current_menu.grid(row=1, column=0, sticky="news", rowspan=2)
        self.view.menu_window = None
        self.view.switch_menu(statistic_menu, StatController(self.view, self.model))

    def user_select_graph(self, master, x, y):
        """This method is use for create graph in UserGraph class"""
        user_graph = self.model.create_figure(master, x, y)
        user_graph.get_tk_widget().grid(row=0, column=0)

    def pull_img_model(self, img_name: str, size: tuple = (450, 300)):
        """Pull image from database"""
        return tk.CTkImage(light_image=self.model.pull_image(img_name), size=size)

    def story_graph(self, which):
        """Apply image to StoryTelling Class"""
        img = self.pull_img_model(which)
        self.view.current_menu.graph.configure(image=img)

    def get_statistic(self, column: str):
        """Get statistic dict from model"""
        data = self.model.stats(column)
        self.view.current_menu.database.configure(text=f"Mean = {data['mean']}\nMedian = {data['median']}"
                                                       f"\nS.D. = {data['sd']}\nMin = {data['min']}"
                                                       f"\nMax = {data['max']}\nVariance = {data['var']}"
                                                       f"\nTypes of Data = {data['type']}")


class ForumController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def create_new_post(self, post_title: str, master, event):
        """Use for create new forum post"""
        if not post_title:
            CTkMessagebox(title="Error", message="Please input something for your post title.", icon="cancel")
        else:
            self.view.current_menu.user_entry.delete(0, tk.END)
            update = self.model.new_post(post_title)

            if not update:
                CTkMessagebox(title="Error", message="Please close csv file that you are opening.", icon="cancel")
            else:
                forum_data_dict = self.model.show_post()

                new_frame = tk.CTkFrame(master.post_frame)
                new_frame.columnconfigure(0, weight=1)
                button = tk.CTkButton(new_frame, text=forum_data_dict[-1]["Title"], anchor="w",
                                      command=lambda data=forum_data_dict[-1]: self.select_forum(data))

                user_label = tk.CTkLabel(new_frame, text=f"-{forum_data_dict[-1]['Name']}-")
                button.grid(column=0, columnspan=10, sticky="new")
                user_label.grid(column=0, columnspan=10, sticky="se")
                new_frame.pack(fill="both", expand=True)

    def display_all_forum(self, master):
        """Pack every forum from database"""
        forum_data_dict = self.model.show_post()

        for data_dict in forum_data_dict:
            new_frame = tk.CTkFrame(master.post_frame)
            new_frame.columnconfigure(0, weight=1)
            button = tk.CTkButton(new_frame, text=data_dict["Title"], anchor="w",
                                  command=lambda data=data_dict: self.select_forum(data))
            user_label = tk.CTkLabel(new_frame, text=f"-{data_dict['Name']}-")
            button.grid(column=0, columnspan=10, sticky="new")
            user_label.grid(column=0, columnspan=10, sticky="se")
            new_frame.pack(fill="both", expand=True)

    def select_forum(self, data: dict):
        """switch window to selected forum"""
        self.view.forum_data = data
        self.view.switch_menu("UserForum", ForumController(self.view, self.model))

    def new_comment(self, comment: str, data: dict, event):
        """Add new comment to database and display it"""
        self.view.current_menu.new_comment_text.delete(0, tk.END)

        update = False
        list_of_data = []
        for key, val in data.items():
            if val == "waiting-for-user-to-comment":
                data[key] = comment
                data[f"user_{key[-1]}"] = self.model.user
                list_of_data = [key, f"user_{key[-1]}", [comment, self.model.user]]
                update = True
                break
        if not update:
            key = [i for i in data.keys()]
            try:
                data.update(
                    {f"com_{int(key[-1][-1]) + 1}": comment, f"user_{int(key[-1][-1]) + 1}": self.model.user})
                list_of_data = [f"com_{int(key[-1][-1])}", f"user_{int(key[-1][-1])}", [comment, self.model.user]]
            except ValueError:
                data.update({"com_0": comment, "user_0": self.model.user})
                list_of_data = ["com_0", "user_0", [comment, self.model.user]]

        success = self.model.update_csv("forum", data, list_of_data)
        if not success:
            CTkMessagebox(title="Error", message="Please close csv file that you are opening.", icon="cancel")
        else:
            current_comment = list(data.values())[2:]
            user_name = []
            user_comment = []
            for i in range(len(current_comment)):
                if i % 2 == 0:
                    user_comment.append(current_comment[i])
                else:
                    user_name.append(current_comment[i])

            for comment in range(len(user_comment)):
                comment_frame = tk.CTkFrame(self.view.current_menu.frame_for_comment)

                if comment == "waiting-for-user-to-comment":
                    break
                elif (user_name[comment], user_comment[comment]) in self.view.current_menu.track_comment:
                    continue
                else:
                    who_comment = tk.CTkLabel(comment_frame, text=f"{user_name[comment]} :", font=("Arial", 18))
                    who_comment.pack(side="left", padx=10)

                    if len(user_comment[comment]) > 170:
                        spaced_com = self.fix_toolong_text(user_comment[comment], 170)
                    else:
                        spaced_com = user_comment[comment]

                    add_comment = tk.CTkLabel(comment_frame, text=spaced_com, font=("Arial", 16))
                    add_comment.pack(side="left", padx=10)

                comment_frame.pack(side="top", expand=True, anchor="w", pady=5)
                self.view.current_menu.track_comment.append((user_name[comment], user_comment[comment]))
                break

    @staticmethod
    def fix_toolong_text(data: str, space: int):
        """If the data is too long frame will extend and my layout will broke
        This method is use to create a new line if the data is too long"""
        space_data = [data[i:i + space] for i in range(0, len(data), space)]
        return '\n'.join(space_data)


class CreditController:
    def __init__(self, view, model):
        self.view = view
        self.model = model
