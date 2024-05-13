from seatable_api import Base, context
from seatable_api.constants import UPDATE_DTABLE


server_url = context.server_url or "https://table.nju.edu.cn"
api_token = context.api_token or "caf934f72e577afa78fa03bd3dd8d4ffc8137486"


base = Base(api_token, server_url)
base.auth()
ans = base.query("SELECT * FROM Table1")
print(ans)
