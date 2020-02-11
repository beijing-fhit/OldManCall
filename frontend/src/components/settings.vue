<template>
  <div>
    <div >
      <Topbar class="topbar" :show-save-btn="true" @saveInfo="saveInfo"/>
    </div>
    <div class="item-title">
      <span class="title-text">联系人号码绑定/修改</span>
      <!--<i class="el-icon-arrow-right big-font-size"/>-->
    </div>
    <!--联系人信息-->
    <!--<div class="contact-panel" v-for="(item,index) in contact" v-bind:key="index">-->
    <div class="contact-panel">
      <el-row class="contact-item border-bottom">
        <span class="contact-name">联系人1</span>
        <span class="contact-number" @click="modifyContact(0)">{{contact[0]=== undefined||contact[0]=== "undefined"||contact[0]=== null||contact[0]=== ""?text1:contact[0]}}</span>
        <span class="delete-img"/>
      </el-row>
      <el-row class="contact-item border-bottom">
        <span class="contact-name">联系人2</span>
        <span class="contact-number" @click="modifyContact(1)">{{contact[1]=== undefined||contact[1]=== "undefined"||contact[1]=== null||contact[1]=== ""?text1:contact[1]}}</span>
        <el-popconfirm
          confirm-button-text="确定"
          cancel-button-text="取消"
          icon="el-icon-info"
          iconColor="red"
          @onConfirm="deleteContact(1)"
          title="删除该联系人吗？">
          <i slot="reference" class="el-icon-delete delete-img" v-show="showContact2Delete"/>
        </el-popconfirm>
      </el-row>
      <el-row class="contact-item">
        <span class="contact-name">联系人3</span>
        <span class="contact-number" @click="modifyContact(2)">{{contact[2]=== undefined||contact[2]=== "undefined"||contact[2]=== null||contact[2]=== ""?text1:contact[2]}}</span>
        <el-popconfirm
          confirm-button-text="确定"
          cancel-button-text="取消"
          icon="el-icon-info"
          iconColor="red"
          @onConfirm="deleteContact(2)"
          title="删除该联系人吗？">
          <i class="el-icon-delete delete-img" v-show="showContact3Delete" @click="deleteContact(2)"/>
        </el-popconfirm>
      </el-row>
    </div>
    <!--</div>-->
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
    <el-button type="success" class="wide-button" @click="saveInfo">保存</el-button>
  </div>
</template>

<script>
import Topbar from './topbar'
import api from '../api'
export default {
  name: 'settings',
  components: {Topbar},
  inject: ['reload'],
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
      text1: '请输入手机号码',
      text2: '请输入手机号码',
      contact: this.getContact(),
      showContact2Delete: false,
      showContact3Delete: false
    }
  },
  created: function () {
    // 获取有无数据
    api.getInfo(sessionStorage.getItem('qrCodeId')).then(res => {
      //  获取数据
      console.log('settings 获取info:', res)
      if (res.data.status_code === 0) {
        var data = res.data.data
        this.manInfo.name = data.old_man_info.name
        this.manInfo.age = data.old_man_info.age
        this.manInfo.address = data.old_man_info.address
        this.manInfo.medical_history = data.old_man_info.medical_history
        this.manInfo.allergy = data.old_man_info.allergy
        this.manInfo.blood_type = data.old_man_info.blood_type
        this.manInfo.drugs = data.old_man_info.drugs
        this.manInfo.treatment = data.old_man_info.treatment
        // this.contact = data.phone_number
        // 如果从addContact页面跳转过来的，则不使用网络上获取到的号码
        if (this.$route.query.getPhoneNumberFromNet !== null && this.$route.query.getPhoneNumberFromNet === false) {
          return
        }
        sessionStorage.setItem('contact', this.generatePhoneStr(data.phone_number))
        // sessionStorage.setItem('contact', data.phone_number)
        console.log('generateStr:', data.phone_number)
        this.contact = this.getContact()
      }
    })
  },
  methods: {
    routeToCallUpdatePage: function () {
      this.$router.push('/updateNumber')
    },
    generatePhoneStr: function (phoneNumbers) {
      var str = ''
      for (var i = 0; i < phoneNumbers.length; i++) {
        var p = phoneNumbers[i]
        str += p + ','
      }
      str = str.substr(0, str.length - 1)
      return str
    },
    getleagalContact: function (contact) {
      var c = []
      var count = 0
      var temp = contact
      for (var i = 0; i < temp.length; i++) {
        if (temp[i] !== null && temp[i] !== '' && temp[i] !== undefined && temp[i] !== 'undefined') {
          c[count] = temp[i]
          count++
        }
      }
      return c
    },
    getContact: function () {
      if (sessionStorage.getItem('contact') !== null) {
        var contact = sessionStorage.getItem('contact').split(',')
        switch (contact.length) {
          case 1:
            // this.text1 = '请输入手机号码'
            // this.text2 = '请输入手机号码'
            this.showContact2Delete = false
            this.showContact3Delete = false
            break
          case 2:
            this.showContact2Delete = true
            this.showContact3Delete = false
            // this.text2 = '请输入手机号码'
            // this.text1 = contact[1]
            break
          case 3:
            this.showContact2Delete = true
            this.showContact3Delete = true
            // this.text1 = contact[1]
            // this.text2 = contact[2]
            break
        }
        console.log('contact:', contact)
        return contact
      }
      return []
    },
    modifyContact: function (index) {
      if (index === 2) {
        if (this.text1 === '') {
          this.$toast('请先绑定第二个联系人！')
          return
        }
      }
      // var mode = 0 // 0代表修改，1代表新增
      this.$router.push({
        path: '/addContact',
        query: {
          modifyNumber: this.contact[index],
          index: index,
          mode: this.contact[index] === '' ? 1 : 0
        }
      })
    },
    deleteContact: function (index) {
      this.contact[index] = ''
      sessionStorage.setItem('contact', this.generatePhoneStr(this.contact))
      this.contact = this.getContact()
      this.reload()
    },
    saveInfo: function () {
      // this.$router.push('/call')
      // 保存老人信息
      // 判空
      if (this.manInfo.name.length === 0) {
        this.$toast('姓名不能为空!')
        return
      }
      // qrCodeId, oldManInfo, phone_number
      var qrCodeId = sessionStorage.getItem('qrCodeId')
      var info = this.manInfo
      var phoneNumber = this.getleagalContact(this.contact)
      console.log('合法的contact:', phoneNumber)
      // 调用后端接口，保存老人信息到数据库
      api.saveInfo(qrCodeId, info, phoneNumber).then(res => {
        // 保存信息成功
        console.log('保存信息成功:', res)
        if (res.data.status_code === 0) {
          this.$toast(res.message)
          console.log('二维码激活状态:', sessionStorage.getItem('isQrCodeActive'))
          if (sessionStorage.getItem('isQrCodeActive') === 0 || sessionStorage.getItem('isQrCodeActive') === '0') { // 未激活
            // 激活二维码
            api.activateQrCode(sessionStorage.getItem('openId'), qrCodeId, sessionStorage.getItem('UcallFreeId'))
              .then(res => {
                if (res.data.Code === 0) {
                  this.$toast('激活二维码成功')
                  this.$router.push('/call')
                  console.log('激活二维码成功:', res)
                } else {
                  this.$toast('激活二维码失败')
                  console.log('激活二维码失败:', res)
                }
              })
              .catch(err => {
                this.$toast('激活二维码失败')
                console.log('激活二维码失败:', err)
              })
          } else {
            this.$toast('保存信息成功')
            this.$router.push('/call')
          }
        } else {
          this.$toast('保存信息失败')
        }
      }).catch(err => {
        // 保存信息失败
        console.log('保存信息失败:', err)
        this.$toast('保存信息失败')
      })
    }
  }
}
</script>

<style scoped>
  .topbar {
    background: #FFFFFF !important;
  }

  .item-title {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    height: 6rem;
    width: 100%;
    background-color: #FAFAFA;
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
    background-color: #FFFFFF;
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

  .delete-img {
    font-size: 2.5rem;
    color: red;
    /*margin-left: 2vw;*/
    margin-right: 3vw;
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
