<template>
  <div class="all-container">
    <topbar/>
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
import axios from 'axios'
import wx from 'weixin-js-sdk'
import config from '../config'
export default {
  name: 'scan',
  components: {topbar},
  data () {
    return {
      tip: '请您拿起家属联络卡，如下<span class="black-text">红色正面</span>朝上。点击下方“扫码”按钮，扫描卡上二维码绑定手机。',
      img_url: require('../assets/yellow_card.png')
    }
  },
  created () {
    console.log('created---')
    wx.ready(function () {
      console.log('ready-----')
    })
    wx.error(function (res) {
      console.log('error-----')
    })
    axios.get('https://agency.ucallclub.com/Common/JsApiConfig').then(config => {
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
      // this.startScan()
      this.handleScanResult('http://www.baidu.com?qrcodeid=12sdfsf3fawerbsvgswe')
    },
    startScan: function () {
      wx.scanQRCode({
        needResult: 1, // 默认为0，扫描结果由微信处理，1则直接返回扫描结果，
        scanType: ['qrCode', 'barCode'], // 可以指定扫二维码还是一维码，默认二者都有
        success: function (res) {
          var result = res.resultStr // 当needResult 为 1 时，扫码返回的结果
          this.handleScanResult(result)
          console.log('scanQrCode:', result)
        }
      })
    },
    handleScanResult: function (content) {
      if (content.indexOf('qrcodeid') !== -1) {
        var params = content.split('?')[1]
        var qrcodeid = params.split('=')[1]
        console.log('传入的qrcode是:' + config.service.verifyQrCodeActive)
        axios.get(config.service.verifyQrCodeActive, {
          params: {
            qrcodeid: qrcodeid
          }
        }).then(res => {
          // console.log('验证二维码激活状态结果:', res)
          var data = res.data
          if (data.Code === 0) {
            switch (data.ActiveState) {
              case 0:
                this.$router.push('/addContact')
                break
              case 1:
                // 判断owner和自己是否相等

                break
              default:
                // alert('二维码无效')
                this.$toast('二维码无效')
                break
            }
          }
        }).catch(res => {
          console.log('error验证二维码激活状态结果:', res)
        })
      }
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
