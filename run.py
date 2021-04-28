import os

def runSetup():
  def alert(missing="API_ID , API_HASH"):
    print(f"\nCopy your {missing} and save it into Secrets(Environment variables) Sidebar!\n")

  api_id = os.getenv("API_ID")
  if api_id == None:
    alert()
    return

  session_string = os.getenv("SESSION_STRING")
  if session_string == None:
    os.system("python3 app/generate_session_string.py")
    alert(missing = "SESSION_STRING")
    return

  os.system("python3 -m app")

if __name__ == '__main__':
  runSetup() 