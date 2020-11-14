SOURCE = r'N:\A1 - Projects'
ARCHIVE_DIRECTORY_NAME = "Archive"
DO_LOGGING = False

testDirectoryList = [
	"A1-18019",
	"A1-19017"
]

directoryList = [
	"A1-10033",
	"A1-10034",
	"A1-11004",
	"A1-11005",
	"A1-11020",
	"A1-11021",
	"A1-11022",
	"A1-11025",
	"A1-11030",
	"A1-11031",
	"A1-11067",
	"A1-12036",
	"A1-12075",
	"A1-12089",
	"A1-12094",
	"A1-12097",
	"A1-13006",
	"A1-13007",
	"A1-13008",
	"A1-13014",
	"A1-13026",
	"A1-13031",
	"A1-13033",
	"A1-13034",
	"A1-13035",
	"A1-13062",
	"A1-13063",
	"A1-13064",
	"A1-13065",
	"A1-13066",
	"A1-13070",
	"A1-13072",
	"A1-13073",
	"A1-13076",
	"A1-13077",
	"A1-13078",
	"A1-13079",
	"A1-13080",
	"A1-13081",
	"A1-13082",
	"A1-13083",
	"A1-13085",
	"A1-13086",
	"A1-13096",
	"A1-13097",
	"A1-13098",
	"A1-13099",
	"A1-13101",
	"A1-13103",
	"A1-13104",
	"A1-13106",
	"A1-13107",
	"A1-13110",
	"A1-13111",
	"A1-13112",
	"A1-13113",
	"A1-13114",
	"A1-13115",
	"A1-13116",
	"A1-13117",
	"A1-13118",
	"A1-13119",
	"A1-13120",
	"A1-13121",
	"A1-13122",
	"A1-13123",
	"A1-13124",
	"A1-13125",
	"A1-13126",
	"A1-13127",
	"A1-13128",
	"A1-13129",
	"A1-13130",
	"A1-14022",
	"A1-14025",
	"A1-14026",
	"A1-14027",
	"A1-14028",
	"A1-14037",
	"A1-14044",
	"A1-14067",
	"A1-14073",
	"A1-15011",
	"A1-15012",
	"A1-15013",
	"A1-15015",
	"A1-15021",
	"A1-15022",
	"A1-15023",
	"A1-15036",
	"A1-15049",
	"A1-15051",
	"A1-15052",
	"A1-15053",
	"A1-15056",
	"A1-15057",
	"A1-15062",
	"A1-15068",
	"A1-15069",
	"A1-15070",
	"A1-15085",
	"A1-15101",
	"A1-15102",
	"A1-15103",
	"A1-15104",
	"A1-15105",
	"A1-15106",
	"A1-15107",
	"A1-15108",
	"A1-15109",
	"A1-15110",
	"A1-15111",
	"A1-15112",
	"A1-15113",
	"A1-15114",
	"A1-15115",
	"A1-15116",
	"A1-15117",
	"A1-15118",
	"A1-15120",
	"A1-15128",
	"A1-15135",
	"A1-15141",
	"A1-15144",
	"A1-16007",
	"A1-16017",
	"A1-16022",
	"A1-16023",
	"A1-16025",
	"A1-16027",
	"A1-16029",
	"A1-16032",
	"A1-16035",
	"A1-16038",
	"A1-16040",
	"A1-16041",
	"A1-16042",
	"A1-16043",
	"A1-16044",
	"A1-16045",
	"A1-16046",
	"A1-16047",
	"A1-16050",
	"A1-16053",
	"A1-16054",
	"A1-16060",
	"A1-16061",
	"A1-16062",
	"A1-16066",
	"A1-16067",
	"A1-16069",
	"A1-16070",
	"A1-16071",
	"A1-16073",
	"A1-16083",
	"A1-16089",
	"A1-16092",
	"A1-16093",
	"A1-16094",
	"A1-16095",
	"A1-16100",
	"A1-17002",
	"A1-17003",
	"A1-17004",
	"A1-17010",
	"A1-17013",
	"A1-17015",
	"A1-17016",
	"A1-17017",
	"A1-17041",
	"A1-17043",
	"A1-17044",
	"A1-17049",
	"A1-17050",
	"A1-17058",
	"A1-17059",
	"A1-17062",
	"A1-17063",
	"A1-17064",
	"A1-17066",
	"A1-17075",
	"A1-17076",
	"A1-17078",
	"A1-17085",
	"A1-17086",
	"A1-17087",
	"A1-17090",
	"A1-17092",
	"A1-17093",
	"A1-17094",
	"A1-17095",
	"A1-17097",
	"A1-17103",
	"A1-18001",
	"A1-18006",
	"A1-18012",
	"A1-18018",
	"A1-18019",
	"A1-18023",
	"A1-18024",
	"A1-18025",
	"A1-18026",
	"A1-18027",
	"A1-18028",
	"A1-18031",
	"A1-18032",
	"A1-18035",
	"A1-18038",
	"A1-18041",
	"A1-18042",
	"A1-18043",
	"A1-18044",
	"A1-18045",
	"A1-18047",
	"A1-18048",
	"A1-18049",
	"A1-18050",
	"A1-18051",
	"A1-18052",
	"A1-18053",
	"A1-18054",
	"A1-18055",
	"A1-19002",
	"A1-19003",
	"A1-19004",
	"A1-19005",
	"A1-19006",
	"A1-19007",
	"A1-19008",
	"A1-19009",
	"A1-19010",
	"A1-19011",
	"A1-19015",
	"A1-19016",
	"A1-19017",
	"A1-19018",
	"A1-19020",
	"A1-19022",
	"A1-19023",
	"A1-19026",
	"A1-19027",
	"A1-19028",
	"A1-19029",
	"A1-19031",
	"A1-19032",
	"A1-19037",
	"A1-19038",
	"A1-19041",
	"A1-19045",
	"A1-19049",
	"A1-19051",
	"A1-19052",
	"A1-20001",
	"A1-20002",
	"A1-20005",
	"A1-20006",
	"A1-20008",
	"A1-20010"
]