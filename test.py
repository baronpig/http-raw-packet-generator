from hrpgen import HRPG

hrpg = HRPG()
hrpg.set_url("http://google.co.kr/a.html")
hrpg.set_method("GET")
hrpg.set_headers({
	"user-agent": "hihi"
	})
hrpg.set_headers("content-type", "application/json")
hrpg.generate_raw_packet()