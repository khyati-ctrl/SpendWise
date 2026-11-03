import customtkinter as ctk
from tkinter import ttk, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# -------------------- APP CONFIGURATION --------------------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

APP_BG = "#F4F7FB"
SIDEBAR_BG = "#172B3A"
PRIMARY = "#176B62"
PRIMARY_LIGHT = "#E5F2EF"
TEXT = "#172B3A"
MUTED = "#718096"
WHITE = "#FFFFFF"
RED = "#C15A4A"
BORDER = "#E4EAF0"

class SpendWiseApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SpendWise | Student Expense Tracker")
        self.geometry("1250x780")
        self.minsize(1050, 680)
        self.configure(fg_color=APP_BG)

        self.current_page = None
        self.nav_buttons = {}

        self.create_sidebar()
        self.create_main_area()
        self.show_page("Dashboard")

    # -------------------- LAYOUT --------------------
    def create_sidebar(self):
        self.sidebar = ctk.CTkFrame(
            self, width=235, corner_radius=0, fg_color=SIDEBAR_BG
        )
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        brand = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        brand.pack(fill="x", padx=22, pady=(28, 38))

        ctk.CTkLabel(
            brand, text="◈", font=ctk.CTkFont(size=30, weight="bold"),
            text_color="#64C8B7"
        ).pack(side="left", padx=(0, 10))

        title_box = ctk.CTkFrame(brand, fg_color="transparent")
        title_box.pack(side="left")
        ctk.CTkLabel(
            title_box, text="SpendWise",
            font=ctk.CTkFont(size=21, weight="bold"), text_color=WHITE
        ).pack(anchor="w")
        ctk.CTkLabel(
            title_box, text="STUDENT EDITION",
            font=ctk.CTkFont(size=9, weight="bold"), text_color="#9CB2C3"
        ).pack(anchor="w", pady=(1, 0))

        ctk.CTkLabel(
            self.sidebar, text="MENU",
            font=ctk.CTkFont(size=10, weight="bold"),
            text_color="#8299AA"
        ).pack(anchor="w", padx=25, pady=(0, 12))

        items = [
            ("Dashboard", "⌂"),
            ("Add Expense", "+"),
            ("Transactions", "▤"),
            ("Analytics", "▥"),
        ]

        for name, symbol in items:
            button = ctk.CTkButton(
                self.sidebar,
                text=f"   {symbol}     {name}",
                anchor="w",
                height=45,
                corner_radius=10,
                fg_color="transparent",
                hover_color="#294354",
                text_color="#D6E1E9",
                font=ctk.CTkFont(size=14),
                command=lambda page=name: self.show_page(page)
            )
            button.pack(fill="x", padx=14, pady=4)
            self.nav_buttons[name] = button

        # Keep the reminder card anchored to the bottom of the sidebar.
        # It remains visible when the window is maximized or resized.
        footer = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        footer.pack(side="bottom", fill="x", padx=15, pady=(10, 14))

        ctk.CTkLabel(
            footer, text="SpendWise v1.0",
            font=ctk.CTkFont(size=10), text_color="#8299AA"
        ).pack(anchor="center")

    def create_main_area(self):
        self.main = ctk.CTkFrame(self, fg_color=APP_BG, corner_radius=0)
        self.main.pack(side="left", fill="both", expand=True)

        self.header = ctk.CTkFrame(self.main, fg_color="transparent")
        self.header.pack(fill="x", padx=32, pady=(25, 12))

        self.page_title = ctk.CTkLabel(
            self.header, text="Dashboard",
            font=ctk.CTkFont(size=27, weight="bold"), text_color=TEXT
        )
        self.page_title.pack(side="left")

        self.date_label = ctk.CTkLabel(
            self.header, text="November 2026",
            font=ctk.CTkFont(size=13), text_color=MUTED
        )
        self.date_label.pack(side="right", padx=5)

        self.content = ctk.CTkFrame(self.main, fg_color="transparent")
        self.content.pack(fill="both", expand=True, padx=32, pady=(5, 25))

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_page(self, page):
        self.current_page = page
        self.page_title.configure(text=page)
        for name, button in self.nav_buttons.items():
            if name == page:
                button.configure(fg_color=PRIMARY, text_color=WHITE)
            else:
                button.configure(fg_color="transparent", text_color="#D6E1E9")

        self.clear_content()
        if page == "Dashboard":
            self.build_dashboard()
        elif page == "Add Expense":
            self.build_add_expense()
        elif page == "Transactions":
            self.build_transactions()
        elif page == "Analytics":
            self.build_analytics()

    # -------------------- REUSABLE COMPONENTS --------------------
    def card(self, parent, title, value, subtitle, accent=PRIMARY):
        frame = ctk.CTkFrame(
            parent, fg_color=WHITE, corner_radius=14,
            border_width=1, border_color=BORDER
        )
        frame.pack(side="left", fill="both", expand=True, padx=6)
        ctk.CTkLabel(
            frame, text=title, font=ctk.CTkFont(size=12),
            text_color=MUTED
        ).pack(anchor="w", padx=17, pady=(15, 5))
        ctk.CTkLabel(
            frame, text=value, font=ctk.CTkFont(size=24, weight="bold"),
            text_color=accent
        ).pack(anchor="w", padx=17)
        ctk.CTkLabel(
            frame, text=subtitle, font=ctk.CTkFont(size=10),
            text_color=MUTED
        ).pack(anchor="w", padx=17, pady=(3, 15))
        return frame

    def section_title(self, parent, title, subtitle=None):
        ctk.CTkLabel(
            parent, text=title, font=ctk.CTkFont(size=16, weight="bold"),
            text_color=TEXT
        ).pack(anchor="w")
        if subtitle:
            ctk.CTkLabel(
                parent, text=subtitle, font=ctk.CTkFont(size=11),
                text_color=MUTED
            ).pack(anchor="w", pady=(3, 8))

    # -------------------- DASHBOARD --------------------
    def build_dashboard(self):
        top = ctk.CTkFrame(self.content, fg_color="transparent")
        top.pack(fill="x", pady=(0, 15))
        ctk.CTkLabel(
            top, text="Welcome back!",
            font=ctk.CTkFont(size=17, weight="bold"), text_color=TEXT
        ).pack(anchor="w")
        ctk.CTkLabel(
            top, text="Here's an overview of your spending this month.",
            font=ctk.CTkFont(size=12), text_color=MUTED
        ).pack(anchor="w", pady=(3, 0))

        cards = ctk.CTkFrame(self.content, fg_color="transparent")
        cards.pack(fill="x", pady=(0, 16))
        self.card(cards, "MONTHLY BUDGET", "₹5,000", "Your spending limit")
        self.card(cards, "TOTAL SPENT", "₹3,250", "This month", RED)
        self.card(cards, "REMAINING", "₹1,750", "Budget left", PRIMARY)
        self.card(cards, "DAILY AVERAGE", "₹108", "Average per day", "#4776A8")

        middle = ctk.CTkFrame(self.content, fg_color="transparent")
        middle.pack(fill="x", pady=(0, 15))

        budget = ctk.CTkFrame(
            middle, fg_color=WHITE, corner_radius=14,
            border_width=1, border_color=BORDER
        )
        budget.pack(side="left", fill="both", expand=True, padx=(0, 7))
        ctk.CTkLabel(
            budget, text="Monthly Budget",
            font=ctk.CTkFont(size=16, weight="bold"), text_color=TEXT
        ).pack(anchor="w", padx=18, pady=(16, 3))
        ctk.CTkLabel(
            budget, text="You've used 65% of your monthly budget.",
            font=ctk.CTkFont(size=11), text_color=MUTED
        ).pack(anchor="w", padx=18, pady=(0, 12))
        progress = ctk.CTkProgressBar(
            budget, height=12, progress_color=PRIMARY,
            fg_color="#E7EFED", corner_radius=8
        )
        progress.pack(fill="x", padx=18, pady=(0, 8))
        progress.set(0.65)
        row = ctk.CTkFrame(budget, fg_color="transparent")
        row.pack(fill="x", padx=18, pady=(0, 15))
        ctk.CTkLabel(
            row, text="₹3,250 spent", font=ctk.CTkFont(size=11),
            text_color=TEXT
        ).pack(side="left")
        ctk.CTkLabel(
            row, text="₹5,000", font=ctk.CTkFont(size=11),
            text_color=MUTED
        ).pack(side="right")

        insight = ctk.CTkFrame(
            middle, fg_color=PRIMARY_LIGHT, corner_radius=14
        )
        insight.pack(side="left", fill="both", expand=True, padx=(7, 0))
        ctk.CTkLabel(
            insight, text="✦  SPENDING INSIGHT",
            font=ctk.CTkFont(size=12, weight="bold"), text_color=PRIMARY
        ).pack(anchor="w", padx=18, pady=(16, 8))
        ctk.CTkLabel(
            insight,
            text="Food is your highest spending category this month.",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=TEXT, wraplength=300, justify="left"
        ).pack(anchor="w", padx=18)
        ctk.CTkLabel(
            insight, text="Try setting a weekly food budget to keep your spending balanced.",
            font=ctk.CTkFont(size=11), text_color="#55736D",
            wraplength=300, justify="left"
        ).pack(anchor="w", padx=18, pady=(5, 15))

        bottom = ctk.CTkFrame(self.content, fg_color="transparent")
        bottom.pack(fill="both", expand=True)

        chart_card = ctk.CTkFrame(
            bottom, fg_color=WHITE, corner_radius=14,
            border_width=1, border_color=BORDER
        )
        chart_card.pack(side="left", fill="both", expand=True, padx=(0, 7))
        ctk.CTkLabel(
            chart_card, text="Spending by Category",
            font=ctk.CTkFont(size=15, weight="bold"), text_color=TEXT
        ).pack(anchor="w", padx=16, pady=(13, 0))
        self.draw_pie_chart(chart_card)

        recent = ctk.CTkFrame(
            bottom, fg_color=WHITE, corner_radius=14,
            border_width=1, border_color=BORDER
        )
        recent.pack(side="left", fill="both", expand=True, padx=(7, 0))
        ctk.CTkLabel(
            recent, text="Recent Transactions",
            font=ctk.CTkFont(size=15, weight="bold"), text_color=TEXT
        ).pack(anchor="w", padx=16, pady=(13, 8))
        self.add_recent_row(recent, "Lunch", "Food · Today", "− ₹180", RED)
        self.add_recent_row(recent, "Bus pass", "Transport · Yesterday", "− ₹500", RED)
        self.add_recent_row(recent, "Notebook", "Academics · 1 Nov", "− ₹120", RED)
        self.add_recent_row(recent, "Movie", "Entertainment · 30 Oct", "− ₹250", RED)

    def draw_pie_chart(self, parent):
        fig = Figure(figsize=(4.2, 2.5), dpi=90, facecolor=WHITE)
        ax = fig.add_subplot(111)
        values = [1200, 700, 500, 450, 400]
        labels = ["Food", "Transport", "Academics", "Shopping", "Other"]
        colors = ["#176B62", "#5C9E95", "#8BBDB5", "#E5B96B", "#9AAEC0"]
        ax.pie(
            values, labels=labels, autopct="%1.0f%%",
            startangle=90, colors=colors,
            textprops={"fontsize": 8, "color": TEXT},
            wedgeprops={"linewidth": 2, "edgecolor": WHITE}
        )
        ax.axis("equal")
        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=8, pady=(0, 5))

    def add_recent_row(self, parent, name, detail, amount, color):
        row = ctk.CTkFrame(parent, fg_color="transparent")
        row.pack(fill="x", padx=15, pady=7)
        text_frame = ctk.CTkFrame(row, fg_color="transparent")
        text_frame.pack(side="left", fill="x", expand=True)
        ctk.CTkLabel(
            text_frame, text=name, font=ctk.CTkFont(size=12, weight="bold"),
            text_color=TEXT
        ).pack(anchor="w")
        ctk.CTkLabel(
            text_frame, text=detail, font=ctk.CTkFont(size=10),
            text_color=MUTED
        ).pack(anchor="w")
        ctk.CTkLabel(
            row, text=amount, font=ctk.CTkFont(size=12, weight="bold"),
            text_color=color
        ).pack(side="right")

    # -------------------- ADD EXPENSE PAGE --------------------
    def build_add_expense(self):
        panel = ctk.CTkFrame(
            self.content, fg_color=WHITE, corner_radius=14,
            border_width=1, border_color=BORDER
        )
        panel.pack(fill="x", padx=5, pady=5)
        ctk.CTkLabel(
            panel, text="Record a new expense",
            font=ctk.CTkFont(size=19, weight="bold"), text_color=TEXT
        ).pack(anchor="w", padx=25, pady=(22, 5))
        ctk.CTkLabel(
            panel, text="Enter the details below to keep track of your spending.",
            font=ctk.CTkFont(size=12), text_color=MUTED
        ).pack(anchor="w", padx=25, pady=(0, 20))

        form = ctk.CTkFrame(panel, fg_color="transparent")
        form.pack(fill="x", padx=25, pady=(0, 20))
        form.grid_columnconfigure((0, 1), weight=1)

        self.amount_entry = self.form_field(form, "Amount (₹)", "e.g. 250", 0, 0)
        self.category_menu = self.form_dropdown(
            form, "Category", ["Food", "Transport", "Academics", "Shopping",
                               "Entertainment", "Snacks", "Social", "Others"], 0, 1
        )
        self.date_entry = self.form_field(form, "Date", "DD/MM/YYYY", 1, 0)
        self.description_entry = self.form_field(
            form, "Description", "What did you spend on?", 1, 1
        )

        ctk.CTkButton(
            panel, text="＋   Add Expense", height=43, width=180,
            fg_color=PRIMARY, hover_color="#10564F",
            font=ctk.CTkFont(size=13, weight="bold"),
            command=lambda: messagebox.showinfo(
                "GUI Preview", "The form is ready. Expense saving will be added later."
            )
        ).pack(anchor="w", padx=25, pady=(0, 25))

    def form_field(self, parent, label, placeholder, row, col):
        cell = ctk.CTkFrame(parent, fg_color="transparent")
        cell.grid(row=row, column=col, sticky="ew", padx=8, pady=10)
        ctk.CTkLabel(
            cell, text=label, font=ctk.CTkFont(size=12, weight="bold"),
            text_color=TEXT
        ).pack(anchor="w", pady=(0, 7))
        entry = ctk.CTkEntry(
            cell, placeholder_text=placeholder, height=40,
            corner_radius=8, border_color=BORDER
        )
        entry.pack(fill="x")
        return entry

    def form_dropdown(self, parent, label, values, row, col):
        cell = ctk.CTkFrame(parent, fg_color="transparent")
        cell.grid(row=row, column=col, sticky="ew", padx=8, pady=10)
        ctk.CTkLabel(
            cell, text=label, font=ctk.CTkFont(size=12, weight="bold"),
            text_color=TEXT
        ).pack(anchor="w", pady=(0, 7))
        menu = ctk.CTkOptionMenu(
            cell, values=values, height=40, fg_color="#F0F4F7",
            button_color=PRIMARY, button_hover_color="#10564F",
            text_color=TEXT, dropdown_fg_color=WHITE
        )
        menu.pack(fill="x")
        return menu

    # -------------------- TRANSACTIONS PAGE --------------------
    def build_transactions(self):
        toolbar = ctk.CTkFrame(self.content, fg_color="transparent")
        toolbar.pack(fill="x", pady=(0, 12))

        search = ctk.CTkEntry(
            toolbar, placeholder_text="Search transactions...",
            width=260, height=38
        )
        search.pack(side="left", padx=(0, 10))
        category = ctk.CTkOptionMenu(
            toolbar, values=["All Categories", "Food", "Transport",
                             "Academics", "Shopping", "Entertainment"],
            height=38, fg_color=WHITE, text_color=TEXT,
            button_color=PRIMARY
        )
        category.pack(side="left")
        ctk.CTkButton(
            toolbar, text="＋ Add Expense", width=135, height=38,
            fg_color=PRIMARY, command=lambda: self.show_page("Add Expense")
        ).pack(side="right")

        table_frame = ctk.CTkFrame(
            self.content, fg_color=WHITE, corner_radius=12,
            border_width=1, border_color=BORDER
        )
        table_frame.pack(fill="both", expand=True)

        columns = ("date", "description", "category", "amount")
        tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        headings = [
            ("date", "DATE", 130), ("description", "DESCRIPTION", 300),
            ("category", "CATEGORY", 180), ("amount", "AMOUNT", 130)
        ]
        for col, heading, width in headings:
            tree.heading(col, text=heading)
            tree.column(col, width=width, anchor="w")
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview", rowheight=38, background=WHITE,
            fieldbackground=WHITE, foreground=TEXT, font=("Arial", 10)
        )
        style.configure(
            "Treeview.Heading", background="#EDF2F6",
            foreground=TEXT, font=("Arial", 9, "bold"), relief="flat"
        )
        style.map("Treeview", background=[("selected", "#DDEFEA")])
        tree.pack(fill="both", expand=True, padx=15, pady=15)

        samples = [
            ("03/11/2026", "Lunch at cafeteria", "Food", "₹180"),
            ("02/11/2026", "Monthly bus pass", "Transport", "₹500"),
            ("01/11/2026", "Notebook and pens", "Academics", "₹120"),
            ("30/10/2026", "Movie ticket", "Entertainment", "₹250"),
            ("29/10/2026", "College snacks", "Snacks", "₹90"),
            ("28/10/2026", "T-shirt", "Shopping", "₹650"),
            ("27/10/2026", "Group outing", "Social", "₹300"),
        ]
        for item in samples:
            tree.insert("", "end", values=item)

    # -------------------- ANALYTICS PAGE --------------------
    def build_analytics(self):
        ctk.CTkLabel(
            self.content, text="Understand where your money goes.",
            font=ctk.CTkFont(size=13), text_color=MUTED
        ).pack(anchor="w", pady=(0, 15))

        top = ctk.CTkFrame(self.content, fg_color="transparent")
        top.pack(fill="x", pady=(0, 15))
        self.card(top, "TOTAL SPENT", "₹3,250", "Selected month", RED)
        self.card(top, "HIGHEST CATEGORY", "Food", "₹1,200 spent", PRIMARY)
        self.card(top, "DAILY AVERAGE", "₹108", "Per day", "#4776A8")

        chart_panel = ctk.CTkFrame(
            self.content, fg_color=WHITE, corner_radius=14,
            border_width=1, border_color=BORDER
        )
        chart_panel.pack(fill="both", expand=True)
        ctk.CTkLabel(
            chart_panel, text="Monthly Spending Breakdown",
            font=ctk.CTkFont(size=16, weight="bold"), text_color=TEXT
        ).pack(anchor="w", padx=20, pady=(17, 0))
        self.draw_pie_chart(chart_panel)

        ctk.CTkLabel(
            self.content,
            text="Sample analytics preview — calculations will be connected later.",
            font=ctk.CTkFont(size=10), text_color=MUTED
        ).pack(anchor="w", pady=(8, 0))



if __name__ == "__main__":
    app = SpendWiseApp()
    app.mainloop()
