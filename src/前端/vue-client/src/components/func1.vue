<template>
  <div>
    <h2>功能一</h2>
    <div class="testCase">
      <p>测试用例:</p>
      <ul>
        <li>tire</li>
        <li>car</li>
        <li>1000</li>
        <li>2019-12-11</li>
      </ul>
    </div>
    <form @submit.prevent="submit($event)">
      <p>lender:
        <label><input type="radio" name="lender" value='car' v-model="formMess.lender">car</label>
        <label><input type="radio" name="lender" value='tire' v-model="formMess.lender">tire</label>
        <label><input type="radio" name="lender" value='hub' v-model="formMess.lender">hub</label>
      </p>
      <p>borrower:
        <label><input type="radio" name="borrower" value='car' v-model="formMess.borrower">car</label>
        <label><input type="radio" name="borrower" value='tire' v-model="formMess.borrower">tire</label>
        <label><input type="radio" name="borrower" value='hub' v-model="formMess.borrower">hub</label>
      </p>
      <p>amount:<input type="number" name="amount" v-model="formMess.amount"></p>
      <p>payDate:<input type="date" name="payDate" v-model="formMess.payDate"></p>
      <input type="submit" value="Submit">
    </form>
  </div>
</template>

<script>
export default {
  name: 'func1',
  data () {
    return {
      formMess: {
        'lender': '',
        'borrower': '',
        'amount': '',
        'payDate': ''
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
        if (key === 'amount') {
          if (this.formMess[key] <= 0) {
            alert('amount must larger than 0')
            return
          }
        }
        formData.append(key, this.formMess[key])
        console.log(key, this.formMess[key])
      }
      if (this.formMess['lender'] === this.formMess['borrower']) {
        alert('lender and borrower must be different')
        return
      }
      console.log(formData)
      this.$http({
        method: 'post',
        url: '/func1/',
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
