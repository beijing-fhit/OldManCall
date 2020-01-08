<template>
  <div>
    <div >
      <Topbar class="topbar"/>
    </div>
    <div class="item-title" v-on:click.prevent="routeToCallUpdatePage">
      <span class="title-text">联系人号码绑定/修改</span>
      <i class="el-icon-arrow-right big-font-size"/>
    </div>
    <!--联系人信息-->
    <div class="contact-panel" v-for="(item,index) in contact" v-bind:key="index">
      <el-row class="contact-item border-bottom" >
        <span class="contact-name">联系人{{(index+1)}}</span>
        <span class="contact-number">{{item}}</span>
      </el-row>
     <!--<el-row class="contact-item border-bottom" >-->
        <!--<span class="contact-name">联系人2</span>-->
        <!--<span class="contact-number">手机号码</span>-->
      <!--</el-row>-->
      <!--<el-row class="contact-item" >-->
        <!--<span class="contact-name">联系人3</span>-->
        <!--<span class="contact-number">手机号码</span>-->
      <!--</el-row>-->
    </div>
    <!--填写老人信息-->
    <div class="item-title border-bottom">
      <span class="title-text">信息填写</span>
     </div>
    <div class="info-fill-panel leftpadding">
      <el-row class="info-item border-bottom ">
        <span class="info-name">姓名</span>
        <el-input v-model="manInfo.name" class="info-content normal-input-style no-border-input" placeholder="预设内容(必填)" clearable></el-input>
      </el-row>
      <el-row class="info-item border-bottom ">
        <span class="info-name">地址</span>
        <el-input v-model="manInfo.address" class="info-content normal-input-style no-border-input" placeholder="预设内容" clearable></el-input>
      </el-row>
    </div>
      <el-row class="info-item border-bottom leftpadding white-bg">
        <span class="info-name">年纪</span>
        <el-input v-model="manInfo.age" class="info-content normal-input-style no-border-input" placeholder="预设内容" clearable></el-input>
      </el-row>
    <div class="info-fill-panel leftpadding">
      <el-row class="info-item border-bottom">
        <span class="info-name">病史</span>
        <el-input v-model="manInfo.medical_history" class="info-content normal-input-style no-border-input" placeholder="预设内容" clearable></el-input>
      </el-row>
      <el-row class="info-item border-bottom">
        <span class="info-name">过敏史</span>
        <el-input v-model="manInfo.allergy" class="info-content normal-input-style no-border-input" placeholder="预设内容" clearable></el-input>
      </el-row>
    </div>

      <el-row class="info-item border-bottom leftpadding white-bg">
        <span class="info-name">血型</span>
        <el-input v-model="manInfo.blood_type" class="info-content normal-input-style no-border-input" placeholder="预设内容" clearable></el-input>
      </el-row>
    <div class="info-fill-panel leftpadding ">
      <el-row class="info-item border-bottom">
        <span class="long-info-name">正在吃的药</span>
        <el-input v-model="manInfo.drugs" class="long-info-content normal-input-style no-border-input" placeholder="预设内容" clearable></el-input>
      </el-row>
      <el-row class="info-item">
        <span class="long-info-name">正在进行的治疗</span>
        <el-input v-model="manInfo.treatment" class="long-info-content normal-input-style no-border-input" placeholder="预设内容" clearable></el-input>
      </el-row>
    </div>
    <el-button type="success" class="wide-button" @click="saveInfo">确定</el-button>
  </div>
</template>

<script>
import Topbar from './topbar'
import api from '../api'
export default {
  name: 'settings',
  components: {Topbar},
  data () {
    return {
      manInfo: {
        name: '',
        address: '',
        age: '',
        medical_history: '',
        allergy: '',
        blood_type: '',
        drugs: '',
        treatment: ''
      },
      contact: this.getContact()
    }
  },
  methods: {
    routeToCallUpdatePage: function () {
      this.$router.push('/updateNumber')
    },
    getContact: function () {
      var contact = sessionStorage.getItem('contact').split(',')
      return contact
    },
    saveInfo: function () {
      // 保存老人信息
      // 判空
      if (this.manInfo.name.length === 0) {
        this.$toast('姓名不能为空!')
        return
      }
      // 调用后端接口，保存老人信息到数据库
      api.saveInfo().then(res => {
        // 保存信息成功
        console.log('保存信息成功:', res)
      }).catch(err => {
        // 保存信息失败
        console.log('保存信息失败:', err)
      })
    }
  }
}
</script>

<style scoped>
  .topbar {
    background: #F9F9FA !important;
  }

  .item-title {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    height: 6rem;
    width: 100%;
    background-color: #FFFFFF;
  }
  .margin-horizontal{
    padding-left: 3vw;
    padding-right: 3vw;
  }

  .title-text {
    font-family: PingFangSC-Medium;
    font-size: 2rem;
    color: #48534A;
    letter-spacing: 0;
    font-weight: bold;
    text-align: center;
    margin-left: 3vw;
  }

  .big-font-size {
    font-size: 2.2rem;
    margin-right: 3vw;
  }
  .contact-panel{
    background-color: #FAFAFA;
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
    width: fit-content;
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
    width: fit-content;
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
  /*填写老人信息的区域*/
  .info-fill-panel{
    background-color: #FFFFFF;
    display: flex;
    flex-direction: column;
    align-items: left;
    justify-content: center;
    /*padding-left: 3vw;*/
  }

  .leftpadding{
    padding-left: 3vw;
  }
  .info-item{
    width: 100%;
    height: 5rem;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
  }
  .full-width-info-item{
    width: 100%;
    height: 5rem;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    padding-left: 3vw;
  }
  .info-name{
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
  .info-content{
     width: 70%;
    font-size: 2rem;
    font-family: PingFangSC-Regular;
    color: #B2B2B2;
    letter-spacing: 0;
    display: flex;
    flex-direction: row;
    justify-content: left;
    align-items: center;
  }
  .long-info-name{
     width: 45%;
    font-size: 2rem;
    font-family: PingFangSC-Regular;
    color: #48534A;
    letter-spacing: 0;
    display: flex;
    flex-direction: row;
    justify-content: left;
    align-items: center;
  }
  .long-info-content{
     width: 55%;
    font-size: 2rem;
    font-family: PingFangSC-Regular;
    color: #B2B2B2;
    letter-spacing: 0;
    display: flex;
    flex-direction: row;
    justify-content: left;
    align-items: center;
  }
  /*input 样式*/
   .normal-input-style{
    font-family: PingFangSC-Regular;
    font-size: 2rem;
    color: #B2B2B2;
    letter-spacing: 0;
  }
  /deep/ .no-border-input .el-input__inner{
   border: 0 none;
    color: #48534A;
    max-lines: 1;
    padding: 0;
    font-size: 2rem;
  }
  .wide-button {
    width: 80%;
    margin-top: 10rem;
    margin-bottom: 10rem;
    letter-spacing: 0.5rem;
    font-size: 2rem;
    background-color: #1AAD19;
}
  .white-bg{
    background-color: #FFFFFF;
  }
</style>
