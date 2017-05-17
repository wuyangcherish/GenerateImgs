<template>
  <div class="block-page">
      <!-- search -->
      <mu-text-field label="搜索" hintText="请输入你想搜索的爱豆~" type="text" v-model="person" labelFloat/><br/>
      <p class="error" v-show="err">{{errMsg}}</p>
      <mu-raised-button label="搜索" class="demo-raised-button" secondary @click="search" :disabled="isDisabled"/>
      <div class="pic-wrap">
        <mu-circular-progress :size="60" :strokeWidth="5" class="loading" v-show="loading"/>
        <img src="../../static/img/output.png" height="1024" width="1024" alt="" v-show="!loading">
      </div>
  </div>
</template>

<script>
import searchApi from '../http.js'
export default {
  name: 'hello',
  data () {
    return {
      person:'',
      loading: false,
      errMsg:"请输入查询的内容",
      err:false,
      isDisabled: false
    }
  },
  methods:{
    search(){
      if(this.person ==''){
        this.err = true 
        return false
      }
      this.loading = true;
      let searchText = this.person;
      let searchPerson = searchApi.searchPerson(searchText)
      searchPerson.then((res)=>{
            this.loading = false
            console.info("res",res.data)
      })
      .catch((err)=>{
        console.error(err)
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  .block-page{
    .pic-wrap{
      width:90%;
      max-width:1024px;
      margin:20px auto;
      img{
        width:100%;
        height:100%;
      }
      .loading{
        margin:50px auto;
      }
    }
    .error{
      color:#f44336;
      text-align:center;
      margin-top:0px;
      margin-bottom:20px;
    }
  }
</style>
