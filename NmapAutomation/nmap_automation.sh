#!/bin/bash

# nmap_automation.sh

echo "--- Script Otomatisasi Nmap Sederhana ---"

# Meminta input dari pengguna
read -p "Masukkan IP Target: " target

# Cek apakah input kosong
if [ -z "$target" ]; then
    echo "IP Target tidak boleh kosong. Keluar."
    exit 1
fi

echo -e "\n[+] Memulai Quick Scan pada $target..."
nmap $target -oN "quick_scan_${target}.txt"

echo -e "\n[+] Memulai Service Version Scan pada $target..."
nmap -sV $target -oN "version_scan_${target}.txt"

echo -e "\n[+] Memulai Default Script Scan pada $target..."
nmap -sC $target -oN "script_scan_${target}.txt"

echo -e "\n[+] Semua scan selesai. Hasil disimpan dalam file .txt"
