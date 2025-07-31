Here’s a full `README.md` file you can use for your GitHub repository, which explains how to fix time sync on Linux when NTP ports are blocked by your ISP using a public HTTP API (like TimeZoneDB):

---

# 📡 NTP Fix on Linux When ISP Blocks Time Sync Ports

When your ISP blocks NTP (UDP port 123), your system clock may not synchronize automatically, leading to incorrect timestamps in logs, cron jobs, or SSL errors. This guide shows how to automatically set system time at boot using an HTTP-based API like [TimeZoneDB](https://timezonedb.com/api).

> ✅ Works on Raspberry Pi and most Debian/Ubuntu-based systems
> ⚠️ Does **not** require NTP port 123 (uses HTTP over port 80)

---

## 🔧 What This Project Does

* Checks internet availability
* Queries the correct time via the TimeZoneDB API
* Sets the system time using `timedatectl` (if allowed)
* Automatically runs on boot using `systemd`

---

## 📁 Folder Structure

```
ntp-fix/
├── get_time_on_boot.py     # Python script to sync time
└── set-ntp-fix.service     # systemd service definition
```

---

## ✅ Prerequisites

* Linux system with Python 3
* API key from [https://timezonedb.com/register](https://timezonedb.com/register)
* Root privileges

---

## 📥 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/gayan-tharuka/Time-Sync-Fix-for-Linux-When-NTP-Is-Blocked.git
cd ntp-fix
```

2. **Edit the Python script with your API key:**

```bash
nano get_time_on_boot.py
```

Replace this line:

```python
api_key = "YOUR_API_KEY"
```

with your actual API key.

3. **Make script executable:**

```bash
chmod +x get_time_on_boot.py
```

---

## 🛠️ Set Up systemd Service

1. **Copy the service file:**

```bash
sudo cp set-ntp-fix.service /etc/systemd/system/
```

2. **Reload systemd and enable the service:**

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable set-ntp-fix.service
```

3. **(Optional) Test the service immediately:**

```bash
sudo systemctl start set-ntp-fix.service
```

4. **Check log output:**

```bash
journalctl -u set-ntp-fix.service -b
```

---

## 🔄 What Happens on Boot

* The script waits for internet access
* Calls TimeZoneDB HTTP API
* Extracts current time
* Sets system clock via `timedatectl` or `date`
* Exits after successful sync

---

## 🧪 Verify Time

Check your time with:

```bash
timedatectl
```

Look for:

```text
System clock synchronized: yes
```

If RTC (hardware clock) is supported, you can also sync it:

```bash
sudo hwclock --systohc
```

---

## 🔐 Note on Security

* Your API key is used in a secure HTTP request and not exposed in logs.
* The script is read-only except for the `date` or `timedatectl` call.

---

## 📜 License

MIT License

---

## 🌐 Acknowledgements

* [TimeZoneDB](https://timezonedb.com/)
* Linux `timedatectl` and `systemd` community
* Raspberry Pi Foundation

---

Let me know if you'd like the GitHub repo files (`get_time_on_boot.py`, `set-ntp-fix.service`) bundled and zipped.
