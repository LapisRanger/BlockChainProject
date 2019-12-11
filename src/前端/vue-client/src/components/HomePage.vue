<template>
  <div class="myApp">
    <h1>Fisco-Bcos供应链系统</h1>
    <div class="btnArr">
      <button @click="func1">功能一</button><br>
      <button @click="func2">功能二</button><br>
      <button @click="func3">功能三</button><br>
      <button @click="func4">功能四</button>
    </div>
    <div class="userManual">
      <h3>用户手册:</h3>
      <ol>
        <li>功能一：实现采购商品—签发应收账款交易上链。例如车企从轮胎公司购买一批轮胎并签订应收账款单据。</li>
        <li>功能二：实现应收账款的转让上链，轮胎公司从轮毂公司购买一笔轮毂，便将于车企的应收账款单据部分转让给轮毂公司。轮毂公司可以利用这个新的单据去融资或者要求车企到期时归还钱款</li>
        <li>功能三：利用应收账款向银行融资上链，供应链上所有可以利用应收账款单据向银行申请融资</li>
        <li>功能四：应收账款支付结算上链，应收账款单据到期时核心企业向下游企业支付相应的欠款</li>
      </ol>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  methods: {
    func1: function () {
      this.$router.push('/func1')
    },
    func2: function () {
      this.$router.push('/func2')
    },
    func3: function () {
      this.$router.push('/func3')
    },
    func4: function () {
      this.$router.push('/func4')
    }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
 li{
   width: 100%;
   text-align: left;
 }
  .userManual{
    bottom: 0;
    position: fixed;
    left: 0;
    width: 100%;
  }
  button{
    margin-bottom: 10px;
    font-size: 18px;
    background-color: #93d0ea;
    box-shadow: #8fcde7;
  }
</style>
