var apiHost = 'https://ucallfree-tecent.ucallclub.com'
var service = {
  apiHost,
  wxConfig: `https://agency.ucallclub.com/Common/JsApiConfig`,
  getOpenId: `/getopenid`,
  verifyQrCodeActive: `${apiHost}/api/v2/active`,
  weChatState: `${apiHost}/api/v1/wechatstate` // 请求用户状态
}
export {
  service
}
