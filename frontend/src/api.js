import axios from 'axios'
/**
 * 封装request方法
 */
function request(url, method, header, data) {
  return new Promise((resove, reject) => {
    axios.request(url,{
      data: data ? data : {},
      header: header ? header : {},
      method: method.toUpperCase(),
      success: function (res) {
        resove(res.data)
      },
      fail: function (err) {
        reject(JSON.stringify(err))
      }
    })
  })
}

/**
 * GET请求
 */
var requestGet = (url, data, header) => {
  return request(url, 'GET', header, data)
}
/**
 * POST请求
 */
var requestPost = (url, data, header) => {
  return request(url, 'POST', header, data)
}
/**
 * PUT请求
 */
var requestPut = (url, data, header) => {
  return request(url, 'PUT', header, data)
}
/**
 * DELETE请求
 */
var requestDelete = (url, data, header) => {
  return request(url, 'DELETE', header, data)
}


/**
 * 用户登录
 */
var login = () => {
  return new Promise((resove, reject) => {
    wx.login({
      success: resove,
      fail: reject
    })
  })
}
/**
 * 获取分享信息
 */
var getShareInfo = (sTicket) => {
  return new Promise((resove, reject) => {
    wx.getShareInfo({
      shareTicket: sTicket,
      success: resove,
      fail: reject
    })
  })
}
var checkSession = () => {
  return new Promise((resove, reject) => {
    wx.checkSession({
      success: resove,
      fail: reject
    })
  })
}
module.exports = {requestGet, requestPost, requestPut, requestDelete, login, getShareInfo, checkSession}
