from modules.rpc import poll

if __name__ == "__main__":
    try:
        poll()
    except KeyboardInterrupt:
        print("Got sigterm, shutting down...")
