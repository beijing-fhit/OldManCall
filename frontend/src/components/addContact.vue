<template>
  <div class="all-container">
    <topbar/>
    <el-row class="add-tip">
      <i class="linear-line margin-horizontal"/>
      <span class="tip-text">您最多可以绑定3位联系人</span>
    </el-row>
    <!--绑定联系人区域-->
    <div class="contact-panel">
      <el-row class="first-item">
        <i class="el-icon-star-on red-star margin-horizontal"></i>
        <span class="title-name">联系人</span>
        <span class="title-tip">(必填)</span>
      </el-row>
      <el-row class="first-input-container bottom-border">
        <el-input type="number" v-model="number1" class="normal-input-style no-border-input" placeholder="请输入手机号码"
                  clearable></el-input>
      </el-row>
      <el-row class="second-input-container">
        <el-input type="number" v-model="number2" class="normal-input-style no-border-input sixty-percent"
                  placeholder="请输入验证码"></el-input>
        <span class="fourty-percent verify-code-text-btn">获取验证码</span>
      </el-row>
    </div>
    <el-button type="success" class="wide-button" @click="centerDialogVisible = true">确定</el-button>
    <el-dialog
      :visible.sync="centerDialogVisible"
      title="绑定成功"
      width="80%"
      :show-close="false"
      center>
      <span class="center-dialog-content">还需要再添加一位联系人么？</span>
      <span slot="footer" class="dialog-footer dialog-btn-group">
        <span @click="centerDialogVisible = false" class="skip-btn">跳过</span>
        <span type="primary" @click="centerDialogVisible = false" class="add-another-btn">添加下一位</span>
      </span>
    </el-dialog>
  </div>
</template>
<script>
import Topbar from './topbar'
export default {
  name: 'addContact',
  components: {Topbar},
  data () {
    return {
      number1: '',
      number2: '',
      centerDialogVisible: false
    }
  }
}
</script>

<style scoped>
  .all-container{
    /*width: 100%;*/
    /*height: fit-content;*/
  }
  .add-tip {
    display: flex;
    flex-direction: row;
    align-items: center;
    height: 6rem;
    width: fit-content;
  }
  .linear-line {
    width: 0.3rem;
    height: 50%;
    background-color: #1AAD19;
    border-radius: 0.2rem;
  }
  .margin-horizontal{
    margin-left: 3vw;
    margin-right: 3vw;
  }
  .tip-text{
    font-family: PingFangSC-Regular;
    font-size: 1.9rem;
    color: #666666;
    letter-spacing: 0;
  }
  .contact-panel{
    display: flex;
    flex-direction: column;
    align-items: left;
    justify-content: center;
    background-color:#FFFFFF ;
    width: 100%;
    height: fit-content;
  }
  .first-item{
    display: flex;
    flex-direction: row;
    align-items: center;
    height: 5rem;
  }
  .red-star{
    color: red;
    font-size: 1.5rem;
  }
  .title-name{
    font-family: PingFangSC-Regular;
    font-size: 2rem;
    color: #48534A;
    letter-spacing: 0;
  }
  .title-tip{
    font-family: PingFangSC-Regular;
    font-size: 2rem;
    color: #B2B2B2;
    letter-spacing: 0;
  }
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
  .first-input-container{
    width: fit-content;
    margin-left: 3vw;
    padding-right: 4vw;
    height: 5rem;
    width: 97%;
  }
  .bottom-border{
    border-bottom: 0.05rem inset #E5E5E5;
  }
  .second-input-container{
    width: 100%;
    margin-left: 3vw;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    height: 5rem;
  }
  .sixty-percent{
    width: 60%;
  }
  .fourty-percent{
    width: 40%;
  }
  .verify-code-text-btn{
    font-size: 1.8rem;
    font-family: PingFangSC-Regular;
    color: #1AAD19;
    letter-spacing: 0;
  }
  .wide-button {
    width: 80%;
    margin-top: 20rem;
    margin-bottom: 10rem;
    letter-spacing: 0.5rem;
    font-size: 2rem;
    background-color: #1AAD19;
}

  /*dialog style*/
  .center-dialog-content{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    font-size: 1.6rem;
  }
  .dialog-btn-group{
    width: 100%;
    height: 5rem;
    display: flex;
    flex-direction: row;
    justify-content:space-evenly;
    align-items: center;
    border-top: 0.05rem inset #E5E5E5;

  }
  .skip-btn{
    font-size: 1.8rem;
    color: #000;
    width: 50%;
    border-right: 0.1rem inset #E5E5E5;
    font-family: PingFangSC-Regular;
    text-align: center;
  }
  .add-another-btn{
    font-size: 1.8rem;
    width: 50%;
    font-family: PingFangSC-Regular;
    color: #02BB00;
    text-align: center;
  }
  /deep/ .el-dialog__footer{
    padding: 0;
  }
</style>
