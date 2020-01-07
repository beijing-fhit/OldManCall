import {get, post, deletes, put} from './http'
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
export default {
  wxConfig, getOpenId, weChatState, verifyQrCodeActive
}
