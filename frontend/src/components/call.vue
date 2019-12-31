<template>
    <div class="info-container">
      <old-man-info/>
      <el-image :src="call_img" class="call-img"></el-image>
      <span class="call-text">呼叫家属</span>
    </div>
</template>

<script>
import OldManInfo from './oldManInfo'
export default {
  name: 'call',
  components: {OldManInfo},
  data () {
    return {
      call_img: require('../assets/call.png')
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
  .call-img{
    width: 10rem;
    height: 10rem;
    margin-top: 5rem;
  }
  .call-text{
    font-family: PingFangSC-Medium;
    font-size: 2.3rem;
    color: #48534A;
    letter-spacing: 0;
    text-align: center;
    font-weight: bold;
  }
</style>
