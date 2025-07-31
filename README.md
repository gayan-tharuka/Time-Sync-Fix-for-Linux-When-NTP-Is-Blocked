# 🕒 Time Sync Fix for Linux (Raspberry Pi / Ubuntu) via API

If your ISP or network **blocks NTP ports (UDP 123)** and your Linux system can't sync time automatically — this tool is a workaround.

## ✅ What This Does

- Uses [TimeZoneDB API](https://timezonedb.com/api) to fetch current time.
- Sets system time using `date -s`.
- Automatically runs at boot using `systemd`.

## 🧰 Requirements

- Python 3
- Internet access (port 80)
- Free TimeZoneDB API key

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/time-sync-fix.git
cd time-sync-fix
