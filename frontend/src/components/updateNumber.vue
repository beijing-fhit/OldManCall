<template>
  <div>
    <topbar class="topbar"></topbar>
    <!--联系人信息-->
    <div class="contact-panel">
      <el-row class="contact-item border-bottom" >
        <span class="contact-name">联系人1</span>
        <span class="contact-number">手机号码</span>
        <!--<div class="img-container">-->
          <i class="el-icon-delete delete-img"/>
        <!--</div>-->
        <!--<el-image :src="delete_img" class="delete-img"></el-image>-->
      </el-row>
     <el-row class="contact-item border-bottom" >
        <span class="contact-name">联系人2</span>
        <span class="contact-number">手机号码</span>
        <i class="el-icon-delete delete-img"/>
      </el-row>
      <el-row class="contact-item" >
        <span class="contact-name">联系人3</span>
        <span class="contact-number">手机号码</span>
        <i class="el-icon-delete delete-img"/>
      </el-row>
    </div>
    <el-button type="success" class="wide-button">确定</el-button>
  </div>
</template>

<script>
import Topbar from './topbar'
export default {
  name: 'updateNumber',
  components: {Topbar},
  data () {
    return {
      delete_img: require('../assets/delete.png')
    }
  }
}
</script>

<style scoped>
 .topbar {
    background: #F9F9FA !important;
  }

  .contact-panel{
    background-color: white;
    display: flex;
    flex-direction: column;
    align-items: left;
    justify-content: center;
    padding-left: 3vw;
  }

  .contact-item {
    width: 100%;
    height: 5rem;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;

  }

  .border-bottom {
    border-bottom: 0.01rem inset #E5E5E5;
  }

  .contact-name {
    width: 30%;
    font-size: 2rem;
    font-family: PingFangSC-Regular;
    color: #48534A;
    letter-spacing: 0;
    display: flex;
    flex-direction: row;
    justify-content: left;
    align-items: center;
  }

  .contact-number {
    width: 60%;
    font-size: 2rem;
    font-family: PingFangSC-Regular;
    color: #B2B2B2;
    letter-spacing: 0;
    margin-left: 5%;
    display: flex;
    flex-direction: row;
    justify-content: left;
    align-items: center;
  }
  .img-container{
    display: flex;
    flex-direction: row;
    justify-content: right;
    align-items: center;
    width: 10%;
  }
  .delete-img{
    font-size: 2.5rem;
    color: red;
    /*margin-left: 2vw;*/
    margin-right: 3vw;
  }

  .wide-button {
    width: 80%;
    margin-top: 10rem;
    margin-bottom: 10rem;
    letter-spacing: 0.5rem;
    font-size: 2rem;
    background-color: #1AAD19;
}
</style>
