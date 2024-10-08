# -*-coding: UTF-8 -*-

# Type"copyright", "credits" or "license()"
# encoding='utf-8'
# for more information.

"""
乙酸正丁酯合成方案

编辑日志
zinc 2024.6.19 基础编辑
"""
# 药品名一览表："C2H4O2":乙酸  "C4H10O":正丁醇# 硬件一览表：flask_1 flask_2 ph(COM40) con1 pdu_1 cycle_test
MODULE_LIST = {
	"initialize": {
		"actions": {
			"chemical_initialize": [
				{"operation": "MOVE_CHEMICAL_TO_WASTE", "action_name": "119", "chemical": "C2H4O2", "waste_address": 0,
				'volume': 1, 'pull_rate': 60, 'push_rate': 60},
				# # # 乙酸充满管道；
				{"operation": "MOVE_CHEMICAL_TO_WASTE", "action_name": "118", "chemical": "C4H10O", "waste_address": 0,
				'volume': 1, 'pull_rate': 60, 'push_rate': 60},
				# # 正丁醇充满管道；
			],
			"instrument_unitialize": [
				{"operation": "INSTRUMENT_PDU", "action_name": "116", "name": "pdu_1", "address": 1, "power": False},
				# # 关闭PDU 1号插口；
				{"operation": "INSTRUMENT_CYCLE_PUMP", "name": "cycle_test", "temp": 75, "heat": True, "cycle": True},
				# # 打开循环泵液路循环；
				{"operation": "INSTRUMENT_PDU", "action_name": "115", "name": "pdu_1", "address": 1, "power": True, },
				{"operation": "WAIT_TIME", "start_mark_time": "115", "mark_time": "115", 'time': 10},
				{"operation": "INSTRUMENT_PDU", "action_name": "114", "name": "pdu_1", "address": 1, "power": False},
				# # 抽滤泵初始化；
				{"operation": "INSTRUMENT_OVER_HEAD_STIR", "action_name": "113", "name": "stir_1", "stir": 200,
				"stir_on": True, },
				{"operation": "WAIT_TIME", "start_mark_time": "114", "mark_time": "114", 'time': 5},
				{"operation": "INSTRUMENT_OVER_HEAD_STIR", "action_name": "112", "name": "stir_2", "stir": 200,
				"stir_on": True},
				{"operation": "WAIT_TIME", "start_mark_time": "113", "mark_time": "113", 'time': 10},
				{"operation": "INSTRUMENT_OVER_HEAD_STIR", "action_name": "111", "name": "stir_1", "stir": 200,
				"stir_on": False},
				{"operation": "INSTRUMENT_OVER_HEAD_STIR", "action_name": "110", "name": "stir_2", "stir": 200,
				"stir_on": False},
				# 搅拌初始化；
			],
		},
    },
	"main": {
		"actions": {
			"mainworka": [ # # 反应；
                {"operation": "INSTRUMENT_CYCLE_PUMP", "name": "cycle_test", "temp": 80, "heat": True, "cycle": False},
                # # # 加热为80℃
                {"operation": "INSTRUMENT_CYCLE_PUMP", "name": "cycle_test", "temp": 80, "heat": True, "cycle": True},
                # # # 开循环
                {"operation": "WAIT_TIME", 'start_mark_time': 'Wait_for_heating', 'mark_time': 'Wait_for_heating', 'time': 10},
                # # # 等待加热
                
				{"operation": "MOVE_CHEMICAL_TO_FLASK", "chemical": "C2H4O2", "flask": 'flask_1', 'volume':10,
				'pull_rate': 85, 'push_rate': 85, 'over_air': 1, 'over_air_volume': 5, "backend": False},
				# # # # 加入乙酸
                {"operation": "MOVE_CHEMICAL_TO_FLASK", "chemical": "C4H10O", "flask": 'flask_1', 'volume':10,
				'pull_rate': 85, 'push_rate': 85, 'over_air': 1, 'over_air_volume': 5, "backend": False},
				# # # # 加入正丁醇
				{"operation": "INSTRUMENT_OVER_HEAD_STIR", "name": "stir_1", "stir": 200, "stir_on": True,
				"backend": False},
				# # # 开1号搅拌
               
                # # # 开始反应
				{"operation": "WAIT_TIME", "start_mark_time": "Wait_for_reaction", 'mark_time': 'Wait_for_reaction',
				'time': 180},
				# # 等待反应完成 
				{"operation": "INSTRUMENT_CYCLE_PUMP", "name": "cycle_test", "temp": 25, "heat": False, "cycle": True},
				# 关闭循环泵加热 保持循环以逐渐降温
				{"operation": "WAIT_TIME", "start_mark_time": "Wait_for_cooling", 'mark_time': 'Wait_for_cooling',
				'time': 180},
				# 等待冷却
				{"operation": "INSTRUMENT_OVER_HEAD_STIR", "name": "stir_1", "stir": 200, "stir_on": False,
				"backend": False},
				# 关1号搅拌
			],
            "mainworkb": [  # 取出样品至稀释模块
                # {"operation": "INSTRUMENT_PDU", "name": "pdu_1", "address": 1, "power": True, "backend": False},
                # 打开继电器电源,抽滤 测试正常
                # {"operation": "WAIT_TIME", 'start_mark_time': 'power0', 'mark_time': 'power0', 'time': 10 * 60},
                # 等待抽滤
                # {"operation": "INSTRUMENT_PDU", "name": "pdu_1", "address": 1, "power": False, "backend": False},
                # # 关闭电源
                {"operation": "MOVE_FLASK_TO_WASTE", "action_name": "109", "flask": "flask_1", "waste_address": 0,
                 'volume': 2, 'pull_rate': 60, 'push_rate': 60, 'over_air': 1, 'over_air_volume': 10},
                {"operation": "MOVE_FLASK_TO_FLASK", "flask": 'flask_1', "dest_flask": "flask_2", 'volume': 1,
                 'pull_rate': 85,
                 'push_rate': 85, 'over_air': 1, 'over_air_volume': 10, "backend": False},
                # # 将产品移到稀释模块
                {"operation": "MOVE_CHEMICAL_TO_FLASK", "chemical": "CH4O", "flask": 'flask_2', 'volume': 49,
                 'pull_rate': 85, 'push_rate': 85, 'over_air': 1, 'over_air_volume': 5, "backend": False},
                # # 加甲醇
                # # # 开2号搅拌
                {"operation": "INSTRUMENT_OVER_HEAD_STIR", "name": "stir_2", "stir": 200, "stir_on": True,
                 "backend": False},
                {"operation": "WAIT_TIME", "start_mark_time": "Wait_for_reaction", 'mark_time': 'Wait_for_reaction',
                 'time': 60},
                {"operation": "INSTRUMENT_OVER_HEAD_STIR", "name": "stir_2", "stir": 200, "stir_on": False,
                 "backend": False},
                # 关2号搅拌

            ],
            "mainworkc": [  # 进样检测；
                {"operation": "MOVE_FLASK_TO_WASTE", "action_name": "109", "flask": "flask_2", "waste_address": 0,
                 'volume': 2, 'pull_rate': 60, 'push_rate': 60, 'over_air': 1, 'over_air_volume': 10},
                {"operation": "MOVE_FLASK_TO_FLASK", "flask": 'flask_2', "dest_flask": "flask_4", 'volume': 1,
                 'pull_rate': 30,
                 'push_rate': 30, 'over_air': 0, 'over_air_volume': 10, "backend": False},
                {"operation": "MOVE_FLASK_TO_WASTE", "action_name": "109", "flask": "flask_2", "waste_address": 0,
                 'volume': 100, 'pull_rate': 60, 'push_rate': 60, 'over_air': 1, 'over_air_volume': 10}
                # # 将产品移到稀释模块
            ],
            "mainwork": [  # 取出样品；
                # {"operation": "INSTRUMENT_PDU", "name": "pdu_1", "address": 1, "power": True, "backend": False},
                # 打开继电器电源,抽滤 测试正常
                # {"operation": "WAIT_TIME", 'start_mark_time': 'power0', 'mark_time': 'power0', 'time': 10 * 60},
                # 等待抽滤
                # {"operation": "INSTRUMENT_PDU", "name": "pdu_1", "address": 1, "power": False, "backend": False},
                # # 关闭电源
                {"operation": "MOVE_FLASK_TO_FLASK", "flask": 'flask_1', "dest_flask": "flask_3", 'volume': 40,
                 'pull_rate': 85,
                 'push_rate': 85, 'over_air': 1, 'over_air_volume': 10, "backend": False}

                # # 将产品移到收集瓶
            ],
        }
    },
    "clean": {
		"actions": {
			"worng_1": [
				{"operation": "INSTRUMENT_OVER_HEAD_STIR", "action_name": "101", "name": "stir_1", "stir": 200,
				"stir_on": True},
				{"operation": "INSTRUMENT_VALVE", "name": 1, "location": 1, "action_name": "valve_1", "backend": False},
				{"operation": "INSTRUMENT_PUMP", "name": 1, "volume": 5, "rate": 60, "mode": 1, "action_name": "A",
				"backend": False},
				{"operation": "INSTRUMENT_PUMP", "name": 1, "start": True, "backend": False},
				{"operation": "INSTRUMENT_VALVE", "name": 1, "location": 8, "action_name": "valve_1", "backend": False},
				{"operation": "INSTRUMENT_PUMP", "name": 1, "volume": 5, "rate": 0.77, "mode": 0,
				"action_name": "pump1_push", "backend": False},
				{"operation": "INSTRUMENT_PUMP", "name": 1, "start": True, "backend": False},
				{"operation": "INSTRUMENT_VALVE", "name": 1, "location": 3, "action_name": "valve_1", "backend": False},
				{"operation": "INSTRUMENT_PUMP", "name": 1, "volume": 10, "rate": 60, "mode": 1, "action_name": "A",
				"backend": False},
				{"operation": "INSTRUMENT_PUMP", "name": 1, "start": True, "backend": False},
				{"operation": "INSTRUMENT_VALVE", "name": 1, "location": 8, "action_name": "valve_1", "backend": False},
				{"operation": "INSTRUMENT_PUMP", "name": 1, "volume": 10, "rate": 35, "mode": 0,
				"action_name": "pump1_push", "backend": False},
				{"operation": "INSTRUMENT_PUMP", "action_name": "130", "name": 1, "start": True, "backend": False}
			],
            "clean_1": [
                # 之后为清洁
                {"operation": "INSTRUMENT_OVER_HEAD_STIR", "action_name": "72", "name": "stir_1", "stir": 200,
                "stir_on": True, "backend": False},
                # 开2号搅拌
                {"operation": "MOVE_CHEMICAL_TO_FLASK", "action_name": "73", "chemical": "C4H10O", "flask": 'flask_1',
                'volume': 7, 'pull_rate': 85, 'push_rate': 60, 'over_air': 1, 'over_air_volume': 5, "backend": False},
                 {"operation": "WAIT_TIME", 'start_mark_time': 'Wait_for_cleaning', 'mark_time': 'Wait_for_heating', 'time': 60},
                {"operation": "MOVE_FLASK_TO_FLASK", "action_name": "74", "flask": 'flask_1', "dest_flask":"flask_2",
                'volume': 7, 'pull_rate': 85, 'push_rate': 85, "backend": False},
                {"operation": "INSTRUMENT_OVER_HEAD_STIR", "action_name": "75", "name": "stir_1", "stir": 200,
                "stir_on": False, "backend": False},
                # 关2号搅拌
           ]
       }
    }
}