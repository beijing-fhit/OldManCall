<template>
    <div id="scan-success-container">
      <el-image :src="success_img_url" class="success-img"></el-image>
      <div class="status-container">
        <div v-html="bindStatusStr"/>
        <div v-text="statusTip" class="normal-tip"/>
      </div>
      <el-button type="success" class="wide-button" v-on:click.prevent="routeToScanSuccess">下一步</el-button>
    </div>
</template>

<script>
export default {
  name: 'ScanSuccess',
  data () {
    return {
      success_img_url: require('../assets/success.png'),
      bindStatusStr: '<span class="black-text">绑定成功!</span>',
      statusTip: '接下来让我们去添加联系人吧'
    }
  }
}
</script>

<style scoped>
  #scan-success-container{
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100vh;
    justify-content: center;
    align-items: center;
  }
  .success-img{
    width: 8rem;
    height: 8rem;
  }
  .status-container{
    margin-top: 1rem;
  }
  >>> .black-text{
    color: #333333;
    font-size:2rem;
    font-family: "PingFang SC";
    letter-spacing: 0.01rem;
    font-style: normal;
    font-weight: bold;
  }
  .normal-tip{
    color: #666666;
    font-size:1.6rem;
    font-family: "PingFang SC";
    letter-spacing: 0.01rem;
    font-style: normal;
    margin-top: 0.5rem;
  }
  .wide-button{
    width: 80%;
    height: 5rem;
    margin-top:10rem;
    margin-bottom: 5rem;
    letter-spacing: 0.5rem;
    font-size: 2rem;
    background-color: #1AAD19;
  }
</style>
