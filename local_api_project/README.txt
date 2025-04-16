
# 📁 Local API Project (Offline & Stdlib Only)

This project lets you build and test a full API flow locally on Ubuntu using **only Python standard libraries**. No external packages or internet required.

---

## 📂 Project Structure

```
local_api_project/
├── api_server.py         # API server (GET/POST support)
├── client.py             # Python client for testing API
├── index.html            # HTML interface using fetch()
├── data_store.json       # Auto-created JSON data store
└── README.txt            # You're here
```

---

## 🧑‍💻 How to Run

### 1. 🟢 Start the API Server
In your terminal:
```bash
python3 api_server.py
```

It will run on `http://localhost:8000`.

---

### 2. 🧪 Send/Fetch Data from Python
In another terminal:
```bash
python3 client.py
```
This sends a POST with test data, then fetches it with a GET.

---

### 3. 🌐 Test from Web Browser

#### Option A: Using Python's Web Server (Recommended)
```bash
python3 -m http.server 8080
```

Then visit:
```
http://localhost:8080/index.html
```

✅ This avoids browser restrictions with file:// URLs.

#### Option B: Open Directly in Browser

If you prefer:
1. Open Firefox from the **app menu** (not from terminal)
2. Press `Ctrl+O` and select `index.html`
3. OR use this URL in address bar:
```
file:///home/yourname/path/to/local_api_project/index.html
```

#### ⚠️ Firefox AppArmor/Wayland Issue
If you see a warning like:
```
Wayland Proxy bind() error : Permission denied
AppArmor prevents access...
```

That’s due to Firefox sandboxing on Ubuntu. To bypass:
```bash
firefox --no-sandbox index.html  # for testing only
```
But it's safer to use `python3 -m http.server`.

---

## ✅ What It Does

- `GET /api/data`: Returns saved JSON entries
- `POST /api/data`: Accepts JSON and saves to `data_store.json`
- HTML page sends POST via fetch() and displays response
- `client.py` lets you simulate both operations in the terminal

---

Happy hacking! 🎉 Offline APIs FTW.
