<template>
  <div class="info-container">
    <el-image :src="heart_img_url" class="heart-img"></el-image>
    <div class="bind-info">{{bind_info}}</div>
    <old-man-info></old-man-info>
    <el-button type="success" class="wide-button">返回</el-button>
  </div>
</template>

<script>
import oldManInfo from './oldManInfo'
export default {
  name: 'alreadyBindInfo',
  components: {oldManInfo},
  data () {
    return {
      heart_img_url: require('../assets/heart.png'),
      bind_info: '该二维码已经绑定过了'
    }
  }
}
</script>

<style scoped>
.info-container{
  margin-top: 4rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.heart-img {
  width: 90%;
  height: 14vh;
}

.bind-info {
  font-family: PingFangSC-Medium;
  font-size: 2rem;
  color: #333333;
  letter-spacing: 0;
  font-weight: bold;
  margin-top: 1rem;
  margin-bottom: 2rem;
}

.wide-button {
  width: 80%;
  height: 5rem;
  margin-top: 5rem;
  margin-bottom: 2rem;
  letter-spacing: 0.5rem;
  font-size: 2rem;
  background-color: #1AAD19;
}
</style>
