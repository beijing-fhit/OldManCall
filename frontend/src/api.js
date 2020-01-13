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
// 激活二维码
const activateQrCode = (openId, qrcodeid, ucallfreeid) => {
  return post(service.verifyQrCodeActive, {
    qrcodeid: qrcodeid,
    ucallfreeid: ucallfreeid
  }, getHeader(openId))
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

const getInfo = (qrCodeId) => {
  return get(service.qrCodeInfo, {qrcodeid: qrCodeId})
}
/**
 * 保存老人信息
 * @param qrCodeId 二维码id
 * @param oldManInfo 老人信息，类型：{}
 * @param phone_number 联系人，类型：[]
 */
const saveInfo = (qrCodeId, oldManInfo, phoneNnumber) => {
  return post(service.qrCodeInfo, {
    qr_code_id: qrCodeId,
    old_man_info: oldManInfo,
    phone_number: phoneNnumber
  })
}
const weChatCalling = (openId, phoneNumbers, qrcodeid) => {
  var serviceNo = ''
  for (var i = 0; i < phoneNumbers.length; i++) {
    serviceNo += phoneNumbers[i] + '`'
  }
  serviceNo = serviceNo.substr(0, serviceNo.length - 1)
  console.log('serviceno:', serviceNo)
  return post(service.weChatCalling, {
    Enterpriseid: service.enterpriseid,
    YhServiceno: service.yhServiceno,
    Callmode: 1,
    Servicetype: 1,
    Serviceno: serviceNo,
    Display: 1,
    Eqrcode: qrcodeid
  }, getHeader(openId))
}
export default {
  wxConfig,
  getOpenId,
  weChatState,
  verifyQrCodeActive,
  activateQrCode,
  getVerifyCode,
  verifyNumber,
  getInfo,
  saveInfo,
  weChatCalling
}
