from tkinter import *
import webview
import urllib.parse

class CampusNavigator:
    def __init__(self, master):
        self.master = master
        self.master.title("CampusNav")
        self.master.geometry("400x250")

        self.create_homepage()

    def create_homepage(self):
        # Homepage UI
        self.label = Label(self.master, text="Welcome to CampusNav", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.search_label = Label(self.master, text="Enter location:")
        self.search_label.pack(pady=5)

        self.search_entry = Entry(self.master, width=30)
        self.search_entry.pack(pady=5)

        self.search_button = Button(self.master, text="Search", command=self.search_location, padx=10, pady=5)
        self.search_button.pack(pady=10)

        self.enter_button = Button(self.master, text="Enter Map", command=self.open_webview, padx=10, pady=5)
        self.enter_button.pack(pady=5)

    def search_location(self):
        # Retrieve the entered location from the entry widget
        location = self.search_entry.get()

        if location:
            # Encode the location for the URL
            encoded_location = urllib.parse.quote(location)

            # Create a webview for OpenStreetMap with automatic zoom to the specified location
            map_url = f'https://www.openstreetmap.org/?query={encoded_location}'
            webview.create_window('CampusNav', map_url)

            # Start the webview event loop
            webview.start()
        else:
            # Show an error message if no location is entered
            messagebox.showerror("Error", "Please enter a location.")

    def open_webview(self):
        # Destroy the homepage UI
        self.label.destroy()
        self.search_label.destroy()
        self.search_entry.destroy()
        self.search_button.destroy()
        self.enter_button.destroy()

        # Create a webview for OpenStreetMap with automatic zoom to the specified location
        map_html = """
        <html>
        <head>
            <title>Campus Navigator</title>
            <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
            <style>
                #map { height: 400px; }
            </style>
        </head>
        <body>
            <div id="map"></div>
            <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
            <script>
                var map = L.map('map').setView([12.8231, 80.0425], 15);
                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    attribution: '© OpenStreetMap contributors'
                }).addTo(map);
                L.marker([12.8231, 80.0425]).addTo(map)
                    .bindPopup('SRM Institute of Science and Technology, Kattankulathur')
                    .openPopup();
            </script>
        </body>
        </html>
        """

        webview.create_window('CampusNav', html=map_html, width=800, height=600)

        # Start the webview event loop
        webview.start()

def main():
    root = Tk()
    root.title("CampusNav")
    app = CampusNavigator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
