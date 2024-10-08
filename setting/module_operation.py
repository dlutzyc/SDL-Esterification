#-*-coding: UTF-8 -*-

# Type"copyright", "credits" or "license()"
# encoding='utf-8'
# for more information.
MODULE_OPERATION_LIST = [
	# # # # 反应模块
	# {"module": "initialize", "action": "instrument_unitialize", "action_name": "instrument_unitialize", "backend": True},
	# # # # # # # # # 所有设备初始化；
	# {"module": "initialize", "action": "chemical_initialize", "action_name": "chemical_initialize", "backend": False},
	# {"operation": "INSTRUMENT_PDU", "action_name": "a14", "name": "pdu_1", "address": 1, "power": False, "backend": False},
	# # # # # # # # # 液路初始化；
	# {"operation": "WAIT_MODULE_ACTION", "action_name": "0", "wait_action": "instrument_unitialize", "backend": False},
	# # # # # 反应模块
	{"module": "main", "action": "mainworka", "action_name": "mainworka", "backend": False},
    {"module": "main", "action": "mainworkb", "action_name": "mainworkb", "backend": False},
    {"module": "main", "action": "mainworkc", "action_name": "mainworkc", "backend": False},
    {"module": "main", "action": "mainwork", "action_name": "mainwork", "backend": False},
	# 清洗
    {"module": "clean", "action": "clean_1", "action_name":"clean","backend": False},
    # 所有设备初始化；
	{"module": "initialize", "action": "instrument_unitialize","action_name": "instrument_over", "backend": True},
]