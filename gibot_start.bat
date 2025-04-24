@echo off
wsl -d Ubuntu-22.04 -- bash -c "cd ~ && source venv1/bin/activate && cd chatbot && python bot_v2.py"