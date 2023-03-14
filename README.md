# sandbox_becu

Set up environment:

```
./scripts/start_app.sh
pip3 install requirements.txt
```

Install Azure CLI and download AzCopy

```
az login
```

Run the Program:

```bash
python3 malware_detonation/main.py
```

After the server starts, go to `127.0.0.1` and you see `{"Hello":"World"}` then it's successful.

## How to use the detonate API endpoint

1. Open the browser and go to `127.0.0.1/docs`
2. Try the detonate api
3. Copy the url of a file you want to test, for example: https://raw.githubusercontent.com/singerGUO/sandbox_becu/upload-blob/hello.sh
4. Click execute
5. Get the 200 OK response
6. Go to azure storage account to check if the new pcap file is uploaded
