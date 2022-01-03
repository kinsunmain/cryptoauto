import pyupbit

access = "CtwO7FFz2yF4AkIYZQApaRqAVMGjsEwV2DK93oT6"          # 본인 값으로 변경
secret = "OEk8JyAsC0N4xqIcqoxZyiZwDO0BnrNaLDl0B48a"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)   

print(upbit.get_balance("KRW-STRK"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회