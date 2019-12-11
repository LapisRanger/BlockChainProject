import Vue from 'vue'
import Router from 'vue-router'
import func1 from '../components/func1'
import func2 from '../components/func2'
import func3 from '../components/func3'
import func4 from '../components/func4'
import HomePage from '../components/HomePage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/func1',
      name: 'func1',
      component: func1
    },
    {
      path: '/func2',
      name: 'func2',
      component: func2
    },
    {
      path: '/func3',
      name: 'func3',
      component: func3
    },
    {
      path: '/func4',
      name: 'func4',
      component: func4
    }
  ]
})
