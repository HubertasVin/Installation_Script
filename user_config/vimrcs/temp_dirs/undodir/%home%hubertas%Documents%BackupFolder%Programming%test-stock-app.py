Vim�UnDo� ƙǝfhw�{<އ~�`P�`��i"?�{g�s�   9   z        net_income_data = ticker.quarterly_earnings[['Net Income']] if 'Net Income' in ticker.quarterly_earnings else None      !      	       	   	   	    f��    _�                             ����                                                                                                                                                                                                                                                                                                                                                             f��    �                   �               5��                    !                       1      5�_�                            ����                                                                                                                                                                                                                                                                                                                                       "           V        f��    �                   �               �              "   import pandas as pd   import matplotlib.pyplot as plt   import yfinance as yf       H# Example manual earnings data (substitute with your actual data source)   %manual_earnings_data = pd.DataFrame({   E    'Date': ['2023-01-15', '2023-04-15', '2023-07-15', '2023-10-15'],   K    'Earnings': [1.5e9, 1.6e9, 1.7e9, 1.8e9]  # Example earnings in dollars   })   Kmanual_earnings_data['Date'] = pd.to_datetime(manual_earnings_data['Date'])       # Fetch stock data   stock_symbol = 'AAPL'   time_period = "1y"   Istock_data = yf.download(stock_symbol, period=time_period, interval="1d")       fig, ax1 = plt.subplots()       # Plot stock closing prices   Qax1.plot(stock_data.index, stock_data['Close'], label='Closing Price', color='g')   *ax1.set_ylabel('Closing Price', color='g')       .# Create a second y-axis for the earnings data   ax2 = ax1.twinx()   `ax2.plot(manual_earnings_data['Date'], manual_earnings_data['Earnings'], 'ro', label='Earnings')   %ax2.set_ylabel('Earnings', color='r')       # Titles and grid   >ax1.set_title(f"{stock_symbol} - Closing Prices and Earnings")   ax1.grid(True)   #ax1.figure.legend(loc='upper left')       
plt.show()    5��            "                      1             �                    @                       �      5�_�                           ����                                                                                                                                                                                                                                                                                                                                       A           V        f��     �                   �               �              A   import tkinter as tk    from tkinter import simpledialog   import yfinance as yf   import matplotlib.pyplot as plt   )from matplotlib.ticker import MaxNLocator   ?from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg   import pandas as pd       *# Function to fetch earnings data and plot   &def show_earnings_graph(stock_symbol):       global graph_window   $    ticker = yf.Ticker(stock_symbol)       try:   '        # Fetch quarterly earnings data   1        earnings_data = ticker.quarterly_earnings   ?        print("Earnings Data:", earnings_data)  # For debugging       except Exception as e:   3        print(f"Error fetching earnings data: {e}")           earnings_data = None       =    if earnings_data is not None and not earnings_data.empty:   (        graph_window = tk.Toplevel(root)   ?        graph_window.title(f"Earnings Data for {stock_symbol}")   (        graph_window.geometry("800x800")                fig, ax = plt.subplots()   o        ax.plot(earnings_data.index, earnings_data['Earnings'], 'ro-')  # 'ro-' for red dots connected by lines   <        ax.set_title(f"{stock_symbol} - Quarterly Earnings")   !        ax.set_ylabel('Earnings')           ax.grid(True)   b        ax.xaxis.set_major_locator(MaxNLocator(integer=True))  # Ensure integer locator for x-axis       <        canvas = FigureCanvasTkAgg(fig, master=graph_window)           canvas.draw()   %        canvas.get_tk_widget().pack()   	    else:   B        tk.messagebox.showinfo("Error", "No earnings data found.")       =# Function to prompt for stock symbol and show earnings graph   %def prompt_and_show_earnings_graph():   5    # Request user input for the company stock symbol   b    stock_symbol = simpledialog.askstring("Input", "Enter the company stock symbol:", parent=root)       if stock_symbol:   )        show_earnings_graph(stock_symbol)       +# Cleanup function to ensure proper closure   def on_closing():   #    if 'graph_window' in globals():           graph_window.destroy()       root.destroy()       # Create the main window   root = tk.Tk()   "root.title("Earnings Data Viewer")       (# Button to prompt user for stock symbol   bprompt_button = tk.Button(root, text="Enter Stock Symbol", command=prompt_and_show_earnings_graph)   prompt_button.pack(pady=20)       =# Bind the cleanup function to the main window's close button   -root.protocol("WM_DELETE_WINDOW", on_closing)       # Start the GUI event loop   root.mainloop()    5��            A                      �             �                    /                       �      5�_�                    
        ����                                                                                                                                                                                                                                                                                                                                                  V        f��    �                        �   	      0          5��    	                                           �                          �                     5�_�                            ����                                                                                                                                                                                                                                                                                                                                       0           V        f�      �                   �               �              0   import tkinter as tk   ,from tkinter import simpledialog, messagebox   import yfinance as yf   import matplotlib.pyplot as plt   ?from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg       &def show_earnings_graph(stock_symbol):       global graph_window   $    ticker = yf.Ticker(stock_symbol)           try:   C        # Placeholder for the correct method to fetch earnings data   ]        # Replace 'correct_method_to_fetch_earnings' with the actual method or attribute name   Q        earnings_data = getattr(ticker, 'correct_method_to_fetch_earnings', None)   8        if earnings_data is None or earnings_data.empty:   ;            raise ValueError("No earnings data available.")       (        graph_window = tk.Toplevel(root)   ?        graph_window.title(f"Earnings Data for {stock_symbol}")   (        graph_window.geometry("800x600")                fig, ax = plt.subplots()   H        # Assuming 'earnings_data' is a DataFrame with 'Earnings' column   F        ax.plot(earnings_data.index, earnings_data['Earnings'], 'ro-')   <        ax.set_title(f"{stock_symbol} - Quarterly Earnings")   !        ax.set_ylabel('Earnings')           ax.grid(True)       <        canvas = FigureCanvasTkAgg(fig, master=graph_window)           canvas.draw()   %        canvas.get_tk_widget().pack()           except Exception as e:   L        messagebox.showerror("Error", f"Failed to fetch earnings data: {e}")       %def prompt_and_show_earnings_graph():   b    stock_symbol = simpledialog.askstring("Input", "Enter the company stock symbol:", parent=root)       if stock_symbol:   )        show_earnings_graph(stock_symbol)       root = tk.Tk()   "root.title("Earnings Data Viewer")       bprompt_button = tk.Button(root, text="Enter Stock Symbol", command=prompt_and_show_earnings_graph)   prompt_button.pack(pady=20)       root.mainloop()    5��            0                      �             �                    8                       �      5�_�      	              
        ����                                                                                                                                                                                                                                                                                                                                                  V        f�!    �   	      9          5��    	                                           5�_�                  	      !    ����                                                                                                                                                                                                                                                                                                                                                             f��    �         9      z        net_income_data = ticker.quarterly_earnings[['Net Income']] if 'Net Income' in ticker.quarterly_earnings else None5��       !       Y          �      Y              �       +                 �                    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        f�O     �       B           �              �              5   import tkinter as tk   ,from tkinter import simpledialog, messagebox   import yfinance as yf   import matplotlib.pyplot as plt   )from matplotlib.ticker import MaxNLocator   ?from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg       2# Revised function to fetch earnings data and plot   &def show_earnings_graph(stock_symbol):       global graph_window   $    ticker = yf.Ticker(stock_symbol)              try:   .        # Attempt to fetch earnings data again   '        earnings_data = ticker.earnings           if earnings_data.empty:   ;            raise ValueError("No earnings data available.")   ?        print("Earnings Data:", earnings_data)  # For debugging              E        # Create a new window for the graph if earnings data is found   (        graph_window = tk.Toplevel(root)   ?        graph_window.title(f"Earnings Data for {stock_symbol}")   (        graph_window.geometry("800x600")                fig, ax = plt.subplots()   j        ax.plot(earnings_data.index, earnings_data['Earnings'], 'ro-')  # Plotting with red dots and lines   <        ax.set_title(f"{stock_symbol} - Quarterly Earnings")            ax.set_xlabel('Quarter')   !        ax.set_ylabel('Earnings')           ax.grid(True)       h        canvas = FigureCanvasTkAgg(fig, master=graph_window)  # Embedding the plot in the tkinter window           canvas.draw()   %        canvas.get_tk_widget().pack()           except Exception as e:   L        messagebox.showerror("Error", f"Failed to fetch earnings data: {e}")       =# Function to prompt for stock symbol and show earnings graph   %def prompt_and_show_earnings_graph():   b    stock_symbol = simpledialog.askstring("Input", "Enter the company stock symbol:", parent=root)       if stock_symbol:   )        show_earnings_graph(stock_symbol)       # Main application window setup   root = tk.Tk()   "root.title("Earnings Data Viewer")       bprompt_button = tk.Button(root, text="Enter Stock Symbol", command=prompt_and_show_earnings_graph)   prompt_button.pack(pady=20)       root.mainloop()    5��            A                      �             �                    4                       y      5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             f�R    �         5       �                 5��                          z                     �                          w                     5��