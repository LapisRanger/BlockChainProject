<template>
  <div>
    <h2>功能三</h2>
    <div class="testCase">
      <p>测试用例:</p>
      <ul>
        <li>1</li>
      </ul>
    </div>
    <form @submit.prevent="submit($event)">
      <p>receiptID:
        <input type="number" name="receiptID" v-model="formMess.receiptID">
      </p>
      <input type="submit" value="Submit">
    </form>
  </div>
</template>

<script>
export default {
  name: 'func3',
  data () {
    return {
      formMess: {
        'receiptID': ''
      }
    }
  },
  methods: {
    submit: function (event) {
      var formData = new FormData()
      for (var key in this.formMess) {
        if (this.formMess[key] === '') {
          alert('all input must not be empty')
          return
        }
        formData.append(key, this.formMess[key])
        console.log(key, this.formMess[key])
      }
      console.log(formData)
      this.$http({
        method: 'post',
        url: '/func3/',
        headers: {
          'Content-Type': 'multipart/form-data'
        },
        withCredentials: true,
        data: formData
      }).then(res => {
        console.log(res)
        if (res.data.result === 'success') {
          alert('合约接口调用成功')
          this.$router.push('/')
        }
      }, err => {
        console.log('error:' + err)
      })```this.$http.post('/func1/', formData).then(function (res) {
        console.log(res)
      }).catch(function (err) {
        console.log('error:' + err)
      })```
    }
  }
}
</script>

<style scoped>
  form{
    text-align: center;
    width: 100%;
  }
  input,p,label{
    vertical-align: middle;
  }
  li{
    list-style: none;
  }
  .testCase{
    bottom: 0;
    position: fixed;
    left: 0;
    width: 100%;
  }
</style>
