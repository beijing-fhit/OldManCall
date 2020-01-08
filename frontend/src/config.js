var apiHost = 'https://ucallfree-tecent.ucallclub.com'
var service = {
  apiHost,
  wxConfig: `https://agency.ucallclub.com/Common/JsApiConfig`,
  getOpenId: `/getopenid`,
  verifyQrCodeActive: `${apiHost}/api/v2/active`,
  weChatState: `${apiHost}/api/v1/wechatstate`, // 请求用户状态
  verifyCode: `${apiHost}/api/v1/verifycode`, // 根据电话号码获取验证码
  verify: `${apiHost}/api/v4/VerifyCodeOnly` // 根据手机号和验证码验证
}
export {
  service
}
