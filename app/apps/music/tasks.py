from celery import shared_task
import time
from ronglian_sms_sdk import SmsSDK

@shared_task
def add(x,y):
    time.sleep(3)

    return x+y

@shared_task
def send_message(mobile,msg,expires):
    accId = '8aaf07086d62068d016d73220d9b107a'  # 容联云通讯分配的主账号ID
    accToken = '0e37fbbc8c1f4fda88c11e145c139abd'  # 容联云通讯分配的主账号TOKEN
    appId = '8aaf07086d62068d016d73220dee1081'  # 容联云通讯分配的应用ID
    sdk = SmsSDK(accId, accToken, appId)
    tid = '1' #容联云通讯创建的模板
    # mobile = '15989502326'#手机号1,手机号2
    # msg="%06d" % random.randint(0,999999)
    datas = (msg,expires)
    sdk.sendMessage(tid, mobile, datas)

    return 'send msg successful'