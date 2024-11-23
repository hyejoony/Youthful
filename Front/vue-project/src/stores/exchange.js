import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router';
import { useAccountStore } from './account';

export const UseExchangeStore = defineStore('Exchange', () => {
    const exchanges= ref([])
    const API_URL =  'http://127.0.0.1:8000'


    // const saveExchanges = function () {
    //     axios({
    //         method: 'get',
    //         url: `${API_URL}/api/v1/exchanges/save/`,
    //     })
    //     .then( res => {
    //         console.log(res.data)
    //         // exchanges.value = res.data.results
    //         // console.log('echanges.value',exchanges.value)
    //     })
    //     .catch(err => console.log(err))
    // }


    const getExchanges = function () {

        const storeAccount = useAccountStore()
        axios({
            method: 'get',
            url: `${API_URL}/api/v1/exchanges/`,
            headers : {
                Authorization: `Token ${storeAccount.token}`
            }
        })
        .then( res => {
            console.log('res.data',res.data)
            exchanges.value = res.data
            console.log('get_exchanges.value',exchanges.value)
        })
        .catch(err => console.log(err))
    }
        
    const clearExchanges = function () {
        axios({
            method: 'delete',
            url: `${API_URL}/api/v1/exchanges/clear/`,
        })
        .then( res => {
            console.log('res.data',res.data)
            exchanges = ref([]) 
            exchanges.value = res.data
            console.log('clear_exchanges.value',exchanges.value)
        })
        .catch(err => console.log(err))
    }


  return { exchanges, getExchanges, clearExchanges
  }
}, { persist: true })
