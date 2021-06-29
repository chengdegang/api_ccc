import os
import requests
import base64

def post_cloud(ip,url,protobufEncodingData,imageEncodingData):
    url = f'http://{ip}{url}'
    # 入参
    data = {
    "alg": {
        "protobufEncodingData": f"{protobufEncodingData}",
        "imageEncodingData": f"{imageEncodingData}"
    }
}
    req = requests.post(url, json=data)
    print(req.json())
    return req.json()

def protobufEncodingData_deal():
    1

"""
遍历指定路径下的所有图片，并转换成base64
"""
def imageEncodingData_deal(file):
    imagedirs = []
    base64_datas = []
    if os.path.exists(file) == False:
        print("该路径不存在")
    #查找路径下所有的jpg文件
    for root, dirs, files in os.walk(file):
        for f in files:
            if '.jpg' in f:
                # print(f)
                #打印文件路径
                # print(os.path.join(root, f))
                imagedirs.append(os.path.join(root, f))
    if len(imagedirs) == 0:
        print("当前路径下.jpg文件为0")

    # print(imagedirs)
    for i in range(len(imagedirs)):
        # print(i)
        with open(f'{imagedirs[i]}', "rb") as f:  # 转为二进制格式
            base64_data = str(base64.b64encode(f.read()))  # 使用base64进行加密
            base64_data = f'data:image/jpg;base64,{base64_data[2:]}'
            base64_datas.append(base64_data)
            # print(f'data:image/jpg;base64,{base64_data[2:]}')
    # print(base64_datas[2])
    return base64_datas

def image_change_base64():
    with open("/Users/jackrechard/PycharmProjects/api_ccc/image/2021-01-19-20-00-14_Suc.jpg", "rb") as f:  # 转为二进制格式
        base64_data = str(base64.b64encode(f.read()))  # 使用base64进行加密
        print(f'data:image/jpg;base64,{base64_data[2:]}')
        # file = open('base.txt', 'wt')  # 写成文本格式
        # file.write(str(base64_data))
        # file.close()

fileimage = 'image/'

if __name__ == '__main__':
    # get_api()
    # get_post()
    protobufEncodingData =['CNH30AkQwczLl/rvJxj///////////8BIlQKABABGQAAACDNv39AIQAAACDNv39AKQAAAODg6nNAMQAAAACXXWZAOQAAAAAAAAAAQQAAAAAAAAAASQAAAAAAAAAAUQAAAAAAAAAAWIAFYOgCaBAqVAoJdGVzdHNjZW5lEAEYACIbGQAAAAAAAPA/GQAAAAAAAABAGQAAAAAAAAhAKiQZAAAAAAAAAAAZAAAAAAAAAAAZAAAAAAAAAAAZAAAAAAAA8D8wGDCQAg==']
    imageEncodingData = imageEncodingData_deal(fileimage)
    result_suc = 0
    result_fail = 0

    post_cloud(ip='59.111.148.60:8087', url='/api/alg/cloud/aw/reloc/proxy?routeApp=wxc.f1f2',
                            protobufEncodingData=protobufEncodingData[0], imageEncodingData=imageEncodingData[0])

    # for i in range(len(imageEncodingData)):
    #     data1 = post_cloud(ip='59.111.148.60:8087', url='/api/alg/cloud/aw/reloc/proxy?routeApp=wxc.f1f2',
    #                        protobufEncodingData=protobufEncodingData[0], imageEncodingData=imageEncodingData[i])
    #     algcode = str(data1['result']['algCode'])
    #     if '1' in algcode:
    #         result_suc = result_suc + 1
    #     elif '16' in algcode:
    #         result_fail = result_fail + 1

    print('-----test data-----')
    print(f'总共 {len(imageEncodingData)} 张图片')
    print(f'成功的次数是:{result_suc}  失败的次数是:{result_fail}')

#     imageEncodingData_deal(fileimage)


