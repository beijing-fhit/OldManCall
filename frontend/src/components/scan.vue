<template>
  <div class="all-container">
    <topbar :hide-back-btn="true"/>
    <div class="img-text-container">
      <div class="text-container">
        <label v-html="this.tip" class="label-style"></label>
      </div>
      <el-image :src="img_url" class="img-style"></el-image>
    </div>
    <el-button type="success" class="wide-button" v-on:click.prevent="routeToScanSuccess">扫码</el-button>
  </div>
</template>

<script>
import topbar from './topbar'
import wx from 'weixin-js-sdk'
import api from '../api'
export default {
  name: 'scan',
  components: {topbar},
  data () {
    return {
      tip: '请您拿起家属联络卡，如下<span class="black-text">红色正面</span>朝上。点击下方“扫码”按钮，扫描卡上二维码绑定手机。',
      img_url: require('../assets/yellow_card.png')
    }
  },
  mounted () {
    console.log('created---')
    wx.ready(function () {
      console.log('ready-----')
    })
    wx.error(function (res) {
      console.log('error-----')
    })
    api.wxConfig().then(config => {
      console.log('config', config.data)
      wx.config({
        debug: false,
        appId: config.data.appId,
        timestamp: config.data.timestamp,
        nonceStr: config.data.nonceStr,
        signature: config.data.signature,
        jsApiList: ['scanQRCode']
      })
    })
  },
  methods: {
    routeToScanSuccess: function () {
      // this.$router.push('/ScanSuccess')
      this.startScan()
      // 已激活二维码
      // this.handleScanResult('http://wechatcall.ucallclub.com/ucall/call?type=1&eqrcodeid=da887208fe9a414b81da578b52102012')
      // 未激活二维码
      // this.handleScanResult('http://wechatcall.ucallclub.com/ucall/call?type=1&eqrcodeid=2de95313459d4064a67a295fab195642')
    },
    startScan: function () {
      var that = this
      var ucallFreeId = sessionStorage.getItem('UcallFreeId')
      if (ucallFreeId === null || ucallFreeId === '' || ucallFreeId === 'undefined' || ucallFreeId === undefined) {
        return
      }
      wx.scanQRCode({
        needResult: 1, // 默认为0，扫描结果由微信处理，1则直接返回扫描结果，
        scanType: ['qrCode', 'barCode'], // 可以指定扫二维码还是一维码，默认二者都有
        success: function (res) {
          var result = res.resultStr // 当needResult 为 1 时，扫码返回的结果
          that.handleScanResult(result)
          console.log('scanQrCode:', result)
        }
      })
    },
    handleScanResult: function (content) {
      var that = this
      if (content.indexOf('eqrcodeid') !== -1) { // 注意，这里判断了二维码内容里面的url包含eqrcodeid
        var substr = content.split('?')[1]
        // var params = substr.split('&')
        var qrcodeid = this.getQueryValue(substr, 'eqrcodeid')
        console.log('传入的qrcode是:' + qrcodeid)
        sessionStorage.setItem('qrCodeId', qrcodeid)
        api.verifyQrCodeActive(qrcodeid).then(res => {
          console.log('验证二维码激活状态结果:', res)
          var UcallFreeId = sessionStorage.getItem('UcallFreeId')
          console.log('本地的UCallfreeid为:', UcallFreeId)
          var data = res.data
          if (data.Code === 0) {
            switch (data.ActiveState) {
              case 0:
                // 未激活
                sessionStorage.setItem('isQrCodeActive', 0)
                that.$router.push('/addContact')
                break
              case 1:
                // 已激活
                sessionStorage.setItem('isQrCodeActive', 1)
                // 判断owner和自己是否相等
                if (data.Owner === UcallFreeId) {
                  // 此二维码属于自己
                  that.$router.push('/settings')
                } else {
                  // 此二维码属于别人
                  that.$router.push('/alreadyBindInfo')
                }
                break
              default:
                // alert('二维码无效')
                that.$toast('二维码无效')
                break
            }
          }
        }).catch(res => {
          console.log('error验证二维码激活状态结果:', res)
        })
      }
    },

    getQueryValue: function (str, queryName) {
      var vars = str.split('&')
      for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=')
        if (pair[0] === queryName) {
          return pair[1]
        }
      }
      return null
    }

  }
}
</script>

<style scoped>
  .all-container{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .img-text-container{
    display: flex;
    flex-direction: row;
    justify-content: center;
    margin: 5rem 5rem;
    position: relative;
  }
  .img-style{
  }
  .text-container{
    padding: 10% 5vw;
    position: absolute;
    z-index: 2;
  }

  .label-style{
    font-size:1.5rem;
    font-family: "PingFang SC";
    color: #666666;
    letter-spacing: 0.01rem;
  }
  /deep/ .black-text{
    color: #121212;
    font-size:1.5rem;
    font-family: "PingFang SC";
    letter-spacing: 0.01rem;
    font-style: normal;
    font-weight: bold;
  }
  .wide-button{
    width: 80%;
    height: 5rem;
    margin-top: 5rem;
    margin-bottom: 5rem;
    letter-spacing: 0.5rem;
    font-size: 2rem;
    background-color: #1AAD19;

  }
</style>
