import {get, post} from './http'
import {service} from './config'

const wxConfig = () => {
  return get(service.wxConfig)
}
const getHeader = function (openId) {
  return {
    'content-type': 'application/json',
    'Authorization': 'Basic ' + openId
  }
}

const getOpenId = () => {
  console.log('api---getOpenId url:' + service.getOpenId)
  return get(service.getOpenId)
}
const weChatState = (openId, nickName = '', serviceno = '') => {
  return post(service.weChatState,
    {
      Nickname: nickName,
      serviceno: serviceno
    }
    , getHeader(openId))
}
const verifyQrCodeActive = (qrCodeId) => {
  return get(service.verifyQrCodeActive, {
    qrcodeid: qrCodeId
  })
}
// 根据手机号获取验证码
const getVerifyCode = (openId, number) => {
  return get(service.verifyCode, {
    tel: number
  }, getHeader(openId))
}
// 验证手机号是否合法
const verifyNumber = (openId, number, verifyNumber) => {
  return post(service.verify, {
    AuthCode: verifyNumber,
    Tel: number
  }, getHeader(openId))
}
// 保存老人信息
const saveInfo = () => {

}
export default {
  wxConfig, getOpenId, weChatState, verifyQrCodeActive, getVerifyCode, verifyNumber, saveInfo
}
