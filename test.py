from rrpacket import RRP

rrp = RRP()
rrp.set_url("http://google.co.kr/a.html")
rrp.set_method("GET")
rrp.set_headers({
	"user-agent": "hihi"
	})
rrp.set_headers("content-type", "application/json")
rrp.generate_raw_packet()