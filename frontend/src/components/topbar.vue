<template>
  <el-row class="bartop">
    <i class="el-icon-menu color-purple margin-horizontal big-font-size" @click="goHome"/>
    <i class="linear-line"/>
    <!--<el-divider direction="vertical"></el-divider>-->
    <i class="el-icon-back color-purple margin-horizontal big-font-size" v-show="!hideBackBtn" @click="onBackTap"/>
    <div v-show="this.showSaveBtn" class="save-area" @click="save">
      <el-image :src="save_icon_url" class="color-purple img-icon-style"/>
      <span class="color-purple small-font-size margin-left-style">保存</span>
    </div>
  </el-row>
</template>

<script>
export default {
  name: 'topbar',
  data: function () {
    return {
      save_icon_url: require('../assets/save.png')
    }
  },
  methods: {
    save: function () {
      this.$emit('saveInfo')
    },
    onBackTap: function () {
      this.$router.back()
    },
    goHome: function () {
      this.$router.push('/')
    }
  },
  props: {
    showSaveBtn: false,
    hideBackBtn: false
  }
}
</script>

<style scoped>
  .bartop {
    display: flex;
    flex-direction: row;
    justify-content: left;
    align-items: center;
    height: 5rem;
    width: 100%;
    background-color: white;
  }

  .margin-horizontal {
    margin-left: 3vw;
    margin-right: 3vw;
  }

  .linear-line{
    width: 0.2rem;
    height: 50%;
    background-color: lightgray;
    border-radius:0.1rem;
  }
  .color-purple {
    color: #432B99;
  }
  .big-font-size{
    font-size: 3rem;
    font-family: "PingFang SC";
  }
  .small-font-size{
    font-size: 1.7rem;
    font-family: "PingFang SC";
  }
  .img-icon-style{
    width: 2.5rem;
    height: 2.5rem;
  }
  .margin-left-style{
    margin-left: 0.5rem;
  }
  /*.bartop:last-child{*/
    /*margin-left: auto;*/
    /*margin-right: 2rem;*/
  /*}*/
  .save-area{
    margin-left: auto;
    margin-right: 2rem;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }
</style>
