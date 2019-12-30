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
export default {
  name: 'scan',
  components: {topbar},
  data () {
    return {
      tip: '请您拿起家属联络卡，如下<span class="black-text">红色正面</span>朝上。点击下方“扫码”按钮，扫描卡上二维码绑定手机。',
      img_url: require('../assets/yellow_card.png')
    }
  },
  methods: {
    routeToScanSuccess: function () {
      this.$router.push('/ScanSuccess')
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
