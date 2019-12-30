<template>
  <el-row class="bartop">
    <i class="el-icon-menu color-purple margin-horizontal big-font-size"/>
    <i class="linear-line"/>
    <!--<el-divider direction="vertical"></el-divider>-->
    <i class="el-icon-back color-purple margin-horizontal big-font-size"/>
  </el-row>
</template>

<script>
export default {
  name: 'topbar'
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
  }

</style>
