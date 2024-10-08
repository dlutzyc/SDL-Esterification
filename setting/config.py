# -*-coding: UTF-8 -*-
# Type"copyright", "credits" or "license()"
# encoding='utf-8'
# for more information.

"""
乙酸正丁酯合成方案

编辑日志
zinc 2024.6.19 基础编辑
"""

LOG_SETTING = {
	"APPLICATION_NAME": "MPT",
}

# 药品名一览表："C2H4O2":乙酸  "C4H10O":正丁醇 # # 硬件一览表：flask_1 flask_2 ph(COM40) con1 pdu_1 cycle_test

# 液体传输单元的路径图和连接通道设定
LIQUID_TRANSFER_PATH_GRAPH = {
	1: { # 第一层key是单元地址， 第二层key是连接的单元地址，其值是单元连接时的通道
		2: 3
	},
	2: {
		1: 7,   
	},

}

# 液体传输的基础设定
LIQUID_TRANSFER_BASE_SETTING = {
	"unit_num": 2, # 传输单元数量
	"waste_location": 8, # 废液通道
	"waste_line_volume": 10, # 废液管路的体积 单位 ml
}

# 泵设置
PUMP_SETTING = {
	"port": "/dev/com_485_0102", # 泵的串口号
	"syringe_dia": 14.567, # 进样器直径 单位mm
	"syringe_volume_max": 10, # 进样器最大容量 单位ml
	"pump_type": 'neodawn_2on1' # 泵阀类型
}

# 阀门设置
VALVE_SETTING = {
	"port": "COM34", # 阀门的串口号
	"location_max": 8, # 最大的通道编号
}

# 化学药品节点设置
CHEMICAL_LIST = {
	"C2H4O2": { # 乙酸
		"volume": 200,
		"address": 1,
		"location": 1,
	},
	"CH4O": { # 甲醇
		"volume": 200,
		"address": 1,
		"location": 5,
	},
	"C4H10O": { # 正丁醇
		"volume": 200,
		"address": 1,
		"location": 6,
	}
}

# 反应烧瓶设置
FLASK_LIST = {
	"flask_1": { # 1号瓶 反应模块 三口烧瓶 带夹套
		"volume": 100,
		"input_address": 1,
		"input_location": 4,
		"output_address": 2,
		"output_location": 6,
	},
	"flask_2": { # 2号瓶 稀释模块
		"volume": 100,
		"input_address": 1,
		"input_location": 7,
		"output_address": 2,
		"output_location": 5,
	},
	"flask_3": { # 收集瓶
		"volume": 100,
		"input_address": 2,
		"input_location": 4,
		"output_address": 2,
		"output_location": 2 
	},
	"flask_4": { # 液相
		"volume": 100,
		"input_address": 1,
		"input_location": 2,
		"output_address": 2,
		"output_location": 2
	},
}
# 磁力搅拌设置
STIR_LIST = {

}
# 顶置搅拌设置
OVER_HEAD_STIR_LIST = {
	"stir_1": { # 磁力搅拌名字 反应模块
		"port": "/dev/com_232_0201", # 串口号
		"stir_max": 2200, # 最大搅拌速度
	},
	"stir_2": { # 磁力搅拌名字 干燥模块
		"port": "/dev/com_232_0102", # 串口号
		"stir_max": 2200, # 最大搅拌速度
	},

}
# 旋蒸设置
ROTARY_EVAPORATION_LIST = {
	# "xuanzheng": {
	# 	"port": "/dev/ttyUSB13",
	# }
}

# PH计设置
PH_SENSOR_LIST = {
	# "ph": {
	# 	"port": "COM40"
	# }
}

# 电导设置
CONDUCTIVITY_SENSOR_LIST = {
	"con1": {
		"port": "/dev/com_232_0101"
	},
}

# PDU设置
PDU_LIST = {
	"pdu_1": {
		"port": "/dev/com_485_0202",
		"count": 4
	}
}

# 循環泵
CYCLE_PUMP_LIST = {
	'cycle_test': {
		"port": "/dev/com_232_0103",
		"type": "NEODAWN"
	}
}

# 日志等级 开发者选项 不要删除/更改
LOG_LEVEL = {
	'level': 'develop' # develop或production
}