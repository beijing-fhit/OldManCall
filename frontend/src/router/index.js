import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import scan from '@/components/scan'
import ScanSuccess from '@/components/ScanSuccess'
import alreadyBindInfo from '@/components/alreadyBindInfo'
import addContact from '@/components/addContact'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/Hello',
      name: 'HelloWorld',
      component: HelloWorld,
      meta: {
        title: 'hello world'
      }
    },
    {
      path: '/',
      name: 'scan',
      component: scan,
      meta: {
        title: '扫码'
      }
    },
    {
      path: '/ScanSuccess',
      name: 'ScanSuccess',
      component: ScanSuccess,
      meta: {
        title: '绑定成功'
      }
    },
    {
      path: '/alreadyBindInfo',
      name: 'alreadyBindInfo',
      component: alreadyBindInfo,
      meta: {
        title: '号码绑定'
      }
    },
    {
      path: '/addContact',
      name: 'addContact',
      component: addContact,
      meta: {
        title: '号码绑定'
      }
    }
  ]
})
