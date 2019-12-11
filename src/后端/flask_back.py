from flask import Flask, abort, request, jsonify
from client.contractnote import ContractNote
from client.bcosclient import BcosClient
import os
from eth_utils import to_checksum_address
from client.datatype_parser import DatatypeParser
from client.common.compiler import Compiler
from client.bcoserror import BcosException, BcosError
from client_config import client_config
import datetime
import time

app = Flask(__name__)
client = BcosClient()
# 从文件加载abi定义
'''
if os.path.isfile(client_config.solc_path) or os.path.isfile(client_config.solcjs_path):
    Compiler.compile_file("contracts/Test.sol")
'''
abi_file = "contracts/Test.abi"
data_parser = DatatypeParser()
data_parser.load_abi_file(abi_file)
contract_abi = data_parser.contract_abi
# 每次启动服务器部署合约
print("\n>>Deploy:----------------------------------------------------------")
with open("contracts/Test.bin", 'r') as load_f:
    contract_bin = load_f.read()
    load_f.close()
result = client.deploy(contract_bin)
#print("deploy", result)
print("new address : ", result["contractAddress"])

def callFunction(funcName,args):
    receipt=client.sendRawTransactionGetReceipt(result['contractAddress'],contract_abi,funcName,args)
    print("receipt:",receipt)
    # 解析receipt里的log
    print("\n>>parse receipt and transaction:--------------------------------------")
    txhash = receipt['transactionHash']
    print("transaction hash: ", txhash)
    logresult = data_parser.parse_event_logs(receipt["logs"])
    i = 0
    for log in logresult:
        if 'eventname' in log:
            i = i + 1
            print("{}): log name: {} , data: {}".format(i, log['eventname'], log['eventdata']))
    # 获取对应的交易数据，解析出调用方法名和参数
    txresponse = client.getTransactionByHash(txhash)
    inputresult = data_parser.parse_transaction_input(txresponse['input'])
    print("transaction input parse:", txhash)
    print(inputresult)
    # 解析该交易在receipt里输出的output,即交易调用的方法的return值
    outputresult = data_parser.parse_receipt_output(inputresult['name'], receipt['output'])
    print("receipt output :", outputresult)    


@app.route('/func1/', methods=['POST'])
def func1():
    if not request.form:
        abort(400)
    for key in request.form:
        print(key)
        print(request.form[key])
    payDate=request.form['payDate']+' 00:00:00'
    timeArray=time.strptime(payDate,"%Y-%m-%d %H:%M:%S")
    timeStamp=int(time.mktime(timeArray))*1000
    print(timeStamp)
    args=[request.form['lender'],request.form['borrower'],int(request.form['amount']),timeStamp]
    callFunction("AccountReceivableCreate",args)
    return jsonify({'result': 'success'})

@app.route('/func2/', methods=['POST'])
def func2():
    if not request.form:
        abort(400)
    for key in request.form:
        print(key)
        print(request.form[key])
    payDate=request.form['payDate']+' 00:00:00'
    timeArray=time.strptime(payDate,"%Y-%m-%d %H:%M:%S")
    timeStamp=int(time.mktime(timeArray))*1000
    print(timeStamp)
    args=[int(request.form['receiptID']),request.form['lender'],request.form['borrower'],int(request.form['amount']),timeStamp]
    callFunction("AccountReceivableTransfer",args)
    return jsonify({'result': 'success'})

@app.route('/func3/', methods=['POST'])
def func3():
    if not request.form:
        abort(400)
    for key in request.form:
        print(key)
        print(request.form[key])
    args=[int(request.form['receiptID'])]
    callFunction("AccountReceivableFinancing",args)
    return jsonify({'result': 'success'})

@app.route('/func4/', methods=['POST'])
def func4():
    if not request.form:
        abort(400)
    for key in request.form:
        print(key)
        print(request.form[key])
    args=[int(request.form['receiptID'])]
    callFunction("AccountReceivablePay",args)
    return jsonify({'result': 'success'})

@app.route('/getNodeInfo/', methods=['GET'])
def getNodeInfo():
    info=client.getinfo()
    print(info)
    return jsonify(info) if info else jsonify({'result': 'not found'})


if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(host="10.0.2.15", port=8000, debug=True,use_reloader=False)
