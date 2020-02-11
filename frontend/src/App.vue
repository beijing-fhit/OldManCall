<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
// import axios from 'axios'
import api from './api'
export default {

  name: 'App',
  provide () {
    return {
      reload: this.reload
    }
  },
  data () {
    return {
      isRouterAlive: true
    }
  },
  created () {
    this.getOpenId()
  },
  methods: {
    getOpenId: function () {
      api.getOpenId().then(res => {
        console.log('在app.vue中获取openid成功:', res)
        let openId = res.data
        sessionStorage.setItem('openId', openId)
        // 获取用户状态，保存其中的ucallfreeid
        api.weChatState(openId).then(res => {
          // console.log('weChatState', res)
          sessionStorage.setItem('UcallFreeId', res.data.UcallFreeId)
          sessionStorage.setItem('Tel', res.data.Tel[0])
        }).catch(res => {
          console.log('webChatState error', res)
        })
      }).catch(res => {
        console.log('在app.vue中获取openid失败:', res)
      })
    },
    reload () {
      this.isRouterAlive = false
      this.$nextTick(function () {
        this.isRouterAlive = true
      })
    }
  }
}
</script>

<style>
  body {
    background-color: #F9F9FA;
    padding: 0;
    margin: 0;
  }

  html {
    font-size: 62.5%;
    padding: 0;
    margin: 0;
  }

  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    /*color: #2c3e50;*/
    /*margin-top: 60px;*/
  }
</style>
