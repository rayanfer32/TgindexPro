import os


def runSetup():
  def alert(missing="API_ID , API_HASH"):
    print(f"\nCopy your {missing} and save it into Secrets(Environment variables) Sidebar!\n")

  if os.environ["API_ID"] == "NA":
    alert()
    return

  if os.environ["SESSION_STRING"] == "NA":
    os.system("python3 app/generate_session_string.py")
    alert(missing = "SESSION_STRING")
    return

  os.system("python3 -m app")

if __name__ == '__main__':
  runSetup() 