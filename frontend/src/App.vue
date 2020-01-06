<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import axios from 'axios'
export default {

  name: 'App',
  created () {
    this.getOpenId()
  },
  methods: {
    getOpenId: function () {
      axios.get('/getopenid').then(res => {
        console.log('在app.vue中获取openid成功:', res)
        sessionStorage.setItem('openId',JSON.stringify(res.data))
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
