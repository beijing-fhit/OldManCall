var apiHost = 'https://ucallfree-tecent.ucallclub.com'
var service = {
  enterpriseid: 107,
  yhServiceno: '2010660101',
  apiHost,
  wxConfig: `https://agency.ucallclub.com/Common/JsApiConfig`,
  getOpenId: `/getopenid`,
  verifyQrCodeActive: `${apiHost}/api/v2/active`,
  weChatState: `${apiHost}/api/v1/wechatstate`, // 请求用户状态
  verifyCode: `${apiHost}/api/v1/verifycode`, // 根据电话号码获取验证码
  verify: `${apiHost}/api/v4/VerifyCodeOnly`, // 根据手机号和验证码验证
  qrCodeInfo: `/qr_code_info/`, // qrcode绑定的信息
  weChatCalling: `${apiHost}/api/v4/wechatcalling`
}
export {
  service
}
